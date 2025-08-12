 #!/usr/bin/env python3
# Script that checks passwords against haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Connor Gronsky
# Date: 8/12/2025

# Import Python modules
import requests
import hashlib

def sha1_hash(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

def check_haveibeenpwned(sha_prefix):
    # Create empty dictionary
    pwnd_dict = {}
    # Send request to API
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    r = requests.get(request_uri)
    # Separate list by newline
    pwnd_list = r.text.split("\r\n")
    for pwnd_pass in pwnd_list:
        # Separate each line by colon
        pwnd_hash = pwnd_pass.split(":")
        # Add hash and value to dictionary
        pwnd_dict[pwnd_hash[0]] = pwnd_hash[1]
    # Return dictionary
    return pwnd_dict

# Get password to check
password = input("What password needs to be checked? ")
# Get SHA-1 hash of password
sha_password = sha1_hash(password).upper()
# Slice hash at the 5th character
sha_prefix = sha_password[0:5]
sha_postfix = sha_password[5:]
# Call API with first 5 characters
pwnd_dict = check_haveibeenpwned(sha_prefix)

# Check if hash is in results
if sha_postfix in pwnd_dict.keys():
    print("Password has been compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
    print("Password has not been compromised. It is safe to use!")
