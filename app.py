# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
    return render_template("index.html")

@app.route("/1006")
def test1():
    return "<p> 1006 homepage </p>"

@app.route("/1006a")
def test2():
    return render_template("1006.html")

@app.route("/assignments")
def assignments():
    return "Assignments"

@app.route("/classes")
def classes():
    return "Classes"

#start the server
if __name__ == "__main__":
    app.run()
    
    