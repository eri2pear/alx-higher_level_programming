#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status
    using package 'requests'
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\tt- content: {}".format(r:))
