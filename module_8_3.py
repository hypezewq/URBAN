class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__number = number if self.__is_valid_number(number) else None

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номера")
        if vin not in range(1000000, 10000000):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(number) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')