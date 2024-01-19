#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    token = 'bearer' + '\
    eyJhbGciOiJSUzI1NiIsImt
    pZCI6IlNIQTI1NjpzS3dsMnlsV0Vt
    MjVmcXhwTU40cWY4MXE2OWFFdWFy
    MnpLMUdhVGxjdWNZIiwidHlwIjoiS
    ldUIn0.eyJzdWIiOiJ1c2VyIiwiZX
    wIjoxNzA1NzE2NTU5LjQzNzUwNCw
    iaWF0IjoxNzA1NjMwMTU5LjQzNz
    UwNCwianRpIjoiek9UUkRUX3NSY0h
    jZzdCR3RtTENwX0JrdlRMMGFnIiwi
    Y2lkIjoiRmdpMWE1NUhDZ3F6cVFrd1JFM
    0JGZyIsImxpZCI6InQyX3FtOXVpczBtaSIs
    ImFpZCI6InQyX3FtOXVpczBtaSIsImxjYSI6
    MTcwMzQyMjU5MTQ5MCwic2NwIjoiZUp5S1Z
    0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iO
    jl9.FP4iQPSkeqFq5OF-GlTfLOijA65kstZ1VFd
    k5NIWZgn8Xsp_2u_rH8c3Tgt4bYcIUsK7cOxor
    PoyT2xUOIzM5c8DPLLIU6hB55ckJEkWy7QXmKCkSNu
    5UnIioLOyYZwryCivmX1yHnQ83SViVBxiXB9ce8
    HHPG2a3mY62wYqk_CkBbMqjN1mAsEFUe6LL7u2-MOA
    m0L0F0k-hL1UnbQy8KLnoInpYv9SEfpr6VM6
    FzjGxuzaGRpYsAKkKaExq545D6E-5HtCKpK
    f36b9IWuhcmPmHVSN_X1OFxJ9ZS47Q4WQBAHG4o
    lxo-eDllundo7e2mUsh221Jc57r1sEcXnCWA
    '
    headers = {
        "User-Agent": "Api-advanced by matthiasVincent",
        "token": token
    }
    # auth = requests.auth.HTTPBasicAuth('matthiasVinco', 'Matthias@28908')
    response = requests.get(
            url,
            headers=headers, allow_redirects=False
            )
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
