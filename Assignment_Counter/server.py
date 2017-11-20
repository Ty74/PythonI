from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
      return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name'] =  request.form['name'],
    session['email']= request.form['email']
    
  # notice how the key we are using to access the info corresponds with the names
      # of the inputs from our html form
    return redirect('/show') # redirects back to the '/' route
@app.route("/show")
def show():
    return render_template('users.html',name=session['name'] ,email=session['email'] )

@app.route("/Counter")
def countInitialize():
      
      if "count" in session: 
        session["count"]+=2
        return render_template('Counter.html',count=session['count'])
      else:
        session["count"]=0
        session["count"]+=1
        print session["count"]
        return render_template('Counter.html',count=session['count'])
      
@app.route("/Single_Counter")
def singleSessionCount():
      if "singleCounter" in session: 
        session["singleCounter"]+=1
        return render_template('Single_Counter.html',singleCounter=session['singleCounter'])
      else:
        session["singleCounter"]=0
        session["singleCounter"]+=1
        print session["singleCounter"]
        return render_template('Single_Counter.html',singleCounter=session['singleCounter'])
      

app.run(debug=True)
