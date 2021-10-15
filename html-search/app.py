from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
import os
import datetime

app = Flask(__name__)

# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = os.environ.get("MYSQL_DATABASE_USER")
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get("MYSQL_DATABASE_PASSWORD")
app.config['MYSQL_DATABASE_DB'] = os.environ.get("MYSQL_DATABASE_DB")
app.config['MYSQL_DATABASE_HOST'] = os.environ.get("MYSQL_DATABASE_HOST")

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        name = request.form['name']
        # search by employee firstname or lastname
        cursor.execute("SELECT emp_id, firstname, lastname, date_birth, occupation, gender\
         from Employee WHERE firstname LIKE %s OR lastname LIKE %s", (name, name))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the employee
        if len(data) == 0 and name == 'all':
            cursor.execute("SELECT emp_id, firstname, lastname, date_birth, occupation, gender from Employee")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    # default search will show all employee
    if request.method == "GET":
        cursor.execute("SELECT emp_id, firstname, lastname, date_birth, occupation, gender from Employee")
        conn.commit()
        data = cursor.fetchall()
        return render_template('search.html', data=data)

# end point for inserting data dynamicaly in the database
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob = request.form['Date of Birth']
        occupation = request.form['occupation']
        gender = request.form['gender']
        format = '%d/%m/%Y'
        # convert from string format to datetime format
        date = datetime.datetime.strptime(dob, format)
        cursor.execute("INSERT INTO Employee (firstname, lastname, date_birth, occupation, gender) \
        Values (%s, %s, %s, %s, %s)", (firstname, lastname, date, occupation, gender))
        conn.commit()
    return render_template('insert.html')

@app.route("/")
def main():
    return "Hello world from Flask!"
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
