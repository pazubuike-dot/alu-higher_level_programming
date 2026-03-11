def __str__(self):
        """Returns string of rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += ("#" * self.__width)
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str
