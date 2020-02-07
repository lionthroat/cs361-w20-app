from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import time
import json

import sys
sys.path.insert(0, 'themes/style.py')
import style

# our classes
from menu import AppMenuBar
from notebook import AppTabs
from calendar import AppCalendar
from todo import *
#from style import * # (Need all because of color palette)

import file

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)      # root tk instance

        # the cosmetic stuff
        self.title(" ~ CS 361 App ~ ")
        self.geometry("800x710")
        self.config(background='#282a36')
        theme = AppStyle(self)

        # the menu bar
        menubar = AppMenuBar(self)   # create menu bar instance
        self.config(menu=menubar) # add menu bar to app

        # the notebook tabs
        tabs = AppTabs(self)

if __name__ == "__main__":
    app=App()      # our App class instantiates the GUI interface and functionality
    app.mainloop() # we've seen this as root.mainloop() before
