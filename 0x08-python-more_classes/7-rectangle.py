#!/usr/bin/python3
"""A class that represents a rectangle"""


class Rectangle:
    """Definition of the Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class with specified width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute with error checking.
        
        Args:
            value (int): The width value to be set.
            
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute with error checking.
        
        Args:
            value (int): The height value to be set.
            
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    rectangle_str += str(self.print_symbol)
                except Exception:
                    rectangle_str += type((self).print_symbol)
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Return a string representation for recreating the object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrease the instance count when a Rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

