import os
import random
import string

import requests


SHODAN_KEY = os.getenv("SHODAN_KEY")
HOST_QUEUE = []


def _fill_queue():
    url = "https://api.shodan.io/shodan/host/search"
    query = f"HTTP {random.choice(string.ascii_letters)}"
    r = requests.get(url, params={"query": query, "key": SHODAN_KEY})
    for match in r.json()["matches"]:
        if match['port'] == 80 and match['data'].startswith("HTTP"):
            HOST_QUEUE.append(match["http"]["host"])
    if len(HOST_QUEUE) == 0:
        _fill_queue()


def get_host():
    if len(HOST_QUEUE) == 0:
        _fill_queue()
    return HOST_QUEUE.pop()
