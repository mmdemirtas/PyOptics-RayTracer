import numpy as np

class Ray:

    def __init__(self, position, direction):

        self.position = np.array(position, dtype=float)

        direction = np.array(direction, dtype=float)

        self.direction = direction / np.linalg.norm(direction)

        self.history = [self.position.copy()]

    def propagate(self, distance):

        self.position += self.direction * distance

        self.history.append(self.position.copy())
