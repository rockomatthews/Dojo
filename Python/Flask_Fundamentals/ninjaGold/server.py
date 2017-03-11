from flask import Flask, render_template, redirect, session, flash, request
import random

app = Flask(__name__)
app.secret_key = 'idontno'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['status'] = "The ninja has gone nowhere so far."
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.form['select_it'] == 'Farm':   
        session['amount'] = random.randrange(10, 21) 
        session['gold'] += session['amount']
        session['status'] += " You got the ninja " + str(session['amount']) + " pieces of gold."
        return redirect('/')
    elif request.form['select_it'] == 'Cave':   
        session['amount'] = random.randrange(5, 11)
        session['gold'] += session['amount']
        session['status'] += " You got the ninja " + str(session['amount']) + " pieces of gold."
        return redirect('/')
    elif request.form['select_it'] == 'House':   
        session['amount'] = random.randrange(2, 5)
        session['gold'] += session['amount']
        session['status'] += " The ninja commit a B&E and stole " + str(session['amount']) + " pieces of gold... killing " + str(random.randrange(1, 11)) + " in the process."
        return redirect('/')
    elif request.form['select_it'] == 'Casino':   
        session['amount'] = random.randrange(0, 51)
        session['gold'] += session['amount']
        session['status'] += " You got the ninja " + str(session['amount']) + " pieces of gold."
        return redirect('/')
    
    return render_template('index.html')
    
@app.route('/reset', methods=["POST"])    
def reset():
    if request.form['reset_it'] == 'zero_it':
        session.pop('gold')
        session.pop('status')
        return redirect('/')

app.run(debug=True)
