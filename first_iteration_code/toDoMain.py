##########################################################################
#   Program: To Do List
#   Summary:  This to do list allows a user to keep track of their to do
#       items.  It can allow the user to add or remove items, and set the
#       item's title and priority status.
##########################################################################

import tkinter.ttk as ttk
import taskList
from todo import *
##need to import whatever file is created for viewability here


def main():
    ####add here for whatever should be called from all the other files

	######################################################
	# tk instantiation
	# since Tk() is meant to be called once per program,
	# all elements need to belong to or be indirectly linked
	# to root to show up in the program
	root = tk.Tk()

	# Window title: think .wm_title('<title>') does same thing?
	root.title('~ CS 361 Final Project ~') # anyone have a good name yet??

	# Set window geometry
	w = '800'
	h = '710'
	root.geometry('{}x{}'.format(w, h))

	# App background color
	root.configure(background='#282a36')
	######################################################

	#showToDo = ttk.LabelFrame(todo_widget, style='taskBlock.TLabelframe', width=670)
	showToDo = AppToDoList(root)
	showToDo.grid(row=1)

	root.mainloop()

main()
