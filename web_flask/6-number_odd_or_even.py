#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """This method displays a HTML page only for integers"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_or_even(n):
    """
    This method displays a HTML page and
    shows if the number is odd or even
    """
    return render_template('6-number_odd_or_even.html', number=n, parity=('even' if n % 2 == 0 else 'odd'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
