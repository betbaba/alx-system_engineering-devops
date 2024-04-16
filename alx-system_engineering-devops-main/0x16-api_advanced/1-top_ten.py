#!/usr/bin/python3
""" that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """ a functon that queres the reddit """

    url = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
