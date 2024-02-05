#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise, returns False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)

# Example usage:
example_object = [1, 2, 3]
result = is_kind_of_class(example_object, list)
print(result)  # This will print True

