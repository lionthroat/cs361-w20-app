##########################################################################
#   Class: CalendarItems
#   Summary:  This class holds the Calendar Items.  It has a list of
#       appointment class instances and functions to add and remove
#       appointments.  It can also save appointments to a JSON file or
#       load from a JSON file.
##########################################################################

import json
from AppointmentClass import *

class CalendarItems:
#########################################################################
#   Variables used in this class:
#       __listOfAppointments: A list of Appointment class instances for
#           each appointment to be listed in the calendar.
#########################################################################
##########################################################################
#   Initializing method
##########################################################################
	def __init__(self):
		self.__listOfCalItems = []

##########################################################################
#   Function: addApptToList
#   Takes: title, date day, month and year, start time, end time and comments of a new appt
#   Returns: nothing
#   Summary: This function takes the information of a new appointment
#		to be added, and appends it to the list of calendar items.
##########################################################################
	def addApptToList(self, title, day, month, year, startTime, endTime, comments):
	

##########################################################################
#   Function: removeApptFromList
#   Takes: title, date day, month and year, start time, end time and comments of appt to be removed
#   Returns: nothing
#   Summary: This function takes the information of the appointment to be
#		deleted, and pops it from the calendar item list.
##########################################################################
	def removeApptFromList(self, title, day, month, year, startTime, endTime, comments):
		

##########################################################################
#   Function: loadJSON
#   Takes: file name to load from
#   Returns: nothing
#   Summary: This function takes a JSON file and loads the data into the
#       __listOfCalItems list by creating instances of Appointment loaded
#       with the next entry's data and placing that instance in the list.
##########################################################################
	def loadJSON(self, filename):
		

##########################################################################
#   Function: saveToJSON
#   Takes: file name to save to
#   Returns: nothing
#   Summary: This function takes the current __listOfCalItems and converts it
#       and places into a JSON file.
##########################################################################
	def saveToJSON(self, filename):
		

##########################################################################
#   Function: printAppts
#   Takes: nothing
#   Returns: nothing
#   Summary: This function prints to console the information of every item
#		in the calendar items list.
##########################################################################
	def printAppts(self):
	    

##########################################################################
#   GETTERS AND SETTERS
##########################################################################
	def getListSize(self):
		return len(self.__listOfCalItems)
	def getApptAt(self, index):
		return self.__listOfCalItems[index]
