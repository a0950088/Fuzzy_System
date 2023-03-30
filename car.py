import math as m

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
        self.front_sensor = 0
        self.right_sensor = 0
        self.left_sensor = 0
        
    def setPhi(self):
        self.phi %= 360
        if self.phi > MAX_PHI:
            self.phi -= (MAX_PHI - MIN_PHI)
    
    def changePosition(self):
        self.setPhi()
        r_theta = m.radians(self.theta)
        r_phi = m.radians(self.phi)
        r_phi -= m.asin((2*m.sin(r_theta))/(self.radius*2))
        self.x += m.cos(r_phi+r_theta) + m.sin(r_theta)*m.sin(r_phi)
        self.y += m.sin(r_phi+r_theta) - m.sin(r_theta)*m.cos(r_phi)
        self.phi = m.degrees(r_phi)