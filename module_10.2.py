# "Потоки на классах"
# Задача "За честь и отвагу!"

# Импорты необходимых модулей и функций
import time, threading


class Knight(threading.Thread):

    def __init__(self, name, power ):
        threading.Thread.__init__(self)
        self.name = name # имя рыцаря (str)
        self.power  = power # сила рыцаря (int)

    def run(self):  # сражение с врагами
        enemies = 100   # количество врагов
        days = 0
        print(self.name,', на нас напали!')

        while enemies >= self.power:
            time.sleep(1) 
            enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов') 

        print(f'{self.name} одержал победу спустя {days} дней (дня, день)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')

