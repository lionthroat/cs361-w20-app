# test Spike for first iteration
# Matt Byrne and Lauren Work

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
