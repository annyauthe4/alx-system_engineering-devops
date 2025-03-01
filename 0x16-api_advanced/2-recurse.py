#!/usr/bin/python3
"""
Recursively queries an API for a list of titles
of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Fetches hot articles recursively.

    Args:
        subreddit (str): Subreddit to be parsed as argument.
        hot_list (list, optional): The list to store the titles
        of hot articles. Default, None.
        after (str, optional): The 'after' parameter for pagination.
        Default, None.

    Returns:
        list: A list of all hot article titles for the given subreddit.
        None: If invalid subreddit is passed or error occured.
    """
    # Initialize the hot_list if it's None
    if hot_list is None:
        hot_list = []

    # Define the URL for the Reddit API endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid too many requests error
    headers = {"User-Agent": "custom-script:v1.0 ( by/u/Otherwise-Fondant360)"}

    # Define parameters for pagination
    params = {"limit": 100}  # Fetch up to 100 posts per request
    if after:
        params["after"] = after

    try:
        # Send a Get request to the Reddit API
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check for response failure
        if response.status_code != 200:
            return None
        # Convert response to JSON object
        data = response.json()

        # Extract the list of posts from the 'data.children'
        posts = data.get("data", {}).get("children", [])

        # Get the title of each post and add it to the hot_list
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        # Check if there are more pages to fetch
        after_value = data.get("data", {}).get("after")
        if after_value:
            # Recursively call the function with the 'after' parameter
            return recurse(subreddit, hot_list, after=after_value)
        else:
            # No more pages, return the completed hot_list
            return hot_list
    except (KeyError, ValueError):
        return None
