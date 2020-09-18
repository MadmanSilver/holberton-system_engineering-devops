#!/usr/bin/python3
""" queries Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers of a given subreddit """
    about = requests.get('https://api.reddit.com/r/{}/about'.format(subreddit),
                         headers={'User-Agent': 'madmansilver'},
                         allow_redirects=False).json()

    if 'data' in about:
        return about['data']['subscribers']

    return 0
