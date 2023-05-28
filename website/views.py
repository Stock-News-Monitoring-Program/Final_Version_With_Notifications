from datetime import time

import requests
import schedule
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from sendgrid import SendGridAPIClient, Mail

from . import db
from .auth import auth
from .models import User

views = Blueprint('views', __name__)

# API keys
STOCK_API_KEY = "W5MCUSXL1KQ6Q7ZN"
NEWS_API_KEY = "e4957b61ade34fd6b6ef8dc58065022c"
sortBy = "publishedAT"
language = "en"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?q"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

views.register_blueprint(auth)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        company1 = request.form.get('stock_1')
        company2 = request.form.get('stock_2')
        company3 = request.form.get('stock_3')
        company4 = request.form.get('stock_4')
        company5 = request.form.get('stock_5')

        # Save stock names in the database
        user = User.query.get(current_user.id)
        user.stock_1 = company1
        user.stock_2 = company2
        user.stock_3 = company3
        user.stock_4 = company4
        user.stock_5 = company5
        db.session.commit()

        # Fetch stock data
        stock_data = fetch_stock_data(user)
        # Fetch news data
        news_data = fetch_news_data([company1, company2, company3, company4, company5])

        return render_template('home.html', stock_data=stock_data, news_data=news_data, user=current_user)

    # Fetch stock data
    user = User.query.get(current_user.user_id)
    stock_data = fetch_stock_data(user)
    # Fetch news data
    news_data = fetch_news_data([user.stock_1, user.stock_2, user.stock_3, user.stock_4, user.stock_5])

    return render_template('home.html', stock_data=stock_data, news_data=news_data, user=current_user)


def fetch_stock_data(user):
    stock_data = []
   
    companies = [
        user.stock_1,
        user.stock_2,
        user.stock_3,
        user.stock_4,
        user.stock_5,
    ]


    for company in companies:
        if company:
            params = {
                "function": "TIME_SERIES_DAILY_ADJUSTED",
                "symbol": company,
                "apikey": STOCK_API_KEY
            }
            response = requests.get("https://www.alphavantage.co/query", params=params)

            try:
                data = response.json()
            except ValueError:
                # If response is not valid JSON, skip this company and continue to the next one
                continue
            if 'Time Series (Daily)' in data:
                # Retrieve the first price
                time_series = data['Time Series (Daily)']

                data_list = [value for (key, value) in time_series.items()]
                first_data = data_list[0]
                first_price = float(first_data["4. close"])
                second_data = data_list[1]
                second_price = float(second_data["4. close"])

                # Calculate the percentage difference
                difference = float(first_price) - float(second_price)
                percentage_difference = round(((difference / float(first_price)) * 100), 2)

                # Notification for limit in price percentage  difference
                if abs(percentage_difference) > user.percentage_difference_limit:
                    send_notification_email(user, company, percentage_difference)
                    send_message(user, company)

                # Determine if the price has gone up or down
                if difference > 0:
                    sign = "🔺"
                else:
                    sign = "🔻"
                price_direction = sign


                stock_data.append({
                    'symbol': company,
                    'first_price': first_price,
                    'second_price': second_price,
                    'percentage_difference': percentage_difference,
                    'price_direction': price_direction,
                    'difference': difference,
                    'data': data['Time Series (Daily)']
                })

    return stock_data


def fetch_news_data(companies):
    news_data = []

    for company in companies:
        news_parameters = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": company,
            "sortBy": sortBy,
            "language": language,
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
        news_json = news_response.json()

        if "articles" in news_json:
            articles = news_json["articles"]

            three_articles = articles[:3]

            company_articles = []
            for article in three_articles:
                article_info = {
                    'company': company,
                    'headline': article['title'],
                    'brief': article['description'],
                    'source': article['url']
                }
                company_articles.append(article_info)

            news_data.extend(company_articles)

    return news_data

# Send the email  using SendGrid API for price changes
def send_notification_email(user, company, percentage_difference):

    message = Mail(
        from_email='NewsStockMonitoring4@gmail.com',
        to_emails=user.email,
        subject=f'{company} Stock Alert',
        plain_text_content=f'The stock price for {company} has changed by {percentage_difference:.2f}%.'
    )

    # Send the email using SendGrid API
    try:
        sendgrid_client = SendGridAPIClient('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')
        sendgrid_client.send(message)
    except Exception as e:
        print(str(e))

# Retrieving news data for sending the email using SendGrid API
def fetch_news_for_messaging(companies):
    text = []

    for company in companies:
        news_parameters = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": company,
            "sortBy": sortBy,
            "language": language,
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
        articles = news_response.json()["articles"]
        three_articles = articles[:3]
        list_articles = [
            f"{company}: \nHeadline: {article['title']}. \nBrief: {article['description']}. "
            f"\nSource: {article['url']}"
            for article in three_articles]
        text_version = "\n".join(list_articles)
        text.append(text_version)
        news_body = "\n".join(text)
    return news_body

# Send the email with news using SendGrid API
def send_message(user, company):
    message = Mail(
        from_email='NewsStockMonitoring4@gmail.com',
        to_emails=user.email,
        subject='StockAlertNews',
        html_content=fetch_news_for_messaging(company))
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    return response.status_code



