class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = True

        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, (int, float)) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, 2 * 3.14 * radius)
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, [side_length] * 12)

    def get_volume(self):
        return self.get_volume


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
