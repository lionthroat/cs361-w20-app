############################################################
# Spike 1: Testing Front-End To-Do List Design
# Oregon State University, Winter 2020: CS 361, Week 4
# Agile Project: Release Cycle 1
#
# February 1, 2020
############################################################

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from functools import partial
import json

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

#function to add a task
#currently adds a task to the dictionary of tasks and prints. Also adds to the listbox and displays
def add_task():
	# get the inputs
	sample_list.append({'name': input_task_name.get(), 'priority': input_task_priority.get()})

	# reset input boxes/selections
	input_task_name.delete(0, 'end')
	input_task_priority.current(0)

	# reset display
	show_tasks()

	print(sample_list)


def rem_task(i):
	# pop the item from the lsit
	sample_list.pop(i)

	# reset display
	show_tasks()

	print(sample_list)



def show_tasks():
	# reset first
	task_box.delete("1.0", "end")
	#insert a title into the taskbox
	task_box.insert(END, 'Task' + '\t' + '\t' + 'Priority' + '\n')

	#insert each task into the taskbox
	for i in range(len(sample_list)):
		task_box.insert(END, sample_list[i]['name'] + '\t' + '\t' + sample_list[i]['priority'] + '\n')
		# attach a button
		task_box.window_create(task_box.index("end"), window = tk.Button(task_box, text="Remove", command = partial(rem_task, i)))
		task_box.insert(END, "\n")


#name of window
root = tk.Tk()

#set window geometry
w = '300'
h = '400'
root.geometry('{}x{}'.format(w, h))

#generate sample list as a starting point
sample_list = []
sample_list.append({'name': "Feed Cat", 'priority': "High"})
sample_list.append({'name': "Mow Lawn", 'priority': "Medium"})
sample_list.append({'name': "Go to DMV", 'priority': "Low"})

#create window label
lbl_title = tk.Label(root, text="To-Do List", bg="white")
lbl_title.grid(row=0,column=0, sticky=W)

#create box to display tasks
task_box = Text(root,width = 25,height=10)
task_box.grid(row=2,column=0)

#create labels for text entry fields
tk.Label(root, text="New Task Name:", bg="white").grid(row=7, sticky=W)
tk.Label(root, text="New Task Priority:", bg="white").grid(row=9, sticky=W)

#create text entry fields
input_task_name = tk.Entry(root)
input_task_name.grid(row = 8, column = 0)

# priority selection field
input_task_priority = Combobox(root, values = ["", "High", "Medium", "Low"])
input_task_priority.grid(row = 10, column = 0)
input_task_priority.current(0)

#create button to add new task
add_new_button = Button(root, text="Add New Task", command=add_task)
add_new_button.grid(row=11, sticky=W)

show_tasks()

if __name__ == "__main__":
	root.mainloop()
