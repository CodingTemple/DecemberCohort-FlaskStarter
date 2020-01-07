from avengersphone import app
from flask import render_template

@app.route("/") # Home Route
def home():
    return render_template("home.html")
