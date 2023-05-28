<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
</p><em>Contributors: Sviatlana Karaliova, Jana Schaeffer, Nazgul Tobler, Poppy Bütikofer-McLaughlin, Alicia de Mora Losana Gago.</em></p>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Stock-News-Monitoring-Program/stock_news">
    <img src="app_logo.png" alt="Logo" height="130">
  </a>

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
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* ![Plotly](https://img.shields.io/badge/-%20Plotly-orange)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Features
* User Registration: Users can create an account by providing their email, first name, last name, and password. Passwords are securely hashed and stored in the database. They are also required to enter at least three stock symbols.
* User Login: Registered users can log in to their accounts using their email and password.
* Stock Dashboard: After logging in, users are presented with a dashboard that displays stock information and related news articles. The stock information is fetched from the Alpha Vantage API and includes the symbol, current price, previous price, percentage difference, and price direction (whether the price has gone up or down). The news articles are fetched from an API based on the user's stock preferences.
* Stock Preferences: Users can customize their stock preferences by adding or modifying the stock symbols they are interested in. They can edit their preferences from the dashboard or the settings page.
* Password Update: Users can change their account password by providing their current password and entering a new password.
* Logout: Users can log out from their account, which redirects them to the login page.

### File structure
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

The application requires the following dependencies which can be installed from the requirements.txt (see Installation):

* Flask: A micro web framework used for building the web application.
* Flask-Login: A Flask extension that handles user authentication and session management.
* Flask-WTF: A Flask extension that simplifies the handling of forms.
* SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library used for database operations.
* PyMySQL: A MySQL client library used for connecting to the MySQL database.
* SendGrid: A library for sending emails, used for password reset functionality.
* Requests: A library for making HTTP requests, used for fetching data from external APIs.
* Werkzeug: A library used for password hashing and verification.

### Installation

1. TO CHANGE!!!! Get a free API Key at [https://example.com](https://example.com) ********
2. Ensure that Python 3.x is installed on your system
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
## Roadmap

- [ ] Feature 1: Ensuring scalability by deploying the application and moving the database to the cloud.
- [ ] Feature 2:
- [ ] Feature 3:

<p align="right">(<a href="#readme-top">back to top</a>)</p>

