import queue
from threading import Thread
import time
import random
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.guest_queue = Queue()
        self.tables_queue = Queue()
        for table in self.tables:
            if not table.guest:
                self.tables_queue.put(table)

    def guest_arrival(self, *guests):
        for guest in guests:
            if not self.tables_queue.empty():
                table = self.tables_queue.get()
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                guest.start()
                continue
            self.guest_queue.put(guest)
            print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.guest_queue.empty() or [table.guest for table in self.tables if table.guest]:
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.guest_queue.empty():
                        guest = self.guest_queue.get()
                        print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest = guest
                        guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
