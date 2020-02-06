import tkinter as tk
import toDoMain

# dummy function for now
def nada():
	return

class MenuBar:
    def __init__(self):
        self.__listOfTasks = []
		fileMenu = tk.Menu(self, tearoff=0)
		fileMenu.add_command(label='New', command=nada)
		fileMenu.add_command(label='Open', command=nada)
		fileMenu.add_command(label='Save', command=nada)
		fileMenu.add_separator()
		fileMenu.add_command(label='Exit', command=root.quit)
		menuBar.add_cascade(label='File', menu=fileMenu)

		helpMenu = tk.Menu(menuBar, tearoff=0)
		helpMenu.add_command(label='Help', command=nada)
		helpMenu.add_command(label='About', command=nada)
		menuBar.add_cascade(label='Info', menu=helpMenu)
