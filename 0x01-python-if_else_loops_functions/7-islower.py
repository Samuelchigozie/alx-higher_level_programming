#!/usr/bin/python3
# Author - Samuel Chigozie

def islower(c):
    """Function checks if there is any lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
