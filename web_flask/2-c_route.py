#!/usr/bin/python3
"""
Script that starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display "HBNB"
/c/<text>: display “C ” followed by the value of the text variable
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    text.replace("_", " ")
    return "C {}".format(escape(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
