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

@app.route("/assignments")
def assignments():
    return render_template("Assignments.html")

@app.route("/classes")
def classes():
    return render_template("Classes.html")

@app.route("/1006")
def test1():
    return "<p> 1006 homepage </p>"

#start the server
if __name__ == "__main__":
    app.run()
    
    