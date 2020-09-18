#!/usr/bin/python3
""" queries Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns all hot posts of a given subreddit """
    if after is None:
        hot = requests.get('https://api.reddit.com/r/{}/hot'.format(subreddit),
                           headers={'User-Agent': 'madmansilver'},
                           allow_redirects=False).json()
    else:
        hot = requests.get('https://api.reddit.com/r/{}/hot?after={}\
'.format(subreddit, after),
                           headers={'User-Agent': 'madmansilver'},
                           allow_redirects=False).json()

    if 'data' not in hot:
        return None

    for post in hot.get('data').get('children'):
        hot_list.append(post)

    after = hot.get('data').get('after')

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
