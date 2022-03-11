import math as mt
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


"""
function prime(f):
function allowing to get the derivative of a function using the limit calculation 
@param f: function to derivate
@return function fp = df/dx

"""
def prime(f):
    h = 0.000000000001
    def fp(x):
        return (f(x+h) - f(x)) / (h)
    return fp

"""function zero(f)
function allowing to search for the zero of a function using Newton's algorithm 
@param f : function to search zero of
@param precision : precision (how close to 0 should the function search)
@param a : starting point of the search
"""
def zero(f, precision, start):
    while abs(f(start)) > precision:
        # tweaking Newton's algorithm to calculate only upwards (adapted for a physics search)
        start = start + (f(start)) / (prime(f))(start)
    return start


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
        # considering the object cannot go under the level 0, the value of the height is 
        # the max between 0 and the altitude coordinate
        return max(0, height)
    return om


"""
function plot_trajectory()
allows to get a matplotlib.pyplot figure given an equation of a movement represented by a function f
@param f : function f(x) to display
@param checkpoints : number of slices of the interval (the more the slices the smoother the curve but the less fast the execution)
@param figure : figure where to plot the data

conditions : 
    f : continuous on [a, b]
    b > a
    checkpoints >= 2
"""


def plot_trajectory(f, figure=None, checkpoints=100, show_max=False):
    if figure is None:
        raise Exception("plot_trajectory : argument figure cannot be NULL")
    
    # get the farthest distance (integer) the object goes 
    max_x = mt.ceil(zero(f, 0.01, 0.1))

    # the datasets of the function
    x = np.linspace(0, max_x, checkpoints)
    y = [f(i) for i in x]

    # Adding the subplot
    plot1 = figure.add_subplot(111)
    
    # plotting the graph
    plot1.plot(x, y, "b.")
    plot1.plot([0 for i in y], y, "k-")
    plot1.plot(x, [0 for i in x], "k-")


# tests
if __name__ == "__main__":
    v0 = float(input("Enter velocity  (m/s) : "))
    h0 = float(input("Enter height  (m) : "))
    teta = 2*mt.pi*(float(input("Enter angle  (deg): ")))/360
    g = 9.81
    f = get_equation(v0, h0, teta, g)
    window = tk.Tk()

    fig = Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().pack()

    plot_trajectory(f, figure=fig, checkpoints=100)
    window.mainloop()   
