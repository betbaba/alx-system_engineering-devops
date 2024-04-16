#!/usr/bin/python3
""" queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
"""
import requests
import re


def count_words(subreddit, word_list, after=None, word_count={}):
    headers = "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()['data']
    for post in data['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            regex = r'\b{}\b'.format(word.lower())
            count = len(re.findall(regex, title))
            if count > 0:
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += count
    if data['after']:
        count_words(subreddit, word_list, data['after'], word_count)
    else:
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f'{word}: {count}')
