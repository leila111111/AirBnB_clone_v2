#!/usr/bin/python3
"""script that starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value
of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space )"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """result 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """result 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """display “C ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f'C {text}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
