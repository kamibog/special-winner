import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0

        while self.enemy > 0:
            time.sleep(1)
            days += 1
            self.enemy -= self.power
            test = max(self.enemy, 0)
            print(f"{self.name}, сражается {days} день..., осталось {test} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней!")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
