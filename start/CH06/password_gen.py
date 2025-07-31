import random
import string

# Define color codes for terminal output
# Note: These may not work in all terminal environments, but are standard.
class Colors:
    LETTER = '\033[92m'  # Green
    NUMBER = '\033[94m'  # Blue
    SYMBOL = '\033[91m'  # Red
    UNICODE = '\033[93m' # Yellow
    ENDC = '\033[0m'     # Reset color

def generate_password(
    length=16,
    include_lowercase=True,
    include_uppercase=True,
    include_numbers=True,
    include_symbols=True,
    include_unicode=False,
    exclude_similar=False,
    exclude_ambiguous=False,
    first_char_is_letter=True
):
    """
    Generates a secure, random password with various customization options.

    Args:
        length (int): The desired length of the password. Must be between 4 and 300.
        include_lowercase (bool): If True, includes lowercase letters (a-z).
        include_uppercase (bool): If True, includes uppercase letters (A-Z).
        include_numbers (bool): If True, includes numbers (0-9).
        include_symbols (bool): If True, includes common symbols (!@#$%^&*()_+-=[]{}|;':",./<>?`~).
        include_unicode (bool): If True, includes a range of common Unicode characters.
        exclude_similar (bool): If True, excludes similar-looking characters like 'i, l, 1'.
        exclude_ambiguous (bool): If True, excludes characters that might be ambiguous, such as '{}[]()'.
        first_char_is_letter (bool): If True, ensures the first character is a letter.

    Returns:
        str: A randomly generated password.
    """
    if not (4 <= length <= 300):
        print(f"Error: Password length must be between 4 and 300 characters. Using default length of 16.")
        length = 16

    # Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"

    # Define characters to be excluded
    similar_chars_to_exclude = "iIlL1o0O|!"
    ambiguous_chars_to_exclude = "{}[]()/\'\"!,;:>,.<"
    
    # Define a simple set of common Unicode characters for demonstration
    # You could expand this list significantly.
    unicode_chars = "".join([chr(i) for i in range(161, 256) if chr(i).isprintable()])

    # Build the master character pool based on user preferences
    char_pool = ""
    if include_lowercase:
        char_pool += lowercase_chars
    if include_uppercase:
        char_pool += uppercase_chars
    if include_numbers:
        char_pool += number_chars
    if include_symbols:
        char_pool += symbol_chars
    if include_unicode:
        char_pool += unicode_chars

    # Apply exclusion rules
    if exclude_similar:
        char_pool = "".join(c for c in char_pool if c not in similar_chars_to_exclude)
    if exclude_ambiguous:
        char_pool = "".join(c for c in char_pool if c not in ambiguous_chars_to_exclude)

    # Ensure at least one character type is selected
    if not char_pool:
        print("Error: No character types selected. Please enable at least one. Using default settings.")
        char_pool = string.ascii_letters + string.digits

    password = []

    # Handle the first character if it must be a letter
    if first_char_is_letter and (include_lowercase or include_uppercase):
        letter_pool = ""
        if include_lowercase:
            letter_pool += lowercase_chars
        if include_uppercase:
            letter_pool += uppercase_chars
        if exclude_similar:
            letter_pool = "".join(c for c in letter_pool if c not in similar_chars_to_exclude)
        
        if letter_pool:
            password.append(random.choice(letter_pool))
    
    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle the list to ensure true randomness and return as a string
    random.shuffle(password)
    return "".join(password)

def color_code_password(password):
    """
    Color-codes the password characters for visual identification.
    """
    colored_password = []
    for char in password:
        if char in string.ascii_lowercase or char in string.ascii_uppercase:
            colored_password.append(f"{Colors.LETTER}{char}{Colors.ENDC}")
        elif char in string.digits:
            colored_password.append(f"{Colors.NUMBER}{char}{Colors.ENDC}")
        elif char in string.punctuation:
            colored_password.append(f"{Colors.SYMBOL}{char}{Colors.ENDC}")
        else: # Assumed to be unicode for this example
            colored_password.append(f"{Colors.UNICODE}{char}{Colors.ENDC}")
    
    return "".join(colored_password)

if __name__ == "__main__":
    
    # --- Example 1: A simple, default password ---
    print("\n--- A simple, default password ---")
    password = generate_password()
    colored_password = color_code_password(password)
    print(f"Password: {colored_password}")
    print(f"Raw password: {password}")

    # --- Example 2: Multiple passwords with specific criteria ---
    print("\n--- Generating 3 passwords, 24 characters long ---")
    print("--- Includes lowercase, uppercase, numbers, and symbols ---")
    print("--- Excludes similar and ambiguous characters ---")
    
    # Unicode characters are often typed using their hexadecimal code preceded by "U+" (e.g., U+00A9 for the copyright symbol ©)
    print("--- Includes unicode characters (e.g., é, ß, ©) ---")
    print("\nColor Legend:")
    print(f"{Colors.LETTER}Letters{Colors.ENDC} | {Colors.NUMBER}Numbers{Colors.ENDC} | {Colors.SYMBOL}Symbols{Colors.ENDC} | {Colors.UNICODE}Unicode{Colors.ENDC}\n")

    for i in range(3):
        password = generate_password(
            length=24,
            exclude_similar=True,
            exclude_ambiguous=True,
            include_unicode=True,
            first_char_is_letter=True
        )
        colored_password = color_code_password(password)
        print(f"Password {i+1}: {colored_password}")
    
    # --- Example 3: A very long password for a specific use case ---
    print("\n--- A very long password (100 characters) for a specific use case ---")
    password = generate_password(
        length=100,
        include_lowercase=False,
        include_uppercase=False,
        include_symbols=False,
        include_numbers=True,
        first_char_is_letter=False
    )
    colored_password = color_code_password(password)
    print(f"Password: {colored_password}")
