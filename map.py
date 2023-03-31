import numpy as np
import os
from tools import convertContentToFloat

CWD = os.getcwd()
FILE_PATH = f"{CWD}\軌道座標點.txt"

class Map:
    def __init__(self):
        self.map_points = self.loadMapFile(FILE_PATH)
        self.end_rectangle = self.map_points[1:3]
        self.map_line_equation = np.array([[1,0,-6],
                                            [0,1,22],
                                            [1,0,18],
                                            [0,1,50],
                                            [1,0,30],
                                            [0,1,10],
                                            [1,0,6],
                                            [0,1,-3]])
    
    def loadMapFile(self, file_path):
        f = open(file_path, mode='r')
        file = f.read().split('\n')
        mapdata = [convertContentToFloat(file_content.split(',')) for file_content in file if file_content != '']    
        return mapdata
    
    def isPointsInEnd(self, x, y, r):
        if y >= self.end_rectangle[1][1] and x >= self.end_rectangle[0][0]+r and x <= self.end_rectangle[0][1]-r:
            return True
        return False
    
    def getSensorDistenceOnMapLine(self, car_x, car_y, sensor_parameter, horizental_line, direction):
        points = []
        for line in self.map_line_equation:
            intersection = []
            if sensor_parameter[0] == 0:
                if line[0] == 1:
                    intersection = [line[2], car_y]
                else:
                    continue
            elif sensor_parameter[1] == 0:
                if line[1] == 1:
                    intersection = [car_x, line[2]]
                else:
                    continue
            else:
                if line[0] == 1:
                    intersection = [line[2],(-sensor_parameter[0]*line[2]-sensor_parameter[2])/sensor_parameter[1]]
                elif line[1] == 1:
                    intersection = [(-sensor_parameter[1]*line[2]-sensor_parameter[2])/sensor_parameter[0],line[2]]
            
            #check intersection is in front
            if direction == "Positive":
                if horizental_line[0]*intersection[0]+horizental_line[1]*intersection[1]+horizental_line[2] >= 0:
                    points.append(intersection)
            else:
                if horizental_line[0]*intersection[0]+horizental_line[1]*intersection[1]+horizental_line[2] < 0:
                    points.append(intersection)
        points = np.array(points)
        
        distence = 0
        for p in points:
            if p[1]==22 and p[0] > 18 and p[0] < 30:
                continue
            elif p[0]==18 and p[1] > 10 and p[1] < 22:
                continue
            elif p[1]==10 and p[0] > -6 and p[0] < 6:
                continue
            elif p[0]==6 and p[1] > 10 and p[1] < 22:
                continue
            else:
                if distence==0 or distence>((p[0]-car_x)**2+(p[1]-car_y)**2)**0.5:
                    distence = ((p[0]-car_x)**2+(p[1]-car_y)**2)**0.5
                else:
                    continue
        return distence
        