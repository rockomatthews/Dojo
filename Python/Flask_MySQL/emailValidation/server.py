from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'idontno'
mysql = MySQLConnector(app, 'emailsdb')

@app.route('/')
def index():
    query = "SELECT * FROM emails"         
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails)

@app.route('/emails', methods=['POST'])
def process():
    address = request.form['email']
    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address):
        print 'test worked'
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/')
    else:
        print "test failed"
        flash('your email address is currently invalid. try over', 'error')
        return redirect('/')
    return render_template('index.html')
app.route('/emails', methods=['POST'])
def create():
    print request.form['email']
    return redirect('/')


app.run(debug=True)

