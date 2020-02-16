from tkinter.ttk import *
import tkinter.ttk as ttk
from functools import partial
from datetime import datetime
import calendar as cal

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

        # Calendar Navigation Buttons
        calNav = ttk.LabelFrame(self, labelanchor='n', style='calNav.TLabelframe')
        calNav.grid(row=1, columnspan=7)

        prevMonthBtn = ttk.Button(calNav, text=' <= Prev ', command=partial(self.prevMonth, current, display)).grid(row=2,column=1, sticky='w')
        currMonthBtn = ttk.Button(calNav, text=' Current ', command=partial(self.currMonth, current, display)).grid(row=2,column=2, sticky='n')
        nxtMonthBtn = ttk.Button(calNav, text=' Next => ', command=partial(self.nextMonth, current, display)).grid(row=2,column=3, sticky='e',)

        self.drawMonth

    def currMonth(self, current, display):
    	display['year'] = current['year']
    	display['month'] = current['month']
    	self.drawMonth
    	return

    def nextMonth(self, current, display):
    	if display['month'] == 12:
    		display['year'] += 1
    		display['month'] = 1
    	else:
    		display['month'] += 1
    	self.drawMonth
    	return

    def prevMonth(current, display):
    	if display['month'] == 1:
    		display['year'] -= 1
    		display['month'] = 12
    	else:
    		display['month'] -= 1
    	self.drawMonth
    	return

    def drawMonth(self):
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
    					dayBlock.append(ttk.LabelFrame(showMonth, text=daysShown, style='dayBlock.TLabelframe'))
    					dayBlock[daysShown].configure(text='%s'%(daysShown + 1), borderwidth=0, width=105, height=100)
    					dayBlock[daysShown].grid(row=wk+3,column=day)
    					#ttk.Label(showMonth, text='%s'%(daysShown + 1), borderwidth=1, padx=5, pady=5, width=10, height=5, foreground='#CFD0C2', background='red', takefocus=1).grid(row=wk+2,column=day)
    					daysShown = daysShown + 1
