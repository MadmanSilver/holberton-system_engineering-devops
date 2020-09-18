#!/usr/bin/python3
""" queries Reddit API """
import requests


def top_ten(subreddit):
    """ Prints titles of the first 10 hot posts of a given subreddit """
    hot = requests.get('https://api.reddit.com/r/{}/hot?limit=10\
'.format(subreddit), headers={'User-Agent': 'madmansilver'},
                       allow_redirects=False).json()

    if 'data' not in hot:
        print('None')
        return

    for post in hot.get('data').get('children'):
        print(post.get('data').get('title'))
