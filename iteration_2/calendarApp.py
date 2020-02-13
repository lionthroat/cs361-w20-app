import tkinter.ttk as ttk
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
		#mylist = ApptList()
		#mylist.loadJSON(self.filepath)
		mylist = [{'appt': 'test input', 'year': 2020, 'month': 2, 'date': 13}]
		
		# Calendar Navigation Buttons
		calNav = ttk.LabelFrame(self, labelanchor='n', style='calNav.TLabelframe')
		calNav.grid(row=2, columnspan=7)

		prevMonthBtn = ttk.Button(calNav, text=' <= Prev ', command=partial(self.prevMonth, current, display, mylist)).grid(row=2,column=1, sticky='w')
		currMonthBtn = ttk.Button(calNav, text=' Current ', command=partial(self.currMonth, current, display, mylist)).grid(row=2,column=2, sticky='n')
		nxtMonthBtn = ttk.Button(calNav, text=' Next => ', command=partial(self.nextMonth, current, display, mylist)).grid(row=2,column=3, sticky='e',)

		self.drawMonth(display, mylist)

# add appointment
	def addAppt(self, display, date, mylist):
		# ask for the appointment name with a pop-up
		inputAppt = simpledialog.askstring('Add Appointment', 'Enter the name of the appointment.')
		if inputAppt:
			# the data structure should be changed from a dictionary to a class
			mylist.append({'appt': inputAppt, 'year': display['year'], 'month': display['month'], 'date': date})
		print(mylist)

		self.drawMonth(display, mylist)

# display appointments for each day
	def displayAppt(self, display, today, mylist):
		toShow = ''
		for item in mylist:
			if item['year'] == display['year'] and item['month'] == display['month'] and item['date'] == today:
				toShow = toShow + (item['appt']) + '\n'

		messagebox.showinfo(f'{display["month"]}/{today}/{display["year"]}', toShow)

	def currMonth(self, current, display, mylist):
		display['year'] = current['year']
		display['month'] = current['month']
		self.drawMonth(display, mylist)
		return

	def nextMonth(self, current, display, mylist):
		if display['month'] == 12:
			display['year'] += 1
			display['month'] = 1
		else:
			display['month'] += 1
		self.drawMonth(display, mylist)
		return

	def prevMonth(self, current, display, mylist):
		if display['month'] == 1:
			display['year'] -= 1
			display['month'] = 12
		else:
			display['month'] -= 1
		self.drawMonth(display, mylist)
		return

	def drawMonth(self, display, mylist):
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
		showMonth['text']=(cal.month_name[display['month']], str(display['year']))
		showMonth.grid(row=3, columnspan=7)

		# DAYS OF THE WEEK (calendar headers)
		for x in range(7):
			ttk.Label(showMonth, text=cal.day_abbr[x], # Can also use day_name[x] for full name
				 borderwidth=0, padding=3).grid(row=1,column=x)

		# Determine What Day of the Week the First Day Falls On (0 for Monday, etc.)
		firstDayOffset = cal.weekday(display['year'], display['month'], 1)
		# Display Month as a Grid of Days

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
						#dayBlock.append(ttk.LabelFrame(showMonth, text=daysShown, style='dayBlock.TLabelframe'))
						dayBlock.append(ttk.LabelFrame(showMonth, text=daysShown + 1, style='dayBlock.TLabelframe'))
						dayBlock[daysShown].configure(borderwidth=0, width=105, height=100)
						dayBlock[daysShown].grid(row=wk+3,column=day)
						dayBlock[daysShown].grid_propagate(False)

						# button to show appointments
						for item in mylist:
							if item['year'] == display['year'] and item['month'] == display['month'] and item['date'] == daysShown + 1:
								showButton = ttk.Button(dayBlock[daysShown], text='Show Appt', command=partial(self.displayAppt, display, daysShown + 1, mylist))
								showButton.grid(row = 1)

						# button to add appointment
						newButton = ttk.Button(dayBlock[daysShown], text='+', command=partial(self.addAppt, display, daysShown + 1, mylist))
						newButton.grid(row = 2, sticky='w')

						#ttk.Label(showMonth, text='%s'%(daysShown + 1), borderwidth=1, padx=5, pady=5, width=10, height=5, foreground='#CFD0C2', background='red', takefocus=1).grid(row=wk+2,column=day)
						daysShown = daysShown + 1
