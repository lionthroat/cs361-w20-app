############################################################
# Spike 1: Testing Front-End To-Do List Design
# Oregon State University, Winter 2020: CS 361, Week 4
# Agile Project: Release Cycle 1
#
# Pair Programming:
# Heather DiRuscio & Paige Enoch
# @wrongenvelope and @paigeenoch
#
# January 20, 2020
############################################################

# Sample To-Do List Code Source: https://www.youtube.com/watch?v=OAHLwtmdqUk

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

#function to add a task
#currently adds a task to the dictionary of tasks and prints. Also adds to the listbox and displays
def add_task():
	# get the inputs
	sample_list[input_task_name.get()] = input_task_priority.get()
	task_box.insert(END, input_task_name.get() + '\t' + '\t' + input_task_priority.get() + '\n')
	# reset input boxes/selections
	input_task_name.delete(0, 'end')
	input_task_priority.current(0)

	print(sample_list)

def rem_task():
    return

#name of window
root = tk.Tk()

#set window geometry
w = '300'
h = '400'
root.geometry('{}x{}'.format(w, h))

#generate sample list as a starting point
sample_list = {}
sample_list["Feed Cat"] = "High"
sample_list["Mow Lawn"] = "Low"
sample_list["Go to DMV"] = "Low"

#create window label
lbl_title = tk.Label(root, text="To-Do List", bg="white")
lbl_title.grid(row=0,column=0, sticky=W)

#create box to display tasks
task_box = Text(root,width = 25,height=10)
task_box.grid(row=2,column=0)

#insert a title into the taskbox
task_box.insert(END, 'Task' + '\t' + '\t' + 'Priority' + '\n')

#insert each task into the taskbox
for i in sample_list:
	task_box.insert(END, i + '\t' + '\t' + sample_list[i] + '\n')

#create labels for text entry fields
tk.Label(root, text="New Task Name:", bg="white").grid(row=7, sticky=W)
tk.Label(root, text="New Task Priority:", bg="white").grid(row=9, sticky=W)

#create text entry fields
input_task_name = tk.Entry(root)
input_task_name.grid(row = 8, column = 0)

# priority selection field
input_task_priority = Combobox(root, values = ["", "High", "Low"])
input_task_priority.grid(row = 10, column = 0)
input_task_priority.current(0)

#create button to add new task
add_new_button = Button(root, text="Add New Task", command=add_task)
add_new_button.grid(row=11, sticky=W)

root.mainloop()
