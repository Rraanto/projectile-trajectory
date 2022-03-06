import math as mt
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""
function get_equation(v0, h0, teta) 
function allowing to get the equation of a motion given the required data
@param v0 : velocity at t = 0
@param h0 : height at t = 0
@param teta : angle at t = 0
@return function om(x) = y (height of the object at 
"""
def get_equation(v0, h0, teta, g):
    def om(x):
        t = x / (v0 * mt.cos(teta))
        height = -0.5*g*t**2 + t * v0 * mt.sin(teta) + h0
        return max(0, height)
    return om


"""
function plot_trajectory()
allows to get a matplotlib.pyplot figure given an equation of a movement represented by a function f
@param f : function f(x) to display
@param a : beginning of the interval (0 by default)
@param b : end of the interval (0 by default)
@param checkpoints : number of slices of the interval (the more the slices the smoother the curve but the less fast the execution)
@param figure : figure where to plot the data

conditions : 
    f : continuous on [a, b]
    b > a
    checkpoints >= 2
"""
def plot_trajectory(f, figure=None, a=0, b=1, checkpoints=100, show_max=False):
    if figure is None:
        raise Exception("plot_trajectory : argument figure cannot be NULL")    
    
    # the datasets of the function
    x = np.linspace(a, b, checkpoints)
    y = [f(i) for i in x]

    # Adding the subplot 
    plot1 = figure.add_subplot(111)

    # plotting the graph
    plot1.plot(x, y, "b.")
    plot1.plot([0 for i in y], y, "k-")
    plot1.plot(x, [0 for i in x], "k-")


# tests 
if __name__ == "__main__" : 
    v0, h0, teta, g = 5, 4, 2*(mt.pi)*45/360, 9.81
    f = get_equation(v0, h0, teta, g)
    window = tk.Tk()
    
    fig = Figure()    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().pack()
    
    plot_trajectory(f, figure=fig, b=5, checkpoints=100)
    window.mainloop()
