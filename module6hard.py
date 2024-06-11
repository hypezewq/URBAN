class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides: int, filled=False) -> None:
        self.color: list[int] = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides: list[int] = list(sides)
        self.filled: bool = filled

    def get_color(self) -> list[int]:
        return self.color

    def get_sides(self) -> list[int]:
        return self.__sides

    @staticmethod
    def __is_valid_color(r: int, g: int, b: int) -> bool:
        return all(i in range(256) for i in (r, g, b))

    def __is_valid_sides(self, *sides: int) -> bool:
        return all(i > 0 for i in sides) and self.sides_count == len(sides)

    def set_sides(self, *sides: int) -> None:
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else self.__sides

    def set_color(self, r: int, g: int, b: int) -> None:
        self.color = [r, g, b] if self.__is_valid_color(r, g, b) else self.color

    def __len__(self) -> int:
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], length: int, filled=False) -> None:
        super().__init__(color, length, filled=filled)
        self.__radius: float = length * 0.5 * 3.14

    def get_square(self) -> float:
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], sides: int, filled=False) -> None:
        super().__init__(color, sides, filled=filled)
        p = len(Triangle) / 2
        self.__height: float | int = p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]) / sides[0]

    def get_square(self) -> float | int:
        return self.__height * 0.5 * self.__sides[0]


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side: int, filled=False) -> None:
        self.side = side
        super().__init__(color, *[side] * 12, filled=filled)

    def get_volume(self) -> float | int:
        return self.side ** 3


