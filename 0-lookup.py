#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object to inspect.

    Returns:
    - List of attributes and methods.
    """
    return dir(obj)

# Example usage:
example_object = "Hello, World!"
result = lookup(example_object)
print(result)

