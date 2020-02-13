from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial	# passing function arguments where syntactically not allowed
from TaskListClass import *


class AppToDoList(ttk.Label):
	def __init__(self, parent):
		ttk.Label.__init__(self) # instantiate ttk Notebook() widget
		showToDo = ttk.LabelFrame(self, style='taskBlock.TLabelframe', width=670)
		showToDo.grid(row=1)

		# Text entry box: add a task
		inputTask = ttk.Entry(showToDo, width=40, font=('Lucida Console', 11, 'bold'))
		inputTask.grid(row=2, column=0)

		# priority selection field
		inputTaskPriority = ttk.Combobox(showToDo, values = ['', 'High', 'Medium', 'Low'])
		inputTaskPriority.grid(row = 2, column=1)
		inputTaskPriority.current(0)

		# TASK LIST
		self.filepath = 'taskFile.json'
		mylist = TaskList()
		mylist.loadJSON(self.filepath)
		# mylist.printTasks()

		# Box to display tasks
		taskBox = ttk.Treeview(showToDo)
		taskBox['columns']=('task','priority')
		taskBox['show'] = 'headings' # without this, there is empty 1st col
		taskBox.column('task', width=470, minwidth=100)
		taskBox.column('priority', width=200, minwidth=100, stretch=tk.NO)
		taskBox.heading('task',text='Task',anchor=tk.W)
		taskBox.heading('priority', text='Priority',anchor=tk.W)

		taskBox.grid(columnspan=3)

		self.showTasks(taskBox, mylist)

		# Button: add new task
		newTask = ttk.Button(showToDo, text='+', command=partial(self.addTask, inputTask, inputTaskPriority, taskBox, mylist), style='newTask.TButton')
		newTask.grid(row=2, column=2)

		# Button: remove task
		remTask = ttk.Button(showToDo, text='-', command=partial(self.remTask, taskBox, mylist), style='newTask.TButton')
		remTask.grid(row=10, column=2)

# add task
	def addTask(self, inputTask, inputTaskPriority, taskBox, mylist):
		# get the inputs and add to the task list object
		mylist.addTaskToList(inputTask.get(), inputTaskPriority.get())
		# clear the input boxes/selections
		inputTask.delete(0, 'end')
		inputTaskPriority.current(0)

		# save changes to file and reset display
		mylist.saveToJSON(self.filepath)
		self.showTasks(taskBox, mylist)

# remove task
	def remTask(self, taskBox, mylist):
		# select current highlighted item and get task and priority
		i = taskBox.focus()
		taskItem = taskBox.item(i)['values'][0]
		taskPriority = taskBox.item(i)['values'][1]

		# pop the item from the list
		mylist.removeTaskFromList(taskItem, taskPriority)

		# save changes to file and reset display
		mylist.saveToJSON(self.filepath)
		self.showTasks(taskBox, mylist)

# show tasks: add all items from task list to the display object
	def showTasks(self, taskBox, mylist):
		# empty treeview taskBox completely
		taskBox.delete(*taskBox.get_children())

		# reprint all items in taskList to taskBox
		for i in range(mylist.getListSize()):
			taskItem = mylist.getTaskAt(i).getTitle()
			taskPriority = mylist.getTaskAt(i).getPriority()
			taskBox.insert('', 'end', values=(taskItem, taskPriority))
		return
