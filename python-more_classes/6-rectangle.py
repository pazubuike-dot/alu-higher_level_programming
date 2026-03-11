class Rectangle:
    number_of_instances = 0  # Put this right under the class name

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1  # Add this line
        self.width = width
        self.height = height

    # ... keep all your getters, setters, area, perimeter, str, repr ...

    def __del__(self):
        type(self).number_of_instances -= 1  # Add this line
        print("Bye rectangle...")
