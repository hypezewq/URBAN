class Vehicle:
    __COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.__power = power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), self.owner, sep="\n")

    def set_color(self, color):
        if color in self.__COLOR_VARIANTS:
            self.__color = color
        print(f"Нельзя сменить цвет на {color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'BLUE', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()