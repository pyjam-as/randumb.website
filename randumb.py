
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    url = get_random_url()
    return redirect(url)


def get_random_url() -> str:
    return "https://shodan.io/"


if __name__ == '__main__':
    app.run()
