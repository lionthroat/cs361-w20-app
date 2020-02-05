##########################################################################
#   Class: TaskList
#   Summary:  This class holds the Task List.  It has a list of task class
#       instances and functions to add and remove tasks.  It can also save
#       tasks to a JSON file or load from a JSON file.
##########################################################################

import json
import tasks

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
    def addTaskToList(self, title, priority):
        ##add/remove team to add here
    def removeTaskFromList(self, title, priority):
        ##add/remove team to add here, no clue what parameters you want
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
            print(jsonData)
        # placeholder: will add remaining functionality Thursday 2/4
##########################################################################
#   Function: saveToJSON
#   Takes: file name to save to
#   Returns: nothing
#   Summary: This function takes the current __listOfTasks and converts it
#       and places into a JSON file.
##########################################################################
    def saveToJSON(self, fileName):
        # placeholder: will add remaining functionality Thursday 2/4
        
