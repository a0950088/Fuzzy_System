import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
from car import Car
from map import Map
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.front_distence = tk.StringVar()
        self.right_distence = tk.StringVar()
        self.left_distence = tk.StringVar()
        self.fig = Figure(figsize=(4,4))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        
    
    def start(self):
        self.root.title("HW1")
        self.root.geometry("450x700")
        self.draw()
        
        f = tkFont.Font(family='Ink Free')
        tk.Label(master=self.root).grid(row=9,column=0,columnspan=2)
        tk.Label(master=self.root).grid(row=9,column=2,columnspan=2)
        quit_btn = tk.Button(master=self.root, text="QUIT", command=self.quit,width=10,height=1,font=f)
        quit_btn.grid(row=9,column=4)
        tk.Label(master=self.root).grid(row=3,column=0)
        tk.Label(master=self.root).grid(row=4,column=0)

        tk.Label(master=self.root, text="Front Distence: ",font=f).grid(row=6,column=0,columnspan=2)
        tk.Label(master=self.root, textvariable=self.front_distence,font=f).grid(row=6,column=2,columnspan=4)
        tk.Label(master=self.root, text="Right Distence: ",font=f).grid(row=7,column=0,columnspan=2)
        tk.Label(master=self.root, textvariable=self.right_distence,font=f).grid(row=7,column=2,columnspan=4)
        tk.Label(master=self.root, text="Left Distence: ",font=f).grid(row=8,column=0,columnspan=2)
        tk.Label(master=self.root, textvariable=self.left_distence,font=f).grid(row=8,column=2,columnspan=4)

        self.root.mainloop()
    
    def draw(self):
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5,column=1,columnspan=5)

        
    def quit(self):
        self.root.quit()
        self.root.destroy()

gui = Gui()
gui.start()