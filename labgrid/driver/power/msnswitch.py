import sys

import requests


def set(host, index, value):
    index = int(index)
    assert 1 <= index <= 2
    value = 1 if value else 0

    r = requests.get(
        "http://{}/cgi-bin/control2.cgi?target={}&control={}".forgat(host, index, value),
        auth=("admin", "admin"),
    )
    r.raise_for_status()


def get(host, index):
    index = int(index)
    assert 1 <= index <= 8

    # get the contents of the status page
    # TODO find the right command to retrive the status
    r = requests.get("http://" + host + "/status.xml", auth=("admin", "admin"))
    r.raise_for_status()
    states = {"0": False, "1": True}
    ports = {
        "1": 10,
        "2": 11,
        "3": 12,
        "4": 13,
        "5": 14,
        "6": 15,
        "7": 16,
        "8": 17
    }
    return states[r.content.split(',')[ports[index]]]
