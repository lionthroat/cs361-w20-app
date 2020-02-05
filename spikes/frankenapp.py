from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
import calendar as cal
from functools import partial
from datetime import datetime
import time
import json

######################################################
class ItemsForToDo:
    def __init__(self, titleOfToDo, priorityStatus):
        self.__title = titleOfToDo
        self.__priority = priorityStatus
    def getTitle(self):
        return self.__title
    def getPriority(self):
        return self.__priority
    def setTitle(self, titleToSet):
        self.__title = titleToSet
    def setPriority(self, priorityToSet):
        self.__priority = priorityToSet

class ToDoList:
    def __init__(self):
        self.__listOfTasks = []
    def addToList(self, itemToAdd):
        self.__listOfTasks.append(itemToAdd)
    def saveToFile(self, fileName):
        outputFile = open(fileName, 'w')
        formattedObj = []
        for item in self.__listOfTasks:
            newDict = {}
            newDict['title'] = item.getTitle()
            newDict['priority'] = item.getPriority()
            formattedObj.append(newDict)
        jsonString = json.dumps(formattedObj)
        outputFile.write(jsonString)
        outputFile.close()
    def loadFromFile(self, fileName):
        inputFile = open(fileName, 'r')
        line = inputFile.readline()
        jsonObj = json.loads(line)
        for item in jsonObj:
            title = item['title']
            priority = item['priority']
            newItem = ItemsForToDo(title, priority)
            self.addToList(newItem)
        inputFile.close()
    def appendToFile(self, itemToAdd, fileName):
        self.addToList(itemToAdd)
        self.saveToFile(fileName)

def main():
    sampleList = ToDoList()
    sampleList.loadFromFile('testFile.json')
    thirdSampleItem = ItemsForToDo('feed fish', 'high')
    sampleList.addToList(thirdSampleItem)
    sampleList.saveToFile('testFile2.json')

main()
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
# MAIN MENU BAR
menuBar = tk.Menu(root)

# dummy function for now
def nada():
	return

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New', command=nada)
fileMenu.add_command(label='Open', command=nada)
fileMenu.add_command(label='Save', command=nada)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)
menuBar.add_cascade(label='File', menu=fileMenu)

helpMenu = tk.Menu(menuBar, tearoff=0)
helpMenu.add_command(label='Help', command=nada)
helpMenu.add_command(label='About', command=nada)
menuBar.add_cascade(label='Info', menu=helpMenu)

root.configure(menu=menuBar) # Add menuBar to root.
###########################################################

###########################################################
# STYLES

# ttk's Style() method is meant to separate cosmetic attributes from functional
# ones. the names given for a label style you create MUST be in the format of
# '<NAME>.TLabel' (same for buttons, needs to be <NAME>.TButton) or the whole
# thing breaks. however, you can create as many button or label styles in one
# ttk.Style() object as you want.

style = ttk.Style()

holo_green = '#d2ffd2'
monster_green = '#50fa7b'
dk_blue_grey='#282a36'
med_blue_grey = '#44475a'
lt_med_blue_grey = '#515366'
lt_grey = '#f8f8f2'
neon_yellow = '#f1fa8c'
lt_red = '#ff5555'
cyan = '#8be9fd'

