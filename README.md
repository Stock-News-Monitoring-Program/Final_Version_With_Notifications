</p><em>Contributors: Sviatlana Karaliova, Jana Schaeffer, Nazgul Tobler, Poppy Bütikofer-McLaughlin, Alicia de Mora Losana Gago.</em></p>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Stock-News-Monitoring-Program/stock_news">
    <img src="https://cdn.pixabay.com/photo/2020/05/21/22/23/logo-5203035_1280.png" alt="Logo" height="130">
  </a>
  <h1><em>stocktrack.io<em/></h1>
  <p align="center">
    Welcome to a simplified way of tracking stock information.
    <br />
    <a href="https://github.com/Stock-News-Monitoring-Program/stock_news"><strong>Click here to access the repo.»</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Technology Stack Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

We have built a Flask-based web application that allows registered users to track pricing information about their selected stocks, as well as to stay up-to-date with the financial news most relevant to those tracked stocks through integration with external APIs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Technology Stack Used
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
* ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
* ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
* ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
* ![Plotly](https://img.shields.io/badge/-%20Plotly-orange)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Main Features
* User Registration: Users can create an account by providing their email, first name, last name, and password. Passwords are securely hashed and stored in a MySQL database. Users are also required to enter at least three ticker symbols (i.e. stock identifiers) of those stocks they would like to track.
* User Login: Registered users can log in to their accounts using their email and password for their tracked stocks to display on their stock dashboard.
* User Logout: Users can log out from their account, which redirects the user to the login page.
* 'Remember Me' (for Registered Users): Registered users do not need to log in as they will remain logged in for easy access unless they have previously logged out.
* Stock Dashboard: After logging in, users are presented with a dashboard that displays their selected stocks' pricing data as well as most relevant news articles. Pricing information is fetched using the Alpha Vantage API and includes a visual representation of daily closing prices from the beginning of the year (2023) identified with the stock's the ticker symbol, the stock's latest closing price (yesterday's price) in USD, the stock's day-before-yesterday's closing price in USD, the percentage difference between the two, and the direction of the price change (i.e. whether the price has gone up or down). The news articles are fetched from an API based on the user's stock preferences.
* Stock Selection: Users can ammend their stock preferences in the 'Stock Selection' page.
* Personal Information Management: Users can ammend their personal details (including their password) in the 'My Account' page.
* Notifications and Alerts: Users are notified via email (using Sendgrid) if their tracked stocks

### File Structure
* auth.py: This file contains the authentication-related routes, including user registration, login, logout, and password update.
* models.py: This file defines the database models used by the application. It includes the User model, which represents the user accounts and their associated fields.
* views.py: This file contains the main routes and logic for rendering the dashboard, fetching stock data and news articles, and handling user actions.
* config.py: This file stores the configuration variables for the application, such as database credentials.
* total_stock_list.py: This file contains a list of valid stock symbols used for validation purposes.
* templates/: This directory contains the HTML templates used for rendering the web pages. Including the base, home, settings, sign_up and stcok_setting HTML Files. 


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

The application requires the following dependencies (amongst others) which can be installed from the requirements.txt (see Installation below):


* Flask: A micro web framework used for building the web application.
* Flask-Login: A Flask extension that handles user authentication and session management.
* Flask-WTF: A Flask extension that simplifies the handling of forms.
* SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library used for database operations.
* PyMySQL: A MySQL client library used for connecting to the MySQL database.
* SendGrid: A library for sending emails, used for password reset functionality.
* Requests: A library for making HTTP requests, used for fetching data from external APIs.
* Werkzeug: A library used for password hashing and verification.

### Installation UPDAAAAAATE THIS PART

1. Get a free API Key for Alpha Vantage, News API, SendGrid at [https://www.alphavantage.co/](https://www.alphavantage.co/), [https://newsapi.org](https://newsapi.org/) and [https://www.twilio.com/en-us](https://www.twilio.com/en-us), respectively.

2. Ensure that Python 3.x is installed on your system.
3. Clone the repo
   ```sh
   git clone https://github.com/Stock-News-Monitoring-Program/*************.git
   ```
4. Navigate to the project directory **********
    ```sh
    cd REPOSITORYNAME
    ```
5. Create a virtual environment to isolate the project's dependencies
    ```sh
    python3 -m venv venv
    ```
6. Activate the virtual environment
    ```sh
    venv\Scripts\activate
    ```
7. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
8. Ensure that you have a MySQL database set up and running
   * Create a database called 'stock'
9. Configure the application
   Within the config.py, ensure the following variables match your database credentials
    * HOST
    * PORT
    * USER
    * PASSWORD
    * DATABASE
   
10. Enter your API in `views.py`
11. Initialise the database
    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
12. Start the application
    ```sh
    flask run
    ``` 
13. Open your web browser and visit http://localhost:5000 to access the application. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<a href="https://scribehow.com/embed/Workflow__qVAlhm1uSri_yBlJijAXIw?as=scrollable&skipIntro=true" target="_blank">Link to Website Workflow</a>



_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap & Next Steps

- [ ] Ensuring scalability by deploying the application and moving the database to the cloud.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

