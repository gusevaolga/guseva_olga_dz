from time import sleep

class TrafficLight:
    __color = "Red"

    def running(self):
        while True:
            print(self.__color)
            sleep(7)
            self.__color = 'Yellow'
            print(self.__color)
            sleep(2)
            self.__color = 'Green'
            print(self.__color)
            sleep(5)
            self.__color = 'Red'


tl = TrafficLight()
tl.running()