style.theme_create('dracula', parent='alt', settings=
	{
	    'TNotebook': {
			'configure': {
				'tabmargins': [2, 5, 2, 0],
				'background': dk_blue_grey, # tab bar bg color
				'relief': 'flat'
			}
		},
	    'TNotebook.Tab': {
	        'configure': {
				'padding': [50, 10], # [x-padding, y-padding for tab labels]
				'background': holo_green, # bg for deselected tab labels
				'foreground': med_blue_grey, # text color for tabs
				'font': ('Lucida Console', 11), # example: ('Arial', 12, 'bold')
				'focuscolor': med_blue_grey
			},
	        'map': {
				'background': [('selected', med_blue_grey)], # selected tab bg color
				'foreground': [('selected', monster_green)], # text color for selected tabs
	            'expand': [('selected', [1, 1, 1, 0])], # what is this??
			}
		},
		'TLabel': {
			'configure': {'background': med_blue_grey, 'foreground': lt_grey}
		},
		'TFramelabel': {
			'configure': {'background': dk_blue_grey, 'foreground': lt_grey}
		},
		'TButton': {
			'configure': {
				'background': lt_med_blue_grey, # default button bg color
				'foreground': lt_grey,
				'focuscolor': lt_med_blue_grey,
			},
			'map': {
		    	'foreground': [('pressed', med_blue_grey), ('active', dk_blue_grey)],
		    	'background': [
					('pressed', '!disabled', 'readonly', med_blue_grey),
					('active', holo_green)
				],
				'focuscolor': [
					('active', holo_green),
					('pressed', '!disabled', 'readonly', med_blue_grey)
				],
			}
		},
        'newTask.TButton': {
            'configure': {
                'padding': [40, 3],
                'background': cyan,
                'font': ('Lucida Console', 14, 'bold'),
                'relief': 'ridge',
                'borderwidth': 2,
            }
        },
        'Treeview': {
            'configure': {
                'background': lt_grey,
                'fieldbackground': lt_grey,
                'padding': [2,2]
            },
            'map': {
                'background': [
                    ('selected', cyan) # active item on to-do list
                ]
            }
        },
		'taskBlock.TLabelframe.Label': {
			'configure': {
				'background': med_blue_grey,
				'foreground': lt_grey,
				'font': ('Lucida Console', 11, 'bold'),
			}
		},
		'taskBlock.TLabelframe': {
			'configure': {
				'background': med_blue_grey,
				'foreground': med_blue_grey,
				'padding': [50, 50], # x and y padding that places the to-do list
			},
		},
        'TEntry': {
            'configure': {
                # 'fieldbackground': neon_yellow,
                'bordercolor': monster_green,
                'foreground': dk_blue_grey,
                'padding': [5,5],
                'font': ('Lucida Console', 11, 'bold')
            }
        },
        'TCombobox': {
            'configure': {
                # 'fieldbackground': neon_yellow,
                'bordercolor': monster_green,
                'foreground': dk_blue_grey,
                'padding': [5,5],
                'font': ('Lucida Console', 11, 'bold')
            }
        },
		'monthBlock.TLabelframe.Label': { # style of month title
			'configure': {
				'background': med_blue_grey,
				'foreground': lt_grey,
				'font': ('Lucida Console', 11, 'bold')
			}
		},
		'monthBlock.TLabelframe': {
			'configure': {
				'background': med_blue_grey,
				'foreground': lt_grey,
				'padding': [15, 15], # x and y padding that places the calendar
			},
		},
		'monthBlock.TLabel': {
			'configure': {
				'background': med_blue_grey,
				'foreground': lt_grey
			},
		},
		'calNav.TLabelframe.Label': {
			'configure': {
				'background': med_blue_grey,
				'foreground': med_blue_grey,
			}
		},
		'calNav.TLabelframe': {
			'configure': {
				'background': med_blue_grey,
				'foreground': med_blue_grey,
				'padding': [10, 10] # position frame containing calendar navigation buttons
			}
		},
		'dayBlock.TLabelframe': {
			'configure': {
				'background': lt_med_blue_grey, # bg color for each day block
				# 'relief': 'ridge' # for different dayBlock border styles
				'labelmargins': 15 # tweak placement of calendar numbers
			}
		},
		'dayBlock.TLabelframe.Label': { # calendar numbers for each day
			'configure': {
				'background': lt_med_blue_grey, # color immediately surrounding num
				'foreground': lt_grey, # font color
			}
		},
		'dayBlock.TLabel': { # style of entries on a calendar day
			'configure': {
				'background': med_blue_grey,
			}
		},
		'nullDay.TLabel': {
			'configure': {
				'background': med_blue_grey,
			}
		}
	}
)
style.theme_use('dracula')

