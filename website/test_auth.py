import unittest
from flask_testing import TestCase
from flask_login import current_user
from werkzeug.security import generate_password_hash
from website.models import User
from website.auth import auth
from website.config import USER, PASSWORD, HOST
from website import create_app, db
from faker import Faker
from urllib.parse import urlparse


class AuthTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/test_stock'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.register_blueprint(auth, name='auth_blueprint')

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()

    def test_login_success(self):
        fake = Faker()
        email = fake.email()
        password = 'trial_password'
        hashed_password = generate_password_hash(password)
        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', data={'email': email, 'password': password})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')

        with self.client.session_transaction() as sess:
            self.assertEqual(sess['email'], email)
        self.assertTrue(current_user.is_authenticated)

    def test_logout(self):
        with self.client:
            fake = Faker()
            email = fake.email()
            password = 'password'

            hashed_password = generate_password_hash(password)
            user = User(email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            self.client.post('/login', data={'email': email, 'password': password})

            response = self.client.get('/logout')

            expected_redirect = '/login'

            self.assertFalse(current_user.is_authenticated)
            parsed_expected = urlparse(expected_redirect)
            parsed_actual = urlparse(response.location)

            self.assertEqual(parsed_actual.path, parsed_expected.path)


if __name__ == '__main__':
    unittest.main()
