import unittest

from unittest.mock import patch, MagicMock


from website.views import fetch_stock_data, fetch_news_data, send_notification_email, fetch_news_for_messaging, send_message


class TestYourModule(unittest.TestCase):

    @patch('website.views.requests.get')
    def test_fetch_stock_data(self, mock_get):
        # Set up mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'Time Series (Daily)': {
                '2023-05-27': {
                    '4. close': '100.0'
                },
                '2023-05-26': {
                    '4. close': '95.0'
                }
            }
        }
        mock_get.return_value = mock_response

        # Setting up test data
        user = MagicMock()
        user.stock_1 = 'AAPL'
        user.percentage_difference_limit = 5.0

        # Calling the function to test
        stock_data = fetch_stock_data(user)

        # Asserting the expected results
        self.assertEqual(len(stock_data), 1)
        self.assertEqual(stock_data[0]['symbol'], 'AAPL')
        self.assertEqual(stock_data[0]['first_price'], 100.0)
        self.assertEqual(stock_data[0]['second_price'], 95.0)
        self.assertEqual(stock_data[0]['percentage_difference'], 5.26)
        self.assertEqual(stock_data[0]['price_direction'], '🔺')
        self.assertEqual(stock_data[0]['difference'], 5.0)

    @patch('website.views.requests.get')
    def test_fetch_news_data(self, mock_get):
        # Set up mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'articles': [
                {
                    'title': 'Why AAPL Stock Is Low-Hanging Fruit on Any Weakness',
                    'description': "InvestorPlace - Stock Market News, Stock Advice & Trading Tips If you own AAPL stock today, there's no need to make a hasty exit. If you currently do not own it, feel free to buy at current prices, but consider pouncing on it following any weakness. The post …",
                    'url': 'https://biztoc.com/x/9150ce1c95581a86'
                },
                {
                    'title': 'Here’s Why Apple (AAPL) Outperformed in Q1',
                    'description': 'Fred Alger Management, an investment management company, released its “Alger Spectra Fund” first quarter 2023 investor letter. A copy of the same can be...',
                    'url': 'https://finance.yahoo.com/news/why-apple-aapl-outperformed-q1-102958851.html'
                },
                {
                    'title': 'Apple (AAPL) Relentless Stock Price Rally Puts $3 Trillion in View - Bloomberg',
                    'description': 'Apple (AAPL) Relentless Stock Price Rally Puts $3 Trillion in View  Bloomberg',
                    'url': 'https://consent.google.com/ml?continue=https://news.google.com/rss/articles/CBMibmh0dHBzOi8vd3d3LmJsb29tYmVyZy5jb20vbmV3cy9hcnRpY2xlcy8yMDIzLTA1LTIyL2FwcGxlLXMtcmVsZW50bGVzcy1yYWxseS1wdXRzLTMtdHJpbGxpb24taW4tdmlldy10ZWNoLXdhdGNo0gEA?oc%3D5&gl=FR&hl=en-US&cm=2&pc=n&src=1'
                }
            ]
        }
        mock_get.return_value = mock_response

        # Setting up test data
        companies = ['AAPL']

        # Calling the function to test
        news_data = fetch_news_data(companies)

        # Asserting the expected results
        self.assertEqual(len(news_data), 3)

    @patch('website.views.SendGridAPIClient')
    def test_send_notification_email(self, mock_client):
        # Set up test data
        user = MagicMock()
        user.email = 'airy-fairy6@yandex.ru'
        company = 'AAPL'
        percentage_difference = 2.0

        # Calling the function to test
        send_notification_email(user, company, percentage_difference)

        # Asserting the expected behavior
        mock_client.return_value.send.assert_called_once()

    @patch('website.views.requests.get')
    def test_fetch_news_for_messaging(self, mock_get):
        # Setting up mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'articles': [
                {
                    'title': 'Why AAPL Stock Is Low-Hanging Fruit on Any Weakness',
                    'description': "InvestorPlace - Stock Market News, Stock Advice & Trading Tips If you own AAPL stock today, there's no need to make a hasty exit. If you currently do not own it, feel free to buy at current prices, but consider pouncing on it following any weakness. The post …",
                    'url': 'https://biztoc.com/x/9150ce1c95581a86'
                },
                {
                    'title': 'Here’s Why Apple (AAPL) Outperformed in Q1',
                    'description': 'Fred Alger Management, an investment management company, released its “Alger Spectra Fund” first quarter 2023 investor letter. A copy of the same can be...',
                    'url': 'https://finance.yahoo.com/news/why-apple-aapl-outperformed-q1-102958851.html'
                },
                {
                    'title': 'Apple (AAPL) Relentless Stock Price Rally Puts $3 Trillion in View - Bloomberg',
                    'description': 'Apple (AAPL) Relentless Stock Price Rally Puts $3 Trillion in View  Bloomberg',
                    'url': 'https://consent.google.com/ml?continue=https://news.google.com/rss/articles/CBMibmh0dHBzOi8vd3d3LmJsb29tYmVyZy5jb20vbmV3cy9hcnRpY2xlcy8yMDIzLTA1LTIyL2FwcGxlLXMtcmVsZW50bGVzcy1yYWxseS1wdXRzLTMtdHJpbGxpb24taW4tdmlldy10ZWNoLXdhdGNo0gEA?oc%3D5&gl=FR&hl=en-US&cm=2&pc=n&src=1'
                }
            ]
        }
        mock_get.return_value = mock_response

        # Setting up test data
        companies = ['AAPL']

        # Calling the function to test
        news_body = fetch_news_for_messaging(companies)

        # Assertting the expected results
        expected_result = "AAPL: \nHeadline: Why AAPL Stock Is Low-Hanging Fruit on Any Weakness. \nBrief: InvestorPlace - Stock Market News, Stock Advice & Trading Tips If you own AAPL stock today, there's no need to make a hasty exit. If you currently do not own it, feel free to buy at current prices, but consider pouncing on it following any weakness. The post … \nSource: https://biztoc.com/x/9150ce1c95581a86\n" \
                          'AAPL: \nHeadline: Here’s Why Apple (AAPL) Outperformed in Q1. \nBrief: Fred Alger Management, an investment management company, released its “Alger Spectra Fund” first quarter 2023 investor letter. A copy of the same can be... \nSource: https://finance.yahoo.com/news/why-apple-aapl-outperformed-q1-102958851.html\n' \
                          'AAPL: \nHeadline: Apple (AAPL) Relentless Stock Price Rally Puts $3 Trillion in View - Bloomberg. \nBrief: Apple (AAPL) Relentless Stock Price Rally Puts $3 Trillion in View  Bloomberg \nSource: https://consent.google.com/ml?continue=https://news.google.com/rss/articles/CBMibmh0dHBzOi8vd3d3LmJsb29tYmVyZy5jb20vbmV3cy9hcnRpY2xlcy8yMDIzLTA1LTIyL2FwcGxlLXMtcmVsZW50bGVzcy1yYWxseS1wdXRzLTMtdHJpbGxpb24taW4tdmlldy10ZWNoLXdhdGNo0gEA?oc%3D5&gl=FR&hl=en-US&cm=2&pc=n&src=1'
        self.assertEqual(news_body, expected_result)

    @patch('website.views.SendGridAPIClient')
    def test_send_message(self, mock_client):
        # Setting up test data
        user = MagicMock()
        user.email = 'airy-fairy6@yandex.ru'
        company = 'AAPL'

        # Calling the function to test
        response = send_message(user, company)

        # Asserting the expected behavior
        mock_client.return_value.send.assert_called_once()
        self.assertEqual(response.status_code, mock_client.return_value.send.return_value.status_code)


if __name__ == '__main__':
    unittest.main()
