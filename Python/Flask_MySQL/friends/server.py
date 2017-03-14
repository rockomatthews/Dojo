from flask import Flask , request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/friends', methods=['POST'])
def add_friend():
    
    return redirect('/')

app.run(debug=True)