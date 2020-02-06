from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from style import *

# TASK LIST
taskList = []
taskList.append({'task': 'Feed Cat', 'priority': 'High'})
taskList.append({'task': 'Mow Lawn', 'priority': 'Medium'})
taskList.append({'task': 'Go to DMV', 'priority': 'Low'})

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

        # Button: add new task
        newTask = ttk.Button(showToDo, text='+', command=self.add_task, style='newTask.TButton')
        newTask.grid(row=2, column=2)

        print(taskList)
        # Box to display tasks
        taskBox = ttk.Treeview(showToDo)
        taskBox['columns']=('task','priority')
        taskBox['show'] = 'headings' # without this, there is empty 1st col
        taskBox.column('task', width=470, minwidth=100)
        taskBox.column('priority', width=200, minwidth=100, stretch=tk.NO)
        taskBox.heading('task',text='Task',anchor=tk.W)
        taskBox.heading('priority', text='Priority',anchor=tk.W)

        taskBox.grid(columnspan=3)
        self.show_tasks

        # Button: remove task
        remTask = ttk.Button(showToDo, text='-', command=self.rem_task, style='newTask.TButton')
        remTask.grid(row=10, column=2)

    def add_task(self):
        # get the inputs
        taskList.append({
            'task': inputTask.get(),
            'priority': inputTaskPriority.get()
        })

        # reset input boxes/selections
        inputTask.delete(0, 'end')
        inputTaskPriority.current(0)

        # reset display
        self.show_tasks

    def rem_task(self):
    	# select current highlighted item and get task and priority
    	i = taskBox.focus()
    	task_item = taskBox.item(i)['values'][0]
    	task_priority = taskBox.item(i)['values'][1]

    	# find index for item to be removed
    	j = 0
    	for i in taskList:
    		if ((i['task'] == task_item) and (i['priority'] == task_priority)):
    			index = j
    		j+=1

    	# pop the item from the list
    	taskList.pop(index)
    	print(taskList)
    	# reset display
    	self.show_tasks

    def show_tasks(self):
        # empty treeview taskBox completely
        taskBox.delete(*taskBox.get_children())

        # reprint all items in taskList to taskBox
        for i in range(len(taskList)):
            task_item = taskList[i]['task']
            task_priority = taskList[i]['priority']
            taskBox.insert('', 'end', values=(task_item, task_priority))
        return
