#!/usr/bin/python3
"""Print the titles of the first ten hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/sam-hez)"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])

    for post in posts:
        print(post.get("data", {}).get("title"))
