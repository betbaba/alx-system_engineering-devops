#!/usr/bin/python3
"""  queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns total number of subscribers """
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
