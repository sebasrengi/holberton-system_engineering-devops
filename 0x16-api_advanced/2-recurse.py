#!/usr/bin/python3
"""
    Module for task 2
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    param = {'after': after, 'limit': '100'}
    response = requests.get(url, headers=headers, params=param)

    if response.status_code == 200:
        hotPosts = response.json()['data']['children']
        after = response.json()['data']['after']

        for posts in hotPosts:
            hot_list.append(posts['data']['title'])

        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list

    return None
