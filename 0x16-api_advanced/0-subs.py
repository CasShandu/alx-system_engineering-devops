#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my-app v1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Debugging output
        print(f"Status Code: {response.status_code}")
        print(f"Response URL: {response.url}")

        if response.status_code == 200:
            try:
                data = response.json().get("data")
                if data:
                    return data.get("subscribers", 0)
            except ValueError:
                print("Error decoding JSON.")
        elif response.status_code == 302:
            # Redirect status code (likely for invalid subreddit)
            print("Redirect detected. Likely invalid subreddit.")
        else:
            print(f"Unexpected status code: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")

    return 0

