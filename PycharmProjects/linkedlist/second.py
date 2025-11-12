class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return "A rectange with a width of " + str(self.width) + " and a height of " + str(self.height) + "."

my_rect = Rectangle(8,5)

print(my_rect.get_area())
print(str(my_rect))
