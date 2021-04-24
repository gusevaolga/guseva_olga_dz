class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print('GO!')

    def stop(self):
        print('STOP!')

    def turn(self, direction):
        print(f'Turn {direction}')

    def show_speed(self):
        print(f'Current vehicle speed = {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Over speed!!!')
        else:
            print(f'Current vehicle speed = {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Over speed!!!')
        else:
            print(f'Current vehicle speed = {self.speed}')

class PoliceCar(Car):
    pass

car_1 = TownCar(45,'red', 'Lada', False)
car_1.show_speed()
car_2 = TownCar(120, 'yellow', 'Mazda', False)
car_2.show_speed()




