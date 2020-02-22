##########################################################################
#   Class: TaskList
#   Summary:  This class holds the Task List.  It has a list of task class
#       instances and functions to add and remove tasks.  It can also save
#       tasks to a JSON file or load from a JSON file.
# Date Last Modified: 16 February 2020
##########################################################################

import json
from TaskClass import *

class TaskList:
#########################################################################
#   Variables used in this class:
#       __listOfTasks: A list of Task class instances for each task
#           to be listed in the to do list
#########################################################################
##########################################################################
#   Initializing method
##########################################################################
	def __init__(self):
		self.__listOfTasks = []

##########################################################################
#   Function: addTaskToList
#   Takes: title and priority of the new task
#   Returns: nothing
#   Summary: This function takes the title and priority of the new task
#		to be added, and appends it to the task list.
##########################################################################
	def addTaskToList(self, title, priority):
		self.__listOfTasks.append(Task(title, priority))

##########################################################################
#   Function: removeTaskFromList
#   Takes: title and priority of the task to be removed
#   Returns: nothing
#   Summary: This function takes the title and priority of the task to be
#		deleted, and pops it from the task list.
##########################################################################
	def removeTaskFromList(self, title, priority):
		for i in range(len(self.__listOfTasks)):
			if self.__listOfTasks[i].getTitle() == title and self.__listOfTasks[i].getPriority() == priority:
				self.__listOfTasks.pop(i)
				break

##########################################################################
#   Function: loadJSON
#   Takes: file name to load from
#   Returns: nothing
#   Summary: This function takes a JSON file and loads the data into the
#       __listOfTasks list by creating instances of task loaded with the
#       next entry's data and placing that instance in the list.
##########################################################################
	def loadJSON(self, filename):
		with open(filename) as jsonHandle:
			jsonData = json.load(jsonHandle)
			for item in jsonData:
				self.addTaskToList(item['title'], item['priority'])
		jsonHandle.close()

##########################################################################
#   Function: saveToJSON
#   Takes: file name to save to
#   Returns: nothing
#   Summary: This function takes the current __listOfTasks and converts it
#       and places into a JSON file.
##########################################################################
	def saveToJSON(self, filename):
		tasks = []
		for item in self.__listOfTasks:
			newTask = {}
			newTask['title'] = item.getTitle()
			newTask['priority'] = item.getPriority()
			tasks.append(newTask)

		with open(filename, "w") as jsonHandle:
			convertedJSON = json.dump(tasks, jsonHandle)

		jsonHandle.close()

##########################################################################
#   Function: printTasks
#   Takes: nothing
#   Returns: nothing
#   Summary: This function prints to console the title and priority of
#		every item in the task list.
##########################################################################
	def printTasks(self):
		for item in self.__listOfTasks:
			print(item.getTitle())
			print(item.getPriority())

##########################################################################
#   GETTERS AND SETTERS
##########################################################################
	def getListSize(self):
		return len(self.__listOfTasks)
	def getTaskAt(self, index):
		return self.__listOfTasks[index]
