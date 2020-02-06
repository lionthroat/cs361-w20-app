import tkinter as tk
import sys

from menu import MenuBar

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)      # root tk instance
        self.title("Sandbox example: Integrating Tkinter GUI elements as classes") # title of our master widget
        self.geometry("800x300")  # root window size
        menubar = MenuBar(self)   # create menu bar instance
        self.config(menu=menubar) # add menu bar to app

if __name__ == "__main__":
    app=App()      # our App class instantiates the GUI interface and functionality
    app.mainloop() # we've seen this as root.mainloop() before
