import numpy as np

def convertContentToFloat(contents): # 轉換.txt檔案資料
    for content in range(len(contents)):
        contents[content] = float(contents[content])
    return contents

def getLinearEquation(x1,y1,x2,y2): # 計算兩點的方程式 ax+by+c=0
    decimal = 6
    a = (y2-y1)
    sign = -1 if a < 0 else 1
    a *= sign
    b = sign*(x1-x2)
    c = sign*((y1*x2) - (x1*y2))
    return np.array([round(a, decimal),round(b, decimal),round(c, decimal)])