#!/usr/bin/python3

"""Definition of a Rectangle class representing rectangles (based on 2-rectangle.py)"""


class Rectangle:
    """Implementation of the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle instance
            Args:
                width (int): Width of the rectangle
                height (int): Height of the rectangle
            Raises:
                TypeError: if width is not an integer
                ValueError: if width is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Get the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += "#"
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Return a string representation for recreating the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

