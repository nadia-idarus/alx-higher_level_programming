#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage:
my_list_instance = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
my_list_instance.print_sorted()

