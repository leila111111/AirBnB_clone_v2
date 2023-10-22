#!/usr/bin/python3
"""script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states_list = storage.all(State)
    return render_template("7-states_list.html", states_list=states_list)


@app.teardown_appcontext
def teardown_app(exc):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
