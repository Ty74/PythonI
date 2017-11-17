from flask import Flask, render_template,request, redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def getUsers():
    print "In get Users information" 
    return render_template('results.html',name=request.form['name'],schoolLocation=request.form['schoolLocation'],favLanguage=request.form['favLanguage'],comments= request.form['comments'])
    


app.run(debug=True)
