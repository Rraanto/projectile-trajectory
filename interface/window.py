import tkinter as tk

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
=======
        # creating all the necessary widgets (labels, buttons, views, etc...)

        #first step with git

>>>>>>> f33ded060da27fe0fd37b176dcce48c16b3587a2
# testings 
if __name__ == "__main__": 
    x, y = 601, 962
    my_window = Window(height=x, width=y)
    my_window.afficher_dimension()
    my_window.mainloop()
