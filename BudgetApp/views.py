from BudgetApp import budget
from datetime import datetime

from flask import Flask, render_template

from . import app
from . import budget

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/retirement/")
def retirement():
    data=budget.budgetData()
    labels=budget.budgetLabels() 
    return render_template(
        "retirement.html",
        data = data,
        labels= labels
    )

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
