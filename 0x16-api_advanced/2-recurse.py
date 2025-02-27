#!/usr/bin/python3
"""
Recursively queries an API for a list of titles
of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[]):
    """Fetches hot articles recursively"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom-script:v1.0 ( by/u/Otherwise-Fondant360)"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        data = response.json()
        posts = data["data"]["children"]
        hot_list.extend([post["data"]["title"] for post in posts])
        after = data["data"].get("after")

        if after is not None:
             return recurse(subreddit, hot_list, after)
        return hot_list
    except (KeyError, ValueError):
        return None
