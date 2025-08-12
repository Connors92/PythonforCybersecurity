#!/usr/bin/env python3
# Script that prints random Dad Joke using API
# By Connor Gronsky on 8/12/2025

# Import Python modules

import requests

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        joke_data = response.json()
        print("Here's a random dad joke:")
        print(joke_data.get("joke", "No joke found."))
    else:
        print(f"Failed to retrieve joke. Status code: {response.status_code}")

# Call the function to get and print a dad joke
get_dad_joke()
