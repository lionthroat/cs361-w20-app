##########################################################################
#   Class: Task
#   Summary:  This class holds the data for each task, including title of
#       the task and priority status for the task.  It also holds
#       functions to get or set all data.
##########################################################################

class Task:
#########################################################################
#   Variables used in this class:
#       __title: holds the title to display for the task
#       --priority: Holds a priority for this task (high or low)
#########################################################################
##########################################################################
#   Initializing method
##########################################################################
    def __init__(self, title, priority):
        self.__title = title
        self.__priority = priority
##########################################################################
#   GETTERS AND SETTERS
##########################################################################
    def getTitle(self):
        return self.__title
    def getPriority(self):
        return self.__priority
    def setTitle(self, title):
        self.__title = title
    def setPriority(self, priority):
        self.__priority = priority

