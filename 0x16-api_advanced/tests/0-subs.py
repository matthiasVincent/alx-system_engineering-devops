#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers():
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/programming/about.json"
    headers = {
        "User-Agent": "Api-advanced by matthiasVinco"
    }
    data = {
            'grant_type': 'password',
            'username': 'matthiasVinco',
            'password': 'Matthias@28908'
            }
    response = requests.get(url, data=data, headers={
        'User-Agent': 'Api-advanced by matthiasVinco'})
    if response.status_code == 404:
        return 0
    results = response.status_code
    return results

print(number_of_subscribers())
