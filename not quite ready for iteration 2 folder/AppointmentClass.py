##########################################################################
#   Class: Appointment
#   Summary:  This class holds the data and methods for each appointment,
#       including title of the appointment, the start and end time, and
#       comments, as well as getters and setters for the data.
##########################################################################

class Appointment:
#########################################################################
#   Variables used in this class:
#       __title: holds the title to display for the appointment
#       __date: holds the date of the appointment
#       __startTime: holds the time the appointment starts
#       __endTime: holds the time the appointment ends
#       __comments: Holds any comments regarding the appointment
#########################################################################
##########################################################################
#   Initializing method
##########################################################################
    def __init__(self, title, date, startTime, endTime, comments):
        self.__title = title
        self.__date = date
        self.__startTime = startTime
        self.__endTime = endTime
        self.__comments = comments
##########################################################################
#   GETTERS AND SETTERS
##########################################################################
    def getTitle(self):
        return self.__title
    def getDate(self):
        return self.__date
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__EndTime
    def getComments(self):
        return self.__comments
    def setTitle(self, title):
        self.__title = title
    def setDate(self, date):
        self.__date = date
    def setStartTime(self, startTime):
        self.__startTime = startTime
    def setEndTime(self, endTime):
        self.__endTime = endTime
    def setComments(self, comments):
        self.__comments = comments
        
