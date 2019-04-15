# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed
        return

    def go(self):
        print("Машина {} {}  цвета поехала со скростью {} км".format(self.name, self.color, self.speed))

    def stop(self):
        print("Машина {} {}  цвета остановилась ".format(self.name, self.color))

    def turn(self):
        print("Машина {} {} повернула !".format(self.name, self.color))


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)



class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)



car1 = SportCar (120, "синего", "GTR")
car1.go()
car2 = TownCar (60, "красного", "Ноnda")
car2.turn()
car3 = WorkCar (0, "Чёрного", "камаз")
car3.stop()
