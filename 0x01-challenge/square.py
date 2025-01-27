#!/usr/bin/python3
""" Square Class Module"""


class Square():
    """ Square Class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instance creation """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter calculation """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printing attributes """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
