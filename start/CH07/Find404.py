 #\!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Connor Gronsky on 8/5/2025

import os

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Get current file directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, log_file)

# Open file
with open(file_path, "r") as f:
    # Read file line by line
    for line in f:
        # Check for 404
        if "404" in line:
            print(line.strip())
