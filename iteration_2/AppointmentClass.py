##########################################################################
# File: AppointmentClass.py
# Function:  This class holds the data and methods for each appointment,
#       including title of the appointment, the start and end time, and
#       comments, as well as getters and setters for the data.
# Date Last Modified: 22 February 2020
##########################################################################

class Appointment:
#########################################################################
#   Variables used in this class:
#       __title: holds the title to display for the appointment
#       __year: holds the year of the date of the appointment
#       __month: holds the month of the date of the appointment
#       __day: holds the day of the date of the appointment
#       __hour: holds the hour the appointment starts
#       __minute: holds the minute the appointment ends
#       __ampm: holds the 12-hour clock period
#########################################################################
##########################################################################
#   Initializing method
##########################################################################
    def __init__(self, title, year, month, day, hour, minute, ampm):
        self.__title = title
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__ampm = ampm
##########################################################################
#   GETTERS AND SETTERS
##########################################################################
    def getTitle(self):
        return self.__title
    def getYear(self):
        return self.__year
    def getMonth(self):
        return self.__month
    def getDay(self):
        return self.__day
    def getHour(self):
        return self.__hour
    def getMinute(self):
        return self.__minute
    def getAmpm(self):
        return self.__ampm
    # def getComments(self):
    #     return self.__comments
    def setTitle(self, title):
        self.__title = title
    def setYear(self, year):
        self.__year = year
    def setMonth(self, month):
        self.__month = month
    def setDay(self, day):
        self.__day = day
    def setDay(self, hour):
        self.__hour = hour
    def setMinute(self, minute):
        self.__minute = minute
    def setAmpm(self, ampm):
        self.__ampm = ampm
    # def setComments(self, comments):
    #     self.__comments = comments

        
