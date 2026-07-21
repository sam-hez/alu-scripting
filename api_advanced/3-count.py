#!/usr/bin/python3
"""Count words in hot post titles for a subreddit."""

import requests


def count_words(subreddit, word_list, after=None, count=None, words=None):
    """Print a sorted count of keywords in hot post titles."""
    if count is None:
        count = {}
        words = {}
        for word in word_list:
            word = word.lower()
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
            count[word] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 100
    }

    if after is not None:
        params["after"] = after

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title")
        title_words = title.lower().split()
        for word in title_words:
            if word in words:
                count[word] += words.get(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, count, words)

    sorted_words = sorted(count.items(), key=lambda item: (-item[1], item[0]))
    for word, total in sorted_words:
        if total > 0:
            print("{}: {}".format(word, total))
