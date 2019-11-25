import os
import random
import string
from typing import List

import requests

ENTROPY = 3
SHODAN_URL = "https://api.shodan.io/shodan/host/search"
SHODAN_KEY = os.getenv("SHODAN_KEY")
HOST_QUEUE = []


def get_host_queue() -> List[str]:
    """ Get a new queue of HTTP hosts
        by querying Shodan API """
    # choose some random chars to introduce result variance
    entropy = ''.join(ENTROPY * [random.choice(string.ascii_letters)])

    # do the shodan API request
    r = requests.get(SHODAN_URL, params={"query": f"HTTP {entropy}",
                                         "key": SHODAN_KEY})

    # filter for matches that contain "HTTP" and are on port 80
    result = [match["http"]["host"]
              for match in r.json()["matches"]
              if match["port"] == 80 and match["data"].statswith("HTTP")]

    # if no matches, recurse until match
    return result if result else get_host_queue()


def get_host():
    if not HOST_QUEUE:
        HOST_QUEUE = get_host_queue()
    return HOST_QUEUE.pop()
