# Reddit API

This directory contains Python functions that query the Reddit API and process
information about subreddits.

## Task 0: How many subs?

`0-subs.py` provides the function `number_of_subscribers(subreddit)`. It
returns the total number of subscribers for a valid subreddit and returns `0`
when the subreddit is invalid.

## Task 1: Top Ten

`1-top_ten.py` provides the function `top_ten(subreddit)`. It prints the
titles of the first ten hot posts for a valid subreddit and prints `None` when
the subreddit is invalid.

## Task 2: Recurse it!

`2-recurse.py` provides the function `recurse(subreddit)`. It returns a list
of all hot post titles for a valid subreddit and returns `None` when the
subreddit is invalid.

## Task 3: Count it!

`3-count.py` provides the function `count_words(subreddit, word_list)`. It
counts given keywords in hot post titles and prints the results sorted by count
and then alphabetically.
