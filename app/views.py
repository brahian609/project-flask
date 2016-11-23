# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    """ Render a la vista index del projecto """
    return render_template("index.html")

@app.route('/about')
def about():
    """ Render a la vista about del projecto """
    return render_template("about.html")
