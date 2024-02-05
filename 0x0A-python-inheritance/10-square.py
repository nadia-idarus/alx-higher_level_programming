#!/usr/bin/python3
"""Defines a Square class."""
from rectangle import Rectangle

class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
