class Robot:
    def __init__(self, x, y, direction=None):
        self.x, self.y, self.direction = x, y, direction

    def avancer(self):
        if self.direction == 'N': self.y += 1
        elif self.direction == 'S': self.y -= 1
        elif self.direction == 'E': self.x += 1
        elif self.direction == 'O': self.x -= 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation :
robot = Robot(0, 0, 'N')
robot.avancer()
print(robot.position())  # Affiche: (0, 1)

robot.direction = 'E'
robot.avancer()
print(robot.position())  # Affiche: (1, 1)
