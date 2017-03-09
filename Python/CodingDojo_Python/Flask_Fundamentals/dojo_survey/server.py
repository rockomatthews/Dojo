from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/process', methods=['POST'])
def pros():
  print "------------------------------------"
  print "churning"
  print "------------------------------------"

  answer_name = request.form['html_name']
  answer_location = request.form['html_location']
  answer_favorite_language = request.form['html_f_language']
  answer_comments = request.form['html_comments']
  return render_template('results.html', answer_name = answer_name, answer_location = answer_location, answer_favorite_language = answer_favorite_language, answer_comments = answer_comments)

app.run(debug=True)