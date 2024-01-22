#!/usr/bin/python3
import sys

def print_safe_integer(value):
    try:
        # Attempt to print the value as an integer
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        # If there's an issue, print an exception message to stderr
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        # If successful, return True
        return True

