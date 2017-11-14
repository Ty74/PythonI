from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninja():
    return render_template('ninjas.html')

@app.route('/dojos/news')
def dojo():
    return render_template('/static/dojos/news/dojo.html')

app.run(debug=True)