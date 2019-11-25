from flask import Flask, redirect, json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/')
def index():
    url = get_random_url()
    return redirect(url)


def get_random_url() -> str:
    return "https://shodan.io/"


@app.errorhandler(HTTPException)
def handle_exception(e):
    """ Prints poop in case of error """
    return "<h1>💩</h1>"


if __name__ == '__main__':
    app.run()

