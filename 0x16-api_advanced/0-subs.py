#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {'User-agent': 'ad-egg'}
    r = requests.get(url, headers=h, allow_redirects=False)

    if r.status_code == 200:
        req = r.json()
        info = req.get('data')
        subscribers = info.get('subscribers')
        if info is not None and subscribers is not None:
            return subscribers
    return 0