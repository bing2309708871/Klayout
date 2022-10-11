from core.Object2D import Object2D
import numpy as np

class Ring(Object2D):
    def __init__(self, x=0, y=0, radius=0, think=0, theta_start=0, theta_stop=0, port_type=0,elliptical=0,number_of_points=100,layer=0):
        super().__init__()
        self.name = 'Ring'
        self.x = x
        self.y = y
        self.radius = radius
        self.think = think
        self.theta_start = theta_start
        self.theta_stop = theta_stop
        self.port_type = port_type
        self.elliptical = elliptical
        self.position = self.draw_ring(number_of_points)
        self.layer = layer

    def draw_ring(self, number_of_points):
        points = []
        self.angle = self.theta_stop - self.theta_start
        if self.port_type == 0:
            for i in range(number_of_points + 1):
                points.append([
                    self.x + (self.radius + self.think / 2) * np.sin(self.angle * i / number_of_points + self.theta_start),
                    self.y + (self.radius + self.elliptical / 2 + self.think / 2) * np.cos(
                        self.angle * i / number_of_points + self.theta_start)])
            for i in range(number_of_points + 1):
                points.append([
                    self.x + (self.radius - self.think / 2) * np.sin(-self.angle * i / number_of_points + self.theta_stop),
                    self.y + (self.radius + self.elliptical / 2 - self.think / 2) * np.cos(
                        -self.angle * i / number_of_points + self.theta_stop)])
        else:
            for i in range(number_of_points + 1):
                points.append([
                    self.x + self.radius * np.sin(self.angle * i / number_of_points + self.theta_start) + self.think * np.sin(
                        (self.theta_start + self.theta_stop) / 2) / 2,
                    self.y + (self.radius + self.elliptical / 2) * np.cos(
                        self.angle * i / number_of_points + self.theta_start) + self.think * np.cos(
                        (self.theta_start + self.theta_stop) / 2) / 2])
            for i in range(number_of_points + 1):
                points.append([
                    self.x + self.radius * np.sin(-self.angle * i / number_of_points + self.theta_stop) - self.think * np.sin(
                        (self.theta_start + self.theta_stop) / 2) / 2,
                    self.y + (self.radius + self.elliptical / 2) * np.cos(
                        -self.angle * i / number_of_points + self.theta_stop) - self.think * np.cos(
                        (self.theta_start + self.theta_stop) / 2) / 2])
        return points
