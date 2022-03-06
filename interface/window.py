import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import *

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
    def __init__(self, title="Window", height=601, width=962):
        # basic setup
        super().__init__()
        self.height = height
        self.width = width
        self.title(title)

        self.geometry(f'{width}x{height}')

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(column=1, row=1, sticky='W')

        self.left_frame = tk.Frame(self)
        self.left_frame.grid(column=2, row=1, sticky='E')

        self.lbl = tk.Label(self.right_frame, text="Data at t=0")
        self.lbl.grid(column=1, row=1, pady=5, padx=10, sticky='NW')

        self.lbl = tk.Label(self.right_frame, text="Velocity")
        self.lbl.grid(column=0, row=3, pady=2, padx=10, sticky='NW')
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

        self.lbl = tk.Label(self.right_frame, text="Angle")
        self.lbl.grid(column=0, row=4, pady=2, padx=10, sticky='NW')
        self.vitesse = tk.Entry(self.right_frame, width=10)
        self.vitesse.grid(column=1, row=4, pady=2, padx=10, sticky='NW')
        self.comboExample = ttk.Combobox(self.right_frame,
                                        values=[
                                            "teta",
                                            "degree"], width=5)
        self.comboExample.grid(column=2, row=4, pady=2, sticky='NW')
        self.comboExample.current(1)

        self.lbl = tk.Label(self.right_frame, text="Position")
        self.lbl.grid(column=0, row=5, pady=2, padx=10, sticky='NW')
        self.vitesse = tk.Entry(self.right_frame, width=10)
        self.vitesse.grid(column=1, row=5, pady=2, padx=10, sticky='NW')

        self.btn = tk.Button(self.right_frame, text=" View", width=20)
        self.btn.grid(column=1, row=6, pady=10, sticky='NW')

        self.cnv = tk.Canvas(self.left_frame, bg='white', bd=1, width=940, height=601, highlightbackground="grey")
        self.cnv.grid(column=3, row=3, columnspan=3, rowspan=3, pady=20, padx=20, sticky='NE')

>>>>>>> 14f9e90863d30afb29066f5316fb859084575636
        # creating all the necessary widgets (labels, buttons, views, etc...)

        # the matplotlib figure to put on the canva
        """self.fig = Figure(figsize=(10, 10), dpi=100)
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.plot(0, 0, "ko")

        # the tkinter.canva element containing the matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(column=3, row=8)
        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().grid(column=3, row=8)
"""

>>>>>>> f33ded060da27fe0fd37b176dcce48c16b3587a2
# testings 
if __name__ == "__main__":
    x, y = 601, 962
    my_window = Window(height=x, width=y)
    my_window.afficher_dimension()
    my_window.mainloop()
