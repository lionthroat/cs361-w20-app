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
                self.__listOfCalItems.append(Appointment(title, day, month, year, startTime, endTime, comments))

##########################################################################
#   Function: removeApptFromList
#   Takes: title, date day, month and year, start time, end time and comments of appt to be removed
#   Returns: nothing
#   Summary: This function takes the information of the appointment to be
#		deleted, and pops it from the calendar item list.
##########################################################################
	def removeApptFromList(self, title, day, month, year, startTime, endTime, comments):
		for i in range(len(self.__listOfCalItems)):
			if self.__listOfCalItems[i].getTitle() == title and \
                           self.__listOfCalItems[i].getDay() == day and \
                           self.__listOfCalItems[i].getMonth() == month and \
                           self.__listOfCalItems[i].getYear() == year and \
                           self.__listOfCalItems[i].getStartTime() == startTime and \
                           self.__listOfCalItems[i].getEndTime() == endTime and \
                           self.__listOfCalItems[i].getComments() == comments:
				self.__listOfCalItems.pop(i)
				break

##########################################################################
#   Function: loadJSON
#   Takes: file name to load from
#   Returns: nothing
#   Summary: This function takes a JSON file and loads the data into the
#       __listOfCalItems list by creating instances of Appointment loaded
#       with the next entry's data and placing that instance in the list.
##########################################################################
	def loadJSON(self, filename):
		with open(filename) as jsonHandle:
			jsonData = json.load(jsonHandle)
			for item in jsonData:
				self.addApptToList(item['title'], item['day'],\
                                item['month'], item['year'], item['startTime'},\
                                item['endTime'], item['comments'])
		jsonHandle.close()

##########################################################################
#   Function: saveToJSON
#   Takes: file name to save to
#   Returns: nothing
#   Summary: This function takes the current __listOfCalItems and converts it
#       and places into a JSON file.
##########################################################################
	def saveToJSON(self, filename):
		appts = []
		for item in self.__listOfCalItems:
			newAppt = {}
			newAppt['title'] = item.getTitle()
			newAppt['day'] = item.getDay()
			newAppt['month'] = item.getMonth()
			newAppt['year'] = item.getYear()
			newAppt['startTime'] = item.getStartTime()
			newAppt['endTime'] = item.getEndTime()
			newAppt['comments'] = item.getComments()
			appts.append(newAppt)

		with open(filename, "w") as jsonHandle:
			convertedJSON = json.dump(appts, jsonHandle)

		jsonHandle.close()

##########################################################################
#   Function: printAppts
#   Takes: nothing
#   Returns: nothing
#   Summary: This function prints to console the information of every item
#		in the calendar items list.
##########################################################################
	def printAppts(self):
	    for appt in self.__listOfCalItems:
			print(appt.getTitle())
			print(appt.getDay())
			print(appt.getMonth())
			print(appt.getYear())
			print(appt.getStartTime())
			print(appt.getEndTime())
			print(appt.getComments())

##########################################################################
#   GETTERS AND SETTERS
##########################################################################
	def getListSize(self):
		return len(self.__listOfCalItems)
	def getApptAt(self, index):
		return self.__listOfCalItems[index]
