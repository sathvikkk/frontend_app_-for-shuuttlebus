from flask import Flask, render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'S@thvikkk2022'
app.config['MYSQL_DB'] = 'shuttlebus'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('add.html')
 
@app.route('/add', methods = ['POST', 'GET'])
def add():
    if request.method == 'GET':
        return "add Passenger details"
     
    if request.method == 'POST':
        passengername = request.form['passengername']
        phonenumber = request.form['phonenumber']
        cityname = request.form['cityname']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO passengersinfo VALUES(%s,%s,%s)''',(passengername,phonenumber,cityname))
        mysql.connection.commit()
        cursor.close()
        return "passenger details added."
 
app.run(host='0.0.0.0', port=5000)