#!/usr/bin/env python3
# Example brute-force attacker
#By Connor Gronsky on 7/29/2025

# NOTE: this example is limited to numbers. There are no letters or symbols in this example
# Suggested to start by debugging to show how brute force walks through all available options 

from passlib.hash import sha512_crypt

def test_password(hashed_password, salt, plaintext_password):
    crypted_password = sha512_crypt.using(rounds=5000).hash(plaintext_password, salt=salt)
    return hashed_password == crypted_password

hashed_password = "$6$G.DTW7g9s5U7KYf5$QFcHx0/J88HV/Q0ab653"
hashed_password += "gfYQ1KyNGx5HRhDQYyai2ZUy7Aw4tyfJ6/kI6kl"
hashed_password += "lfXl0DyS.LuaUJvqnlIn2fVM5F0"
salt = "G.DTW7g9s5U7KYf5"

for password in range(100000):
    result = test_password(hashed_password, salt, str(password))
    if result:
        print("Match found: {0}".format(password))
        break
