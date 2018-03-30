import sys
import re

import requests


def set(host, index, value):
    index = int(index)
    assert 1 <= index <= 8
    value = 'ON' if value else 'OFF'

    r = requests.get(
        "http://{}/outlet?{}={}".format(host, index, value),
        auth=("admin", "1234"),
    )
    r.raise_for_status()


def get(host, index):
    index = int(index)
    assert 1 <= index <= 8

    # get the contents of the status page
    r = requests.get("http://" + host + "/status", auth=("admin", "1234"))
    r.raise_for_status()
    match_list = re.findall('<div id="(\w+)">([0-9a-f]+)</div>', r.content.text)
    if match_list:
        match_dict = dict(match_list)
        try:
	    # The state of each outlet is encoded as a bit in the map
	    # If the outlet is off, the bit is zero
	    # If the outlet is on, the bit is one
            state_map = int(match_dict['state'], 16)
            return True if (state_map & (1 << (index - 1))) else False
        except KeyError:
            pass

