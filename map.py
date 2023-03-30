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