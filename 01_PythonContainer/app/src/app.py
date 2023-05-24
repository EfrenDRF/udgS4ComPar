"""
    File_name:  app.py
    Author:     Efren Del Real Frias
    Date:       May 23th 2023
    Reference:  https://flask.palletsprojects.com/en/2.3.x/quickstart/#html-escaping
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello :), World!</p>"