#!/usr/bin/python3
"""A class definition for a square"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializer for the square class
        Args:
            size: Specifies the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieves the value of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square
        Args:
            value: Represents the new size value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates the area of the square
        Returns: The square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters to stdout
        Prints an empty line if size = 0
        """

        if self.__size == 0:
            print()

        for row in range(self.__size):
            print("#" * self.__size)

