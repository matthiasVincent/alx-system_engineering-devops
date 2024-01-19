#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Api-advanced by matthiasVincent"
    }
    auth = requests.auth.HTTPBasicAuth('matthiasVinco', 'Matthias@28908')
    response = requests.get(
            url, auth=auth,
            headers=headers, allow_redirects=False
            )
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    print('OK')
    return results.get("subscribers")