# secondary styles for widgets can be described outside of a theme
style.configure('Dracula_Green.TLabel', foreground='#50fa7b', background='#44475a')
###########################################################

###########################################################
# NOTEBOOK:
# - allows tabbed view for calendar and to-do list

# instantiate our tabbed notebook
notebook = ttk.Notebook(root, width=770, height=630, padding=20)

# create content for notebook sections
cal_widget = ttk.Label()
cal_widget.grid() # doesn't work when compounded w/line above e.g. ttk.Label().grid()
todo_widget = ttk.Label()
todo_widget.grid()

# create tabs for notebook
notebook.enable_traversal() # enables keyboard shortcuts for tabs if fully implemented
notebook.add(todo_widget, text='To-Do List') # sticky to position content inside tab
notebook.add(cal_widget, text='Calendar')
notebook.grid()

###########################################################

###########################################################
# CALENDAR APP
def currMonth(current, display):
	display['year'] = current['year']
	display['month'] = current['month']
	drawMonth()
	return

def nextMonth(current, display):
	if display['month'] == 12:
		display['year'] += 1
		display['month'] = 1
	else:
		display['month'] += 1
	drawMonth()
	return

def prevMonth(current, display):
	if display['month'] == 1:
		display['year'] -= 1
		display['month'] = 12
	else:
		display['month'] -= 1
	drawMonth()
	return

def drawMonth():
	# Get Number of Days and Numbers of Full or Partial Weeks in This Month
	#		Note on line 16: calendar's monthrange(year,month) function returns
	#		a tuple like (2, 29). See documentation for more info
	monthRange = cal.monthrange(display['year'], display['month'])
	numDays = monthRange[1]
	if numDays % 7 != 0: # if days don't divide evenly into 7, need extra week row to display month
		rowsForWeeks = int(numDays / 7) + 1
	else:
		rowsForWeeks = int(numDays / 7)

	# Frame to contain calendar month (note: labelanchor is for month name only, not box containing calendar)
	showMonth = ttk.LabelFrame(cal_widget, style='monthBlock.TLabelframe', labelanchor='n')
	showMonth['text']=(cal.month_name[display['month']], str(display['year']))
	showMonth.grid(row=3, columnspan=7)

	# DAYS OF THE WEEK (calendar headers)
	for x in range(7):
		ttk.Label(showMonth, text=cal.day_abbr[x], # Can also use day_name[x] for full name
			 borderwidth=0, padding=3).grid(row=1,column=x)

	# Determine What Day of the Week the First Day Falls On (0 for Monday, etc.)
	firstDayOffset = cal.weekday(display['year'], display['month'], 1)
	# Display Month as a Grid of Days

	daysShown = 0 # Counter starts at zero
	dayBlock = [] # Empty list for tkinter labels, each containing one calendar day
	for wk in range(rowsForWeeks):
		for day in range(7):
			if firstDayOffset != 0:
				nullDay = ttk.Label(showMonth, style='nullDay.TLabel')
				nullDay.grid(row=wk+3,column=day)
				firstDayOffset = firstDayOffset - 1
			else:
				# If number of days printed to grid so far is less than the days in
				# a given month, add another day
				if daysShown < numDays:
					dayBlock.append(ttk.LabelFrame(showMonth, text=daysShown, style='dayBlock.TLabelframe'))
					dayBlock[daysShown].configure(text='%s'%(daysShown + 1), borderwidth=0, width=105, height=100)
					dayBlock[daysShown].grid(row=wk+3,column=day)
					#ttk.Label(showMonth, text='%s'%(daysShown + 1), borderwidth=1, padx=5, pady=5, width=10, height=5, foreground='#CFD0C2', background='red', takefocus=1).grid(row=wk+2,column=day)
					daysShown = daysShown + 1

