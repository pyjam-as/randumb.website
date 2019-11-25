from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    url = get_random_url()
    return redirect(url)


def get_random_url() -> str:
    return "https://shodan.io/"


@app.errorhandler(Exception)
def handle_exception(e):
    """ Prints poop in case of error """
    return "<h1>💩</h1>"


if __name__ == '__main__':
    app.run()

