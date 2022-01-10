import random


class Car:
    accelerate_speed = 1

    def __init__(self, name, color):
        self.name = name
        self.speed = 0
        self.color = color
        self.is_police = None
        self._movement_direction = None

    def go(self):
        self.speed += self.accelerate_speed

    def push_brake(self):
        self.speed -= self.accelerate_speed
        if self.speed < 0:
            self.stop()

    def stop(self):
        self.speed = 0
        print(f'The car is stopped')

    def turn(self, direction):
        if direction == 'left' or direction == 'right':
            self._movement_direction = direction
            print(f'Turn {direction}')
        else:
            print('f{Unknown direction, must be left or right')

    def show_speed(self):
        if self.speed > 110:
            self._show_warning()
        return self.speed

    def _show_warning(self):
        print(f'WARNING! Speed {self.speed} is too high!')

    def __str__(self):
        return f'A car {self.name} in {self.color} color has speed {self.speed}'


class WorkCar(Car):
    accelerate_speed = 5

    def show_speed(self):
        if self.speed > 40:
            self._show_warning()
        return self.speed


class TownCar(Car):
    accelerate_speed = 10

    def show_speed(self):
        if self.speed > 60:
            self._show_warning()
        return self.speed


class SportCar(Car):
    accelerate_speed = 20


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True

    def __str__(self):
        return f'A POLICE car {self.name} in {self.color} color has speed {self.speed}'


car_pol = PoliceCar('TOYOTA', 'white')
print(car_pol)
car_1 = Car('CAR-1', 'RED')
print(car_1)
car_sport = SportCar('Lamborgini', 'blue')
print(car_sport)
car_sport.go()
print(car_sport)
car_sport.go()
print(f'Speed of {car_sport.name} is {car_sport.show_speed()}')
car_sport.go()
print(f'Speed of {car_sport.name} is {car_sport.show_speed()}')
print(car_sport)