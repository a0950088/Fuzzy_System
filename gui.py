import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.font as tkFont
from car import Car
from map import Map
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.patches import Circle
matplotlib.use('TkAgg')

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.front_distence = tk.StringVar()
        self.right_distence = tk.StringVar()
        self.left_distence = tk.StringVar()
        self.fig = Figure(figsize=(4,4))
        self.ax = self.fig.add_subplot(111)
        self.ax.title.set_text('Map')
        self.ax.set_aspect(1)
        self.ax.set_xlim(-11,42)
        self.ax.set_ylim(-5,55)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.update_point = []
        self.update_distence = []

    def start(self):
        self.root.title("HW1")
        self.root.geometry("450x600")
        
        f = tkFont.Font(family='Ink Free')
        tk.Label(master=self.root).grid(row=9,column=0,columnspan=2)
        tk.Label(master=self.root).grid(row=9,column=2,columnspan=2)
        quit_btn = tk.Button(master=self.root, text="QUIT", command=self.quit,width=10,height=1,font=f)
        quit_btn.grid(row=9,column=4)
        tk.Label(master=self.root).grid(row=3,column=0)
        tk.Label(master=self.root).grid(row=4,column=0)

        tk.Label(master=self.root, text="Front Distence: ", font=f).grid(row=6,column=0,columnspan=2)
        tk.Label(master=self.root, textvariable=self.front_distence, font=f).grid(row=6,column=2,columnspan=4)
        tk.Label(master=self.root, text="Right Distence: ", font=f).grid(row=7,column=0,columnspan=2)
        tk.Label(master=self.root, textvariable=self.right_distence, font=f).grid(row=7,column=2,columnspan=4)
        tk.Label(master=self.root, text="Left Distence: ", font=f).grid(row=8,column=0,columnspan=2)
        tk.Label(master=self.root, textvariable=self.left_distence, font=f).grid(row=8,column=2,columnspan=4)
    
    def draw(self):
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5,column=1,columnspan=5)

    def draw_map(self, points, end_points):
        end_x = [end_points[0][0], end_points[1][0], end_points[1][0], end_points[0][0], end_points[0][0]]
        end_y = [end_points[0][1], end_points[0][1], end_points[1][1], end_points[1][1], end_points[0][1]]
        self.ax.plot(end_x, end_y)
        map_point_x, map_point_y = zip(*points)
        self.ax.plot(map_point_x, map_point_y)
        self.draw()
    
    def draw_car(self):
        p = self.update_point.pop(0)
        d = self.update_distence.pop(0)
        self.front_distence.set(str(d[0]))
        self.right_distence.set(str(d[1]))
        self.left_distence.set(str(d[2]))
        car_circle = Circle(xy=(p[0], p[1]), radius=3, alpha=0.5)
        self.ax.add_artist(car_circle)
        self.draw()
        if self.update_point != []:
            self.root.after(100, self.draw_car)
        
    def quit(self):
        self.root.quit()
        self.root.destroy()
        
def main():
    map = Map()
    car = Car()
    gui = Gui()
    points = []
    distence_list = []
    # initialize
    gui.start()
    # run
    while True:
        car.run()
        front_distence = map.getSensorDistenceOnMapLine(car.x, car.y, car.front_sensor, car.horizental_line, car.horizental_direction)
        right_distence = map.getSensorDistenceOnMapLine(car.x, car.y, car.right_sensor, car.horizental_line, car.horizental_direction)
        left_distence = map.getSensorDistenceOnMapLine(car.x, car.y, car.left_sensor, car.horizental_line, car.horizental_direction)
        car.setSensorsData(front_distence, right_distence, left_distence)
        points.append(car.getPosition()[:2])
        distence_list.append([front_distence, right_distence, left_distence])
        if map.isPointsInEnd(car.x, car.y, car.radius):
            print("Success!")
            break
        elif front_distence<3 or right_distence<3 or left_distence<3:
            print("Failed!")
            break
    gui.update_point = points
    gui.update_distence = distence_list
    plt.ion()
    gui.draw_map(map.map_points[3:], map.end_rectangle)
    gui.draw_car()
    plt.ioff()
    gui.root.mainloop()
    
if __name__ == "__main__":
    main()