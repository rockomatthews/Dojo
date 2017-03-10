from flask import Flask, render_template, redirect, session, flash, request
import random

app = Flask(__name__)
app.secret_key = 'idontno'

def lucky_Start():
    session['lucky_number'] = random.randrange(0, 101)

@app.route('/')
def index():
    session['button_status'] = "submit"
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def processIt():
    
    print session['lucky_number']
    user_guess = int(request.form['number_guess'])
    while user_guess != session['lucky_number']:
        if (user_guess > session['lucky_number']):
            session['string'] = "Wrong! You guessed high. So sorry buddy"
            return redirect('/')
        elif (user_guess < session['lucky_number']):
            session['string'] = "Wrong! You guessed low. so so sorry buddy."
            return redirect('/')
    session['string'] = "YOU. GOT. It. and do you want to play again?"
    session['button_status'] = "TRY AGAIN"
    session.pop('lucky_number')
    session['lucky_number'] = random.randrange(0, 101)
    return render_template('index.html')

            

app.run(debug=True)