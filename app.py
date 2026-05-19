from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@1911",
    database="gymdb"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_member():

    name = request.form['name']
    age = request.form['age']
    phone = request.form['phone']

    sql = "INSERT INTO members(name, age, phone) VALUES(%s, %s, %s)"
    values = (name, age, phone)

    cursor.execute(sql, values)
    db.commit()

    return "Registration Successful"


if __name__ == '__main__':
    app.run(debug=True)
    