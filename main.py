
from random import choice
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 20
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(auto)
        def get_job(self):
            if self.car.drive():
                pass
            else:
                self.to_repair()
                self.job = Job(option_work)
    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:  # Тут зупинка
    # self.money += 100
    # self.happiness += 2
    def to_chill(self):
        pass
    def to_repair(self):
        pass

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0
class Auto:
    def __init__(self, auto):
        self.brand = choice(list(auto))
        self.fuel = auto[self.brand]["fuel"]
        self.strength = auto[self.brand]["strength"]
        self.consumption = auto[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False
class Job:
    def __init__(self, option_work):
        self.work = choice(list(option_work))
        self.salary = option_work[self.work]['salary']
        self.gladness = option_work[self.work]['gladness']
option_work = {"Developer C++": {"salary": 50, 'gladness': 10},
               "Developer Python": {"salary": 40, 'gladness': 20}, }

auto = {"BMW": {"fuel": 50, "strength": 100, "consumption": 18},
        "OPEL": {"fuel": 30, "strength": 60, "consumption": 12},
        "FORD": {"fuel": 35, "strength": 80, "consumption": 10},}

nick = Human()
