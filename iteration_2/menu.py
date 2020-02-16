############################################################################
# File: menu.py
# Function: This creates the menu bar at the top of the program.  It contains
#   all methods for the menu dropdown options.
# Last Modified: 16 February 2020
##############################################################################
import tkinter as tk
import sys

class AppMenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

    def quit(self):
        sys.exit(0)
