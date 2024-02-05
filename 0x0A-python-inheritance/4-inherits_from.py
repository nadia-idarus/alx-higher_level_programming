#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, returns False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a class that inherits from a_class,
      False otherwise.
    """
    return issubclass(type(obj), a_class)

# Example usage:
class MyBaseClass:
    pass

class MyDerivedClass(MyBaseClass):
    pass

example_object = MyDerivedClass()
result = inherits_from(example_object, MyBaseClass)
print(result)  # This will print True

