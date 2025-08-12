#!/usr/bin/env python3
# Script that tells us how many people there are in space
# By Connor Gronsky on 8/12/2025

# Import Python modules
import requests
import json

def get_people_in_space():
    request_uri = "http://api.open-notify.org/astros.json"
    r = requests.get(request_uri)
    items = r.json()
    return items

astronauts = get_people_in_space()

# Print basic details
print(astronauts)

# Print "pretty" JSON
print(json.dumps(astronauts, indent=2))
