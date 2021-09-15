

class Rocket():
    def __init__(self, x_pos=0, y_pos=0, height=200):
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
    def move_rocket(self):
        self.x_pos += 10
        self.y_pos += 30

rocket1 = Rocket(10,30)
for i in range(5):
    print(rocket1.x_pos)
    print(rocket1.y_pos)
    rocket1.move_rocket()


