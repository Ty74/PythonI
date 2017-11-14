from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html", cookies="Chocolate Chips", quantity=5)
app.run(debug=True)
