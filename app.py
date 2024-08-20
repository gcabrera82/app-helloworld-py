from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db')
def db_test():
    # Conexión a MySQL
    connection = mysql.connector.connect(
        host='db',
        user='root',
        password='rootpassword',
        database='test_db'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return f'Connected to database: {db_name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)