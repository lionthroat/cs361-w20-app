##########################################################################
#   Program: To Do List
#   Summary:  This to do list allows a user to keep track of their to do
#       items.  It can allow the user to add or remove items, and set the
#       item's title and priority status.
##########################################################################

from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
import calendar as cal
# from functools import partial
from datetime import datetime
# import time
import json

import taskList
import menuBar
##need to import whatever file is created for viewability here


def main():
    root = tk.Tk()
    root.title('~ CS 361 Final Project ~')

    # Set window geometry
    w = '800'
    h = '710'
    root.geometry('{}x{}'.format(w, h))
    root.configure(background='#282a36')
    # Application Menu Bar
    menuBar = tk.Menu(root)
    root.configure(menu=menuBar) # Add menuBar to root.
main()
