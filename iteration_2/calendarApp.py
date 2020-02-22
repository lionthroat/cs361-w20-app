##############################################################################
# File: calendarApp.py
# Function:  This draws the calendar and maintains the calendar view based
#       on current date, selection to move forward or back, or adding or
#       removing appointments.
# Date Last Modified: 16 February 2020
################################################################################

import tkinter.ttk as ttk
import tkinter as tk
from tkinter import *
from functools import partial
from datetime import datetime
import calendar as cal

from tkinter import simpledialog
from tkinter import messagebox

class AppCalendar(ttk.Label):
	def __init__(self, parent):
		ttk.Label.__init__(self)
		# CALCULATE CURRENT DATE (& store this info for when user jumps back to current month)
		current = {'day'	: datetime.now().day,
				   'month'	: datetime.now().month,
				   'year'	: datetime.now().year}

		# MONTH TO DISPLAY IN CALENDAR (starts as current date by default)
		display = {'month'	: current['month'],
				   'year'	: current['year']}

		# appointment list
		#self.filepath = 'apptFile.json'
		#myCal = ApptList()
		#myCal.loadJSON(self.filepath)
		myCal = [
			{'appt': 'Concert','year': 2020,'month': 2,'date': 16,'hour': 8,'minute': 30,'ampm': 'PM'},
			{'appt': 'Volunteer','year': 2020,'month': 2,'date': 17,'hour': 12,'minute': '00','ampm': 'PM'},
			{'appt': 'President\'s Day','year': 2020,'month': 2,'date': 18,'hour': '','minute': '','ampm': ''},
			{'appt': 'Midterm','year': 2020,'month': 2,'date': 20,'hour': 7,'minute': 45,'ampm': 'AM'},
			{'appt': 'Hiking','year': 2020,'month': 2,'date': 24,'hour': 2,'minute': 15,'ampm': 'PM'},
			{'appt': 'Leap Day','year': 2020,'month': 2,'date': 29,'hour': '','minute': '','ampm': ''}
		]

		# Calendar Navigation Buttons
		calNav = ttk.LabelFrame(self, labelanchor='n', style='calNav.TLabelframe')
		calNav.grid(row=2, columnspan=7)

		prevMonthBtn = ttk.Button(calNav, text=' <= Prev ', command=partial(self.prevMonth, current, display, myCal)).grid(row=2,column=1, sticky='w')
		currMonthBtn = ttk.Button(calNav, text=' Current ', command=partial(self.currMonth, current, display, myCal)).grid(row=2,column=2, sticky='n')
		nxtMonthBtn = ttk.Button(calNav, text=' Next => ', command=partial(self.nextMonth, current, display, myCal)).grid(row=2,column=3, sticky='e',)

		self.drawMonth(display, myCal, current)

	def newApptfromModal(self, modalWin, inputAppt, apptHour, apptMinute, apptAMPM, display, date, myCal, current):

		# only save appointment if user gave the event a name/title
		if inputAppt.get() != '':
			# add task
			myCal.append({'appt': inputAppt.get(), 'year': display['year'], 'month': display['month'], 'date': date, 'hour': apptHour.get(), 'minute': apptMinute.get(), 'ampm': apptAMPM.get()})
			print(myCal)

			inputAppt.delete(0, 'end')

			# Redraw Calendar
			self.drawMonth(display, myCal, current)

		# save changes to file and reset display
		#myCal.saveToJSON(self.filepath)

		# Close the modal
		modalWin.wm_attributes("-disabled", False)
		modalWin.destroy()

	def apptModal(self, display, date, myCal, current):
		modalWin = tk.Toplevel()
		w = '430'
		h = '200'
		modalWin.geometry('{}x{}'.format(w, h))
		modalWin.title(' Add Appointment ') # main window title
		modalWin.config(background='#F5F5F5')
		modalWin.attributes("-toolwindow",1)
		modalWin.resizable(0,0)
		modalWin.grid()
		modalWin.focus_force()

		self.center(modalWin)

		# Appointment Entry Container container
		apptInputContainer = ttk.LabelFrame(modalWin, labelanchor='n', style='timeInput.TLabelframe')
		apptInputContainer.grid(row=0, columnspan=7, padx=10, pady=0, sticky='w')

		# apptIcon = PhotoImage(apptInputContainer, file = 'images/appt.ico')
		# apptIcon.grid()

		# Text entry box: add Appt
		inputAppt = ttk.Entry(apptInputContainer, width=28, font=('Lucida Console', 14), textvariable='Add Appointment')
		inputAppt.grid(row = 0, columnspan=5, sticky='e', padx=20, pady=18)

		# Time input container
		timeInput = ttk.LabelFrame(modalWin, labelanchor='n', style='timeInput.TLabelframe')
		timeInput.grid(row=1, columnspan=4, padx=50, pady=0, sticky='w')

		apptHour = ttk.Combobox(timeInput, font=('Lucida Console', 11), values = ['','1','2','3','4','5','6','7','8','9','10','11','12'], width=2)
		apptHour.grid(row = 1, column=0, sticky='w')
		apptHour.current(4)

		apptMinute = ttk.Combobox(timeInput, font=('Lucida Console', 11), values = ['','00','15','30','45',], width=2)
		apptMinute.grid(row = 1, column=1, sticky='n')
		apptMinute.current(2)

		apptAMPM = ttk.Combobox(timeInput, font=('Lucida Console', 11), values = ['','AM','PM'], width=2)
		apptAMPM.grid(row = 1, column=2, sticky='e')
		apptAMPM.current(2)

		saveBtn = ttk.Button(modalWin, text=' Save ', command=partial(self.newApptfromModal, modalWin, inputAppt, apptHour, apptMinute, apptAMPM, display, date, myCal, current), style='saveBtn.TButton')
		saveBtn.grid(row = 1, columnspan=6, sticky='e')

	def center(self, win):
		# centering a toplevel window (modal) in tkinter
		# based on this solution:
		# https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
	    win.update_idletasks()
	    width = win.winfo_width()
	    height = win.winfo_height()
	    x = (win.winfo_screenwidth() // 2) - (width // 2)
	    y = (win.winfo_screenheight() // 2) - (height // 2)
	    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

	def addAppt(self, display, date, myCal):
		# ask for the appointment name with a pop-up
		inputAppt = simpledialog.askstring('Add Appointment', 'Enter the name of the appointment.')
		if inputAppt:
			# the data structure should be changed from a dictionary to a class
			myCal.append({'appt': inputAppt, 'year': display['year'], 'month': display['month'], 'date': date})
		print(myCal)

		self.drawMonth(display, myCal, current)

		# display appointments for each day
	def displayAppt(self, display, today, myCal):
		toShow = ''
		for item in myCal:
			if item['year'] == display['year'] and item['month'] == display['month'] and item['date'] == today:
				toShow = toShow + (item['appt']) + '\n'

		messagebox.showinfo(f'{display["month"]}/{today}/{display["year"]}', toShow)

	# When user clicks to see current month, the date stored in current
	# will allow us to jump back/forward to the present month
	def currMonth(self, current, display, myCal):
		display['year'] = current['year']
		display['month'] = current['month']
		self.drawMonth(display, myCal, current)
		return

	# Upon button clicking to see next month, the system will try
	# to simply add 1 from the current month, unless it's December,
	# in which case the calendar needs to show month 1 of next year
	def nextMonth(self, current, display, myCal):
		if display['month'] == 12:
			display['year'] += 1
			display['month'] = 1
		else:
			display['month'] += 1
		self.drawMonth(display, myCal, current)
		return

	# Upon button clicking to see previous month, the system will try
	# to simply subtract 1 from the current month, unless it's January,
	# in which case the calendar needs to show month 12 of prev year
	def prevMonth(self, current, display, myCal):
		if display['month'] == 1:
			display['year'] -= 1
			display['month'] = 12
		else:
			display['month'] -= 1
		self.drawMonth(display, myCal, current)
		return

	def drawMonth(self, display, myCal, current):
		# Get Number of Days and Numbers of Full or Partial Weeks in This Month
		#		Note on line 16: calendar's monthrange(year,month) function returns
		#		a tuple like (2, 29). See documentation for more info
		monthRange = cal.monthrange(display['year'], display['month'])
		numDays = monthRange[1]
		if numDays % 7 != 0: # if days don't divide evenly into 7, need extra week row to display month
			rowsForWeeks = int(numDays / 7) + 1
		else:
			rowsForWeeks = int(numDays / 7)

		# Frame to contain calendar month (note: labelanchor is for month name only, not box containing calendar)
		showMonth = ttk.LabelFrame(self, style='monthBlock.TLabelframe', labelanchor='n')

		# Print name of month and year at top of calendar month
		showMonth['text']=(cal.month_name[display['month']], str(display['year']))
		showMonth.grid(row=3, columnspan=7)

		# DAYS OF THE WEEK (calendar headers)
		for x in range(7):
			ttk.Label(showMonth, text=cal.day_abbr[x], # Can also use day_name[x] for full name
				 borderwidth=0, padding=3).grid(row=1,column=x)

		# Determine What Day of the Week the First Day Falls On (0 for Monday, etc.)
		firstDayOffset = cal.weekday(display['year'], display['month'], 1)

		# DISPLAY MONTH AS A GRID OF DAY BLOCKS
		daysShown = 0 # Counter starts at zero
		dayBlock = [] # Empty list for tkinter labels, each containing one calendar day
		for wk in range(rowsForWeeks):
			for day in range(7):
				if firstDayOffset != 0:
					nullDay = ttk.Label(showMonth, style='nullDay.TLabel')
					nullDay.grid(row=wk+3,column=day)
					firstDayOffset = firstDayOffset - 1
				else:
					# If number of days printed to grid so far is less than the days in
					# a given month, add another day
					if daysShown < numDays:
						dayBlock.append(ttk.LabelFrame(showMonth, text=daysShown + 1))
						dayBlock[daysShown].configure(labelanchor='nw', width=105, height=100, borderwidth=0)

						today = current['day']
						todayFlag = 0
						# Configure calendar block styles based on whether day is past/today/future
						if display['month'] == current['month'] and display['year'] == current['year']:
							if daysShown + 1 == today:
								dayBlock[daysShown].configure(style='todayBlock.TLabelframe')
								todayFlag = 1
							elif daysShown + 1 < today:
								dayBlock[daysShown].configure(style='pastBlock.TLabelframe')
							else:
								dayBlock[daysShown].configure(style='dayBlock.TLabelframe')
						else:
							dayBlock[daysShown].configure(style='dayBlock.TLabelframe')
						dayBlock[daysShown].grid(row=wk+3,column=day)
						dayBlock[daysShown].grid_propagate(False)

						# button to show appointments
						for item in myCal:
							if item['year'] == display['year'] and item['month'] == display['month'] and item['date'] == daysShown + 1:
								if item['hour'] != '': # see if user input a time for the event or if it's an all-day event
									itemDisplay = item['hour'], ':' ,item['minute'], item['appt']
								else:
									itemDisplay = item['appt']
								showButton = ttk.Button(dayBlock[daysShown], text=(itemDisplay), command=partial(self.displayAppt, display, daysShown + 1, myCal))
								showButton.grid(row = 1)

								# special styling for today's events
								if todayFlag == 1:
									showButton.configure(style='showButton.TButton')

						newBtn = ttk.Button(dayBlock[daysShown], text='+', command=partial(self.apptModal, display, daysShown + 1, myCal, current)).grid(row=2,sticky='w',pady=5)

						daysShown = daysShown + 1
