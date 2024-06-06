class House:
    def __init__(self, name, floors):
        self.name, self.floors = name, floors

    def go_to(self, floor):
        if 0 < floor <= self.floors:
            for i in range(1, floor + 1):
                print(i)
            return 0
        print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
