#\!/usr/bin/env python3
 # Script that encrypts/decrypts text using ROT13
 # By Connor Gronsky on 7/22/2025
 # Prompt for the source message
  # source_message \= input("What is the message to encrypt/decrypt? ")
 # Convert message to lower-case for simplicity source_message \= source_message.lower() final_message \= ""
 # Loop through each letter in the source message

source_message = "your message here"
final_message = ""

for letter in source_message:
    # Convert the letter to the ASCII equivalent
    ascii_num = ord(letter)
    
    # Check to see if it's a lowercase alphabetic (a-z) character
    if ascii_num >= 97 and ascii_num <= 122:
        # Add 13 to ascii_num to "shift" it by 13
        new_ascii = ascii_num + 13
        
        # Confirm new character will still be alphabetic
        if new_ascii > 122:
            # If not, wrap around
            new_ascii = new_ascii - 26
        
        final_message = final_message + chr(new_ascii)
    else:
        # Keep the character unchanged if not a-z
        final_message = final_message + chr(ascii_num)

# Print converted message
print("Hello World:")

