#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status
    using package 'requests'
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
