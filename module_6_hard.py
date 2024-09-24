class Figure:
    def __init__(self, color: list, *sides: int):
        self.__color = [*color] if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    @property
    def __is_valid_color(self):
        def check_color(r, g, b):
            return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        return check_color

    @property
    def __is_valid_sides(self):
        def check_sides(*new_sides):
            if len(new_sides) != self.sides_count:
                return False
            return all(isinstance(side, int) and side > 0 for side in new_sides)
        return check_sides

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    def __init__(self, color:str, *sides:int):
        self.sides_count = 1
        super().__init__(color, *sides)
        if len(sides) != 1:
            self._Figure__sides = [1]

    def get_square(self):
        radius = self.get_sides()[0] / (2 * 3.14159)  # длина окружности = 2 * pi * r
        return 3.14159 * (radius ** 2)


class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)
        if len(sides) != 3:
            self._Figure__sides = [1, 1, 1]

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12
        super().__init__(color, *sides)

        if len(sides) != 1:
            self._Figure__sides = [1] * 12
        else:
            self._Figure__sides = [sides[0]] * 12

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


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