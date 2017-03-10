from flask import Flask, render_template, redirect, session, flash, request

app = Flask(__name__)
app.secret_key = "this is the secret_key!"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/cali')
def california():
    if "trip_history" in session:
        history=session['trip_history']
        history.insert(0, 'visited California')
        session['trip_history']=history
    return render_template('california.html')

@app.route('/indi')
def indiana():
    if "trip_history" in session:
        history=session['trip_history']
        history.insert(0, 'visited Indiana')
        session['trip_history']=history
    return render_template('indiana.html')

@app.route('/new_york')
def new_york():
    if "trip_history" in session:
        history=session['trip_history']
        history.insert(0, 'visited New York')
        session['trip_history']=history
    return render_template('new_york.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def auth():
    print "------------------------------------"
    print "authenticating user"
    print "------------------------------------"

    server_email = request.form['html_email']
    server_password = request.form['html_password']
    if server_email == "rob@matthews.com" and server_password == "asdfasdf":
        session['trip_history']= []
        session['user_name'] = 'Some User'
        session['email'] = 'server_email'
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



app.run(debug=True) 