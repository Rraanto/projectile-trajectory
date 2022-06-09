import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import *
import engine

"""
Class Window 
inherits tkinter.Tk()
instance of which will serve as the main window of the application
"""

class Window(tk.Tk):
    """
    initializer function 
    @param height : default to 601, allows to create instance of the class with different height
    @param width : default to 962, allows to create instance of the class with different width
    """
    def __init__(self, title="Window", height=680, width=1306):
        # basic setup
        super().__init__()
        self.height = height
        self.width = width
        self.title(title)

        self.geometry(f'{width}x{height}')
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(column=1, row=1, sticky='W')

        self.left_frame = tk.Frame(self)
        self.left_frame.grid(column=2, row=1, sticky='E')

        self.title_lbl = tk.Label(self.right_frame, text="Data at t=0")
        self.title_lbl.grid(column=1, row=1, pady=5, padx=10, sticky='NW')

        self.vitesse_lbl = tk.Label(self.right_frame, text="Velocity")
        self.vitesse_lbl.grid(column=0, row=3, pady=2, padx=10, sticky='NW')
        self.vitesse = tk.Entry(self.right_frame, width=10)
        self.vitesse.grid(column=1, row=3, pady=2, padx=10, sticky='NW')
        self.comboExample = ttk.Combobox(self.right_frame,
                                    values=[
                                        "m/s",
                                        "km/h",
                                        "mi/s",
                                        "mph"], width=5)
        self.comboExample.grid(column=2, row=3, pady=2, sticky='NW')
        self.comboExample.current(1)

        self.angle_lbl = tk.Label(self.right_frame, text="Angle")
        self.angle_lbl.grid(column=0, row=4, pady=2, padx=10, sticky='NW')
        self.angle = tk.Entry(self.right_frame, width=10)
        self.angle.grid(column=1, row=4, pady=2, padx=10, sticky='NW')
        self.comboExample = ttk.Combobox(self.right_frame,
                                        values=[
                                            "teta",
                                            "degree"], width=5)
        self.comboExample.grid(column=2, row=4, pady=2, sticky='NW')
        self.comboExample.current(1)

        self.position_lbl = tk.Label(self.right_frame, text="Position")
        self.position_lbl.grid(column=0, row=5, pady=2, padx=10, sticky='NW')
        self.position = tk.Entry(self.right_frame, width=10)
        self.position.grid(column=1, row=5, pady=2, padx=10, sticky='NW')

        self.btn = tk.Button(self.right_frame, text=" VIEW ", width=20, command=self.view)
        self.btn.grid(column=1, row=6, pady=10, sticky='NW')

        self.cnv = tk.Canvas(self.left_frame, bg='white', bd=1, width=940, height=601, highlightbackground="grey")  
        
        self.fig = Figure()
        self.plot_canva = FigureCanvasTkAgg(self.fig, master=self.cnv)
        self.plot_canva.draw()
        self.plot_canva.get_tk_widget().pack()
        
        self.cnv.grid(column=3, row=3, columnspan=3, rowspan=3, pady=20, padx=20, sticky='NE')
        
    def view(self):
        """
        plots the trajectory of the motion given: 
        the movement equation 
        the figure on which to draw
        the number of checkpoints (default to 100)
        """
        v0 = float(self.vitesse.get())
        h0 = float(self.position.get())
        teta = float(self.angle.get())
        g = 9.81
        equation = engine.functions.get_equation(v0, h0, teta, g)
        self.plot_canva.draw()
        self.plot_canva.get_tk_widget().pack()
        engine.functions.plot_trajectory(equation, self.fig)
                      
# testings 
if __name__ == "__main__":
    my_window = Window()
    equation = engine.functions.get_equation(5, 5, 45, 9.81)
    my_window.update()
    my_window.mainloop()
