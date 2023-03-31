import math as m
import numpy as np
from tools import getLinearEquation

MAX_THETA = 40
MIN_THETA = -40
MAX_PHI = 270
MIN_PHI = -90

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.phi = 90
        self.radius = 3
        self.theta = 0 # Car turning angle
        self.front_sensor = np.zeros(3)
        self.right_sensor = np.zeros(3)
        self.left_sensor = np.zeros(3)
        self.horizental_line = np.zeros(3)
        self.horizental_direction = "Positive"
        
    def setPhi(self, phi):
        phi %= 360
        if phi < MIN_PHI:
            phi += (MAX_PHI - MIN_PHI)
        return phi
    
    def changePosition(self):
        self.phi = self.setPhi(self.phi)
        r_theta = m.radians(self.theta)
        r_phi = m.radians(self.phi)
        r_phi -= m.asin((2*m.sin(r_theta))/(self.radius*2))
        self.x += m.cos(r_phi+r_theta) + m.sin(r_theta)*m.sin(r_phi)
        self.y += m.sin(r_phi+r_theta) - m.sin(r_theta)*m.cos(r_phi)
        self.phi = m.degrees(r_phi)
    
    def getPosition(self):
        return [self.x, self.y, self.phi]
    
    def setTheta(self, theta):
        self.theta = theta
        
    def computeLines(self, phi):
        r_phi = m.radians(phi)
        circle_point_x = self.radius*m.cos(r_phi) + self.x
        circle_point_y = self.radius*m.sin(r_phi) + self.y
        line_parameter = getLinearEquation(self.x, self.y, circle_point_x, circle_point_y)
        return line_parameter, circle_point_x, circle_point_y
    
    def setSensorsAndHorizentalLine(self):
        self.front_sensor, front_x, front_y = self.computeLines(self.phi)
        self.right_sensor, _, _ = self.computeLines(self.setPhi(self.phi-45))
        self.left_sensor, _, _ = self.computeLines(self.setPhi(self.phi+45))
        self.horizental_line, _, _ = self.computeLines(self.setPhi(self.phi+90))
        self.horizental_direction = "Positive" if self.horizental_line[0]*front_x+self.horizental_line[1]*front_y+self.horizental_line[2] >= 0 else "Negative"        
    
    def run(self):
        # fuzzy system change theta
        self.setTheta(self.theta)
        self.changePosition()
        self.setSensorsAndHorizentalLine()
        print(self.front_sensor)
        print(self.right_sensor)
        print(self.left_sensor)
        print(self.horizental_line)
        print(self.horizental_direction)
        print(self.x, self.y)