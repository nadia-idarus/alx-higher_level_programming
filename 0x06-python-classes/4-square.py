class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # Check if size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if size is non-negative
        if value < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = value

    def area(self):
        return self.__size ** 2

