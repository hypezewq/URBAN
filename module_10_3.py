from threading import Thread, Lock
import random
import time


class Bank:
    lock = Lock()

    def __init__(self):
        self.balance = 500

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на снятие {amount}")
            if amount > self.balance:
                print(f"Запрос отклонён. Недостаточно средств.")
                self.lock.acquire()
            self.balance -= amount
            print(f"Снятие: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
