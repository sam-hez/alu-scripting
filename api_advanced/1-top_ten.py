#!/usr/bin/python3
"""Print the titles of the first ten hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/sam-hez)"
    }
    params = {
        "limit": 10
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data")
    posts = data.get("children")

    for post in posts:
        print(post.get("data").get("title"))
