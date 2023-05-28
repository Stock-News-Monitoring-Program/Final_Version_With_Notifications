from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import pymysql
from .config import HOST, USER, PASSWORD, DATABASE
from .total_stock_list import total_stock_list

auth = Blueprint('auth', __name__)

pymysql.install_as_MySQLdb()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                session['email'] = email  # Store email in session
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
        session['email'] = email  # Store email in session even if user does not exist or password is incorrect

    # Retrieve the email from session if available
    email = session.get('email')

    return render_template("login.html", user=current_user, email=email)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form_data = {}

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        stock_1 = request.form.get('stock_1')
        stock_2 = request.form.get('stock_2')
        stock_3 = request.form.get('stock_3')
        stock_4 = request.form.get('stock_4')
        stock_5 = request.form.get('stock_5')

        form_data = {
            'email': email,
            'firstName': first_name,
            'lastName': last_name,
            'password1': password1,
            'password2': password2,
            'stock_1': stock_1,
            'stock_2': stock_2,
            'stock_3': stock_3,
            'stock_4': stock_4,
            'stock_5': stock_5
        }

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif not stock_1 or not stock_2 or not stock_3:
            flash('Please enter at least 3 stocks.', category='error')
        else:
            user_stock_list = [stock_1, stock_2, stock_3, stock_4, stock_5]
            user_final_stock_list = []
            for stock in user_stock_list:
                if stock:
                    stock = stock.strip().upper()
                    if stock in user_final_stock_list:
                        flash('Duplicate stock symbol: ' + stock + '. Please remove the duplicate.', category='error')
                        return render_template("sign_up.html", user=current_user, form_data=form_data)
                    user_final_stock_list.append(stock)
            invalid_stocks = [stock for stock in user_final_stock_list if stock not in total_stock_list]
            if invalid_stocks:
                flash(
                    'Invalid ticker symbols: ' + ', '.join(invalid_stocks) + '. Please check the provided list again.',
                    category='error')
            else:
                new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(
                    password1, method='sha256'))
                new_user.stock_1 = stock_1
                new_user.stock_2 = stock_2
                new_user.stock_3 = stock_3
                new_user.stock_4 = stock_4
                new_user.stock_5 = stock_5
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user, form_data=form_data)


@auth.route('/settings', methods=['GET', 'POST'])
@login_required
def edit_password():
    if request.method == 'POST':
        current_password = request.form.get('currentPassword')
        new_password1 = request.form.get('newPassword1')
        new_password2 = request.form.get('newPassword2')

        if not check_password_hash(current_user.password, current_password):
            flash('Incorrect current password.', category='error')
        elif new_password1 != new_password2:
            flash('New passwords do not match.', category='error')
        elif len(new_password1) < 7:
            flash('New password must be at least 7 characters.', category='error')
        else:
            current_user.password = generate_password_hash(new_password1, method='sha256')
            db.session.commit()
            flash('Password updated successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template("settings.html", user=current_user)

@auth.route('/edit_stock', methods=['GET', 'POST'])
@login_required
def edit_stock():
    if request.method == 'POST':
        user = current_user
        stock_1 = request.form.get('stock_1')
        stock_2 = request.form.get('stock_2')
        stock_3 = request.form.get('stock_3')
        stock_4 = request.form.get('stock_4')
        stock_5 = request.form.get('stock_5')
        user.percentage_difference_limit = float(request.form.get('percentage_difference_limit'))  # Add this line

        user_stock_list = [stock_1, stock_2, stock_3, stock_4, stock_5]
        user_final_stock_list = []
        invalid_stocks = []

        for stock in user_stock_list:
            if stock:
                stock = stock.strip().upper()
                if stock in user_final_stock_list:
                    flash('Duplicate stock symbol: ' + stock + '. Please remove the duplicate.', category='error')
                    return redirect(url_for('auth.edit_stock'))
                user_final_stock_list.append(stock)
                if stock not in total_stock_list:
                    invalid_stocks.append(stock)

        if invalid_stocks:
            flash('Invalid ticker symbols: ' + ', '.join(invalid_stocks) + '. Please check the provided list again.', category='error')
        else:
            user.stock_1 = stock_1
            user.stock_2 = stock_2
            user.stock_3 = stock_3
            user.stock_4 = stock_4
            user.stock_5 = stock_5
            db.session.commit()
            flash('Stock updated successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template('stock_settings.html', user=current_user)


