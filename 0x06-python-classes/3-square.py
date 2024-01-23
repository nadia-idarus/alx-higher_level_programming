#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is non-negative
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

