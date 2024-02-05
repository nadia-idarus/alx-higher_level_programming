#!/usr/bin/python3
""" Defines a Rectangle class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Represents a rectangle. """

    def __init__(self, width, height):
        """ Initialize a new Rectangle. """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Return the print/str representation of the Rectangle. """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
