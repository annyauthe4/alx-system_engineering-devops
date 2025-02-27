#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed
for a given subreddit API.
"""


import requests


def top_ten(subreddit):
    """Prints top 10 hot posts of an API."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "custom-script:v1.0 ( by/u/Otherwise-Fondant360)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print(None)
