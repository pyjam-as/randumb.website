# deps
from flask import Flask, redirect
from loguru import logger

# app
import shodan

app = Flask(__name__)


@app.route('/')
def index():
    host = shodan.get_host()
    url = f"http://{host}/"
    return redirect(url)


@app.errorhandler(Exception)
def handle_exception(e):
    """ Prints poop in case of error """
    logger.error(f"Error: {e}")
    return "<h1>💩</h1>"


if __name__ == '__main__':
    app.run()
