# Билет №13
class Auto():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, go):
        if self.direction.lower() == 'вправо':
            self.x += abs(go)
            print('Двигаемся вправо на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
        elif self.direction.lower() == 'влево':
            self.x -= abs(go)
            print('Двигаемся влево на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
        elif self.direction.lower() == 'вверх':
            self.y += abs(go)
            print('Двигаемся вверх на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
        elif self.direction.lower() == 'вниз':
            self.x -= abs(go)
            print('Двигаемся вниз на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))

    def change_of_direction(self, direction):
        self.direction = direction
        print('Текущее направление: ' + direction.upper())

class Bus(Auto):

    def __init__(self, x, y, direction, number_of_passengers):
        super().__init__(x, y, direction)
        self.number_of_passengers = number_of_passengers
        self.money = 0

    def enter(self, number):
        if number > 0:
            self.number_of_passengers += number
        print('Число пассажиров: ' + str(self.number_of_passengers))

    def exit(self, number):
        if number > 0:
            self.number_of_passengers -= number
        print('Число пассажиров: ' + str(self.number_of_passengers))

    def move(self, go):
        if self.direction.lower() == 'вправо':
            self.x += abs(go)
            self.money += go * self.number_of_passengers
            print('Двигаемся вправо на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
            print('Количество денег: ' + str(self.money))
        elif self.direction.lower() == 'влево':
            self.x -= abs(go)
            self.money += go * self.number_of_passengers
            print('Двигаемся влево на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
            print('Количество денег: ' + str(self.money))
        elif self.direction.lower() == 'вверх':
            self.y += abs(go)
            self.money += go * self.number_of_passengers
            print('Двигаемся вверх на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
            print('Количество денег: ' + str(self.money))
        elif self.direction.lower() == 'вниз':
            self.x -= abs(go)
            self.money += go * self.number_of_passengers
            print('Двигаемся вниз на ' + str(go) + ' единиц')
            print('Текущее положение: x - ' + str(self.x) + ' y - ' + str(self.y))
            print('Количество денег: ' + str(self.money))

bus = Bus(10, 10, 'вправо', 10)
bus.enter(15)
bus.exit(10)
bus.move(20)
bus.change_of_direction('Вниз')
bus.move(30)
auto = Auto(10, 30, 'Влево')
auto.move(45)
auto.change_of_direction('вверх')
auto.move(50)


