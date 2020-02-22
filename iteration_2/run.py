##########################################################################
#   Program: To Do List
#   Summary:  This to do list allows a user to keep track of their to do
#       items.  It can allow the user to add or remove items, and set the
#       item's title and priority status.
#
# icons from https://icon-icons.com/pack/Vector-Flat-Gradient/2063
##########################################################################

import tkinter.ttk as ttk
import TaskListClass
from todoApp import *
from style import *
import sys
import time
import json

from menu import AppMenuBar
from calendarApp import AppCalendar
from notebook import AppTabs

class mainApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self) # root tk instance
		#### add here for whatever should be called from all the other files ####

		# the cosmetic stuff
		self.title(' Time.to ') # main window title
		self.iconbitmap('images/coffee.ico') # coffee cup icon

		# Set window geometry
		w = '790'
		h = '720'
		self.geometry('{}x{}'.format(w, h))

		# Create theme set and apply default theme
		self.config(background='#FFFFFF')
		themes = AppStyle(self)

		# the menu bar
		menubar = AppMenuBar(self, themes)   # create menu bar instance
		self.config(menu=menubar) # add menu bar to app

		# the notebook tabs
		tabs = AppTabs(self)

if __name__ == "__main__":
	app=mainApp()      # our App class instantiates the GUI interface and functionality
	app.mainloop() # we've seen this as root.mainloop() before
