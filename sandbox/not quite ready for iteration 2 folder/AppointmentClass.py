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
#       __day: holds the day of the date of the appointment
#       __month: holds the month of the date of the appointment
#       __year: holds the year of the date of the appointment
#       __startTime: holds the time the appointment starts
#       __endTime: holds the time the appointment ends
#       __comments: Holds any comments regarding the appointment
#########################################################################
##########################################################################
#   Initializing method
##########################################################################
    def __init__(self, title, day, month, year, startTime, endTime, comments):
        self.__title = title
        self.__day = day
        self.__month = month
        self.__year = year
        self.__startTime = startTime
        self.__endTime = endTime
        self.__comments = comments
##########################################################################
#   GETTERS AND SETTERS
##########################################################################
    def getTitle(self):
        return self.__title
    def getDay(self):
        return self.__day
    def getMonth(self):
        return self.__month
    def getYear(self):
        return self.__year
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__EndTime
    def getComments(self):
        return self.__comments
    def setTitle(self, title):
        self.__title = title
    def setDay(self, day):
        self.__day = day
    def setMonth(self, month):
        self.__month = month
    def setYear(self, year):
        self.__year = year
    def setStartTime(self, startTime):
        self.__startTime = startTime
    def setEndTime(self, endTime):
        self.__endTime = endTime
    def setComments(self, comments):
        self.__comments = comments
        
