from time import sleep

colors = {
    'red': [7, '6;30;41'],
    'yellow': [2, '5;30;43'],
    'green': [7, '6;30;42']
}


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.next_color()
            self.show_color()
            self._wait()

    def next_color(self):
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
        else:
            self.__color = 'red'

    def show_color(self):
        print(f'\x1b[{colors[self.__color][1]}m{self.__color}\x1b[0m')

    def _wait(self):
        sleep(colors[self.__color][0])


my_tl = TrafficLight()
my_tl.running()