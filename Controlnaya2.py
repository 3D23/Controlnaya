class Robot():
    def __init__(self, x, y):
        while not(x >= 0 and x <= 100):
            x = int(input('Введите другое значение x: '))
        self.x = x
        while not(y >= 0 and y <= 100):
            y = int(input('Введите другое значение y: '))
        self.y = y

    def move(self, s):
        for i in s:
            if i.lower() == 'n' and self.y != 100:
                self.y += 1
            elif i.lower() == 's' and self.y != 0:
                self.y -= 1
            elif i.lower() == 'e' and self.x != 100:
                self.x += 1
            elif i.lower() == 'w' and self.x != 0:
                self.x -= 1
        return [self.x, self.y]
x = int(input('Введите начальное положение робота по координате x: '))
y = int(input('Введите начальное значение робота по координате y: '))
robot = Robot(x, y)
print(robot.move('wweEEESssNNNNNN'))
