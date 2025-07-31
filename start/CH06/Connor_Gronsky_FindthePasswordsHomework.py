# Created by Connor Gronsky on 7/31/2025
# Find the passwords homework

import os
import sys
from passlib.hash import sha512_crypt

def test_password(hashed_password, plaintext_password):
    # Use built-in verify() method (auto-uses salt & rounds from hash)
    return sha512_crypt.verify(plaintext_password, hashed_password)

def read_dictionary():
    file_path = os.path.join(script_dir, "top1000000.txt")
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().splitlines()

def read_shadow_file():
    file_path = os.path.join(script_dir, "shadow")
    with open(file_path, "r") as f:
        return f.readlines()

# Get script directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Load data
passwords = read_dictionary()
shadow_entries = read_shadow_file()
cracked = {}

# Attempt to crack each user
for line in shadow_entries:
    parts = line.strip().split(":")
    if len(parts) < 2 or not parts[1].startswith("$6$"):
        continue

    username = parts[0]
    hashed_password = parts[1]

    for password in passwords:
        try:
            if test_password(hashed_password, password):
                print(f"[+] Match found: {username} = {password}")
                cracked[username] = password
                break
        except:
            continue  # In case of malformed hashes

# Final output
if not cracked:
    print("[-] No matches found.")
else:
    print("\n[+] Summary of cracked accounts:")
    for user, pwd in cracked.items():
        print(f"{user}: {pwd}")

