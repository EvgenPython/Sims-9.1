from random import randint


class Transport:
    engine = True
    driver = True
    weight = 100

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def move(self):
        self.speed += randint(5, 50)
        return self.speed


class Auto(Transport):

    def __init__(self, wheels, age, speed, color):
        super().__init__(speed, color)
        self.wheels = wheels
        self.age = age

auto = Auto(4, 10, 25, 'green')
print(auto.wheels)
print(auto.age)
print(auto.engine)
print(auto.driver)
print(auto.weight)
print(auto.speed)
print(auto.color)