# Created by Connor Gronsky on 7/31/2025
# Automated Password Generator

import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# SETTINGS
SETTINGS = {
    "length": 100, #Password length should be between 4 and 300 characters
    "lower": True,
    "upper": True,
    "digits": True,
    "symbols": True,
    "exclude_similar": True,
    "exclude_ambiguous": True,
    "require_letter_start": True,
    "num_passwords": 10
}

# Characters to exclude
SIMILAR_CHARS = set("ilLI|1!")
AMBIGUOUS_CHARS = set("{}[]()/\\'\"!,;:>.")

def build_character_pool(settings):
    pool = ""
    if settings["lower"]:
        pool += string.ascii_lowercase
    if settings["upper"]:
        pool += string.ascii_uppercase
    if settings["digits"]:
        pool += string.digits
    if settings["symbols"]:
        pool += string.punctuation

    if settings["exclude_similar"]:
        pool = ''.join(c for c in pool if c not in SIMILAR_CHARS)
    if settings["exclude_ambiguous"]:
        pool = ''.join(c for c in pool if c not in AMBIGUOUS_CHARS)

    return pool

def generate_password(length, pool, require_letter_start):
    if not pool:
        return "[ERROR] Character pool is empty."

    if require_letter_start:
        letters = ''.join(c for c in pool if c.isalpha())
        if not letters:
            return "[ERROR] No letters for first character."
        first_char = random.choice(letters)
        rest = ''.join(random.choice(pool) for _ in range(length - 1))
        return first_char + rest
    else:
        return ''.join(random.choice(pool) for _ in range(length))

def colorize_password(pw):
    colored = ""
    for c in pw:
        if c in string.ascii_lowercase:
            colored += Fore.BLUE + c     # Lowercase
        elif c in string.ascii_uppercase:
            colored += Fore.GREEN + c    # Uppercase
        elif c in string.digits:
            colored += Fore.YELLOW + c      # Numbers
        elif c in string.punctuation:
            colored += Fore.MAGENTA + c  # Symbols
        else:
            colored += Fore.RED + c   # Others
    return colored + Style.RESET_ALL

def print_legend():
    print("\nLegend:")
    print(Fore.BLUE + "Blue" + Style.RESET_ALL + "    = Lowercase Letters")
    print(Fore.GREEN + "Green" + Style.RESET_ALL + "   = Uppercase Letters")
    print(Fore.YELLOW + "Yellow" + Style.RESET_ALL + "  = Numbers")
    print(Fore.MAGENTA + "Magenta" + Style.RESET_ALL + " = Symbols")
    print(Fore.RED + "Red" + Style.RESET_ALL + "     = Other Characters\n")

def main():
    pool = build_character_pool(SETTINGS)

    print("Generated Passwords:\n" + "-" * 30)
    for _ in range(SETTINGS["num_passwords"]):
        pw = generate_password(SETTINGS["length"], pool, SETTINGS["require_letter_start"])
        print(colorize_password(pw))

    print_legend()

if __name__ == "__main__":
    main()
