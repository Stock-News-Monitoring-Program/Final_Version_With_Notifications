import pymysql
from website import create_app

pymysql.install_as_MySQLdb()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

