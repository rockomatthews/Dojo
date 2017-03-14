from flask import Flask , request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
            'first_name': request.form['html_first_name'],
            'last_name': request.form['html_last_name'],
            'occupation': request.form['html_occupation']
            }
    friends = mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('edit.html', one_friend=friends[0])

@app.route('/friends/update', methods=['POST'])
def update(friend_id):  
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :specific_id"
    data = {
            'specific_id': friend_id,
            'first_name': 'html_first_name',
            'last_name': 'html_last_name',
            'occupation': 'html_occupation'
            }
    friends = mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    friends = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)