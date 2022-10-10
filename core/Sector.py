from core.Object2D import Object2D
import numpy as np


class Sector(Object2D):
    def __init__(self, x=0, y=0, radius=0, theta_start=0, theta_stop=0, elliptical=0, layer=0,
                 number_of_points=100):
        super().__init__()
        self.name = 'Sector'
        self.layer = layer
        self.x = x
        self.y = y
        self.radius = radius
        self.theta_start = theta_start
        self.theta_stop = theta_stop
        self.elliptical = elliptical
        self.position = self.draw_sector(number_of_points)

    def draw_sector(self, number_of_points):
        points = []
        self.angle = self.theta_stop - self.theta_start
        for i in range(number_of_points + 1):
            points.append([self.x + self.radius * np.sin(self.angle * i / number_of_points + self.theta_start),
                           self.y + (self.radius + self.elliptical / 2) * np.cos(
                               self.angle * i / number_of_points + self.theta_start)])
        points.append([self.x, self.y + self.elliptical / 2])
        points.append([self.x, self.y - self.elliptical / 2])
        return points
