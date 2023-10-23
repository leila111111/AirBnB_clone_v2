#!/usr/bin/python3
"""script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exc):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page: (inside the tag BODY)"""
    states_list = storage.all(State)
    amenities_list = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states_list=states_list, amenities_list=amenities_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
