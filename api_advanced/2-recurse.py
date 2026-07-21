#!/usr/bin/python3
"""Return all hot post titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 100
    }

    if after is not None:
        params["after"] = after
    else:
        hot_list = list(hot_list)

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    children = data.get("children")

    hot_list += [
        child.get("data").get("title")
        for child in children
    ]

    after = data.get("after")
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list

    return recurse(subreddit, hot_list, after)
