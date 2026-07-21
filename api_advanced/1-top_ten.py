#!/usr/bin/python3
"""Print the titles of the first ten hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data")
    posts = data.get("children")

    for post in posts[:10]:
        print(post.get("data").get("title"))
