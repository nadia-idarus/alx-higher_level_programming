#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end=' ')
    except IndexError:
        pass  # Handles the case where x is greater than the length of the list
    finally:
        print()  # Adds a newline after printing the elements

# Example usage:
my_list = [1, 2, 3, 4, 5]
safe_print_list(my_list, 3)

