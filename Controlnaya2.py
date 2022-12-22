class Robot():
    def __init__(self, x, y):
        self.x = x
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

robot = Robot(23, 76)
print(robot.move('sssssweeeeeeewwwwwwNNNEEEEEEEEwwwwww'))
