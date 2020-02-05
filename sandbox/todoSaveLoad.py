import json

class TaskList:
# class-defined variables: __listOfTasks[] for holding task instances
    def __init__(self):
        self.__listOfTasks = []
    def loadJSON(self, filename):
        with open(filename) as jsonHandle:
            jsonData = json.load(jsonHandle)
            print(jsonData)
    # placeholder: will add remaining functionality Thursday 2/4

class Tasks:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
    def getTitle(self):
        return self.title
    def getPriority(self):
        return self.priority
    def setTitle(self, title):
        self.title = title
    def setPriority(self, priority):
        self.priority = priority

# test for loadJSON
newTodo = TaskList()

newTodo.loadJSON("testFile.json")