#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://oauth.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Api-advanced by matthiasVinco)"
    }
    auth = requests.auth.HTTPBasicAuth('matthiasVinco', 'Matthias@28908')
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, auth=auth, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
