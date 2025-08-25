from string import ascii_letters, digits
from random import choice

def generate_string(initials="", length=15):
    """
    Helps to generate alpha-numeric string.
    """
    chars = ascii_letters + digits
    return initials + "".join(choice(chars) for _ in range(length))

