#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This method displays a string, Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This method displays a string, HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """This method displays c followed by some text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text="is cool"):
    """This method displays python followed by some text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """This method displays only integers"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
