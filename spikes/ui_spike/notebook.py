from tkinter.ttk import *
import tkinter.ttk as ttk
from todoApp import AppToDoList
from calendarApp import AppCalendar

class AppTabs(ttk.Notebook):
    def __init__(self, parent):
        ttk.Notebook.__init__(self, width=770, height=630, padding=10) # instantiate ttk Notebook() widget
        self.enable_traversal() # enables keyboard shortcuts for tabs if fully implemented
        
        todo_widget = AppToDoList(self)
        todo_widget.grid()
        cal_widget = AppCalendar(self)
        cal_widget.grid()

        self.add(cal_widget, text='Calendar')
        self.add(todo_widget, text='To-Do List') # sticky to position content inside tab
        self.grid()