# CALCULATE CURRENT DATE (& store this info for when user jumps back to current month)
current = {'day'	: datetime.now().day,
		   'month'	: datetime.now().month,
		   'year'	: datetime.now().year}

# MONTH TO DISPLAY IN CALENDAR (starts as current date by default)
display = {'month'	: current['month'],
		   'year'	: current['year']}

# Calendar Navigation Buttons
calNav = ttk.LabelFrame(cal_widget, labelanchor='n', style='calNav.TLabelframe')
calNav.grid(row=1, columnspan=7)

prevMonthBtn = ttk.Button(calNav, text=' <= Prev ', command=partial(prevMonth, current, display)).grid(row=2,column=1, sticky='w')
currMonthBtn = ttk.Button(calNav, text=' Current ', command=partial(currMonth, current, display)).grid(row=2,column=2, sticky='n')
nxtMonthBtn = ttk.Button(calNav, text=' Next => ', command=partial(nextMonth, current, display)).grid(row=2,column=3, sticky='e',)

drawMonth()
###########################################################

###########################################################
# TASK LIST
task_list = []
task_list.append({'task': "Feed Cat", 'priority': "High"})
task_list.append({'task': "Mow Lawn", 'priority': "Medium"})
task_list.append({'task': "Go to DMV", 'priority': "Low"})

def add_task():
    # get the inputs
    task_list.append({
        'task': input_task.get(),
        'priority': input_task_priority.get()
    })

    # reset input boxes/selections
    input_task.delete(0, 'end')
    input_task_priority.current(0)

    # reset display
    show_tasks()

def rem_task():
	# select current highlighted item and get task and priority
	i = task_box.focus()
	task_item = task_box.item(i)["values"][0]
	task_priority = task_box.item(i)["values"][1]
	
	# find index for item to be removed
	j = 0
	for i in task_list:
		if ((i["task"] == task_item) and (i["priority"] == task_priority)):
			index = j
		j+=1

	# pop the item from the list
	task_list.pop(index)
	print(task_list)
	# reset display
	show_tasks()

def show_tasks():
    # empty treeview task_box completely
    task_box.delete(*task_box.get_children())

    # reprint all items in task_list to task_box
    for i in range(len(task_list)):
        task_item = task_list[i]['task']
        task_priority = task_list[i]['priority']
        task_box.insert('', 'end', values=(task_item, task_priority))
    return

showToDo = ttk.LabelFrame(todo_widget, style='taskBlock.TLabelframe', width=670)
showToDo.grid(row=1)

# Text entry box: add a task
input_task = ttk.Entry(showToDo, width=40, font=('Lucida Console', 11, 'bold'))
input_task.grid(row=2, column=0)

# priority selection field
input_task_priority = ttk.Combobox(showToDo, values = ['', 'High', 'Medium', 'Low'])
input_task_priority.grid(row = 2, column=1)
input_task_priority.current(0)

# Button: add new task
newTask = ttk.Button(showToDo, text='+', command=add_task, style='newTask.TButton')
newTask.grid(row=2, column=2)

# Box to display tasks
task_box = ttk.Treeview(showToDo)
task_box['columns']=('task','priority')
task_box['show'] = 'headings' # without this, there is empty 1st col
task_box.column('task', width=470, minwidth=100)
task_box.column('priority', width=200, minwidth=100, stretch=tk.NO)
task_box.heading('task',text='Task',anchor=tk.W)
task_box.heading('priority', text='Priority',anchor=tk.W)

task_box.grid(columnspan=3)
show_tasks()

# Button: remove task
remTask = ttk.Button(showToDo, text='-', command=rem_task, style='newTask.TButton')
remTask.grid(row=10, column=2)
###########################################################
# BEGIN MAIN APP LOOP: content added BELOW this function won't show up in app
if __name__ == '__main__':
	root.mainloop()
###########################################################
