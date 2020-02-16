#########################################################################
# File: style.py
# Function: This holds all of the main styling for the program, including
#   colors, padding, any stylistic choices
# Last Modified: 16 February 2020
########################################################################
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk

# Color Palette for dracula theme
holo_green = '#d2ffd2'
monster_green = '#50fa7b'
dk_blue_grey='#282a36'
med_blue_grey = '#44475a'
lt_med_blue_grey = '#515366'
lt_grey = '#f8f8f2'
neon_yellow = '#f1fa8c'
lt_red = '#ff5555'
cyan = '#8be9fd'

class AppStyle(ttk.Style):
    def __init__(self, parent):
        ttk.Style.__init__(self) # instantiate Style() widget
        self.theme_create('dracula', parent='alt', settings=
        	{
        	    'TNotebook': {
        			'configure': {
        				'tabmargins': [2, 5, 2, 0],
        				'background': dk_blue_grey, # tab bar bg color
        				'relief': 'flat'
        			}
        		},
        	    'TNotebook.Tab': {
        	        'configure': {
        				'padding': [50, 10], # [x-padding, y-padding for tab labels]
        				'background': holo_green, # bg for deselected tab labels
        				'foreground': med_blue_grey, # text color for tabs
        				'font': ('Lucida Console', 11), # example: ('Arial', 12, 'bold')
        				'focuscolor': med_blue_grey
        			},
        	        'map': {
        				'background': [('selected', med_blue_grey)], # selected tab bg color
        				'foreground': [('selected', monster_green)], # text color for selected tabs
        	            'expand': [('selected', [1, 1, 1, 0])], # what is this??
        			}
        		},
        		'TLabel': {
        			'configure': {'background': med_blue_grey, 'foreground': lt_grey}
        		},
        		'TFramelabel': {
        			'configure': {'background': dk_blue_grey, 'foreground': lt_grey}
        		},
        		'TButton': {
        			'configure': {
        				'background': lt_med_blue_grey, # default button bg color
        				'foreground': lt_grey,
        				'focuscolor': lt_med_blue_grey,
        			},
        			'map': {
        		    	'foreground': [('pressed', med_blue_grey), ('active', dk_blue_grey)],
        		    	'background': [
        					('pressed', '!disabled', 'readonly', med_blue_grey),
        					('active', holo_green)
        				],
        				'focuscolor': [
        					('active', holo_green),
        					('pressed', '!disabled', 'readonly', med_blue_grey)
        				],
        			}
        		},
                'newTask.TButton': {
                    'configure': {
                        'padding': [40, 3],
                        'background': cyan,
                        'font': ('Lucida Console', 14, 'bold'),
                        'relief': 'ridge',
                        'borderwidth': 2,
                    }
                },
                'Treeview': {
                    'configure': {
                        'background': lt_grey,
                        'fieldbackground': lt_grey,
                        'padding': [2,2]
                    },
                    'map': {
                        'background': [
                            ('selected', cyan) # active item on to-do list
                        ]
                    }
                },
        		'taskBlock.TLabelframe.Label': {
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': lt_grey,
        				'font': ('Lucida Console', 11, 'bold'),
        			}
        		},
        		'taskBlock.TLabelframe': {
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': med_blue_grey,
        				'padding': [50, 50], # x and y padding that places the to-do list
        			},
        		},
                'TEntry': {
                    'configure': {
                        # 'fieldbackground': neon_yellow,
                        'bordercolor': monster_green,
                        'foreground': dk_blue_grey,
                        'padding': [5,5],
                        'font': ('Lucida Console', 11, 'bold')
                    }
                },
                'TCombobox': {
                    'configure': {
                        # 'fieldbackground': neon_yellow,
                        'bordercolor': monster_green,
                        'foreground': dk_blue_grey,
                        'padding': [5,5],
                        'font': ('Lucida Console', 11, 'bold')
                    }
                },
        		'monthBlock.TLabelframe.Label': { # style of month title
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': lt_grey,
        				'font': ('Lucida Console', 11, 'bold')
        			}
        		},
        		'monthBlock.TLabelframe': {
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': lt_grey,
        				'padding': [15, 15], # x and y padding that places the calendar
        			},
        		},
        		'monthBlock.TLabel': {
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': lt_grey
        			},
        		},
        		'calNav.TLabelframe.Label': {
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': med_blue_grey,
        			}
        		},
        		'calNav.TLabelframe': {
        			'configure': {
        				'background': med_blue_grey,
        				'foreground': med_blue_grey,
        				'padding': [10, 10] # position frame containing calendar navigation buttons
        			}
        		},
        		'dayBlock.TLabelframe': {
        			'configure': {
        				'background': lt_med_blue_grey, # bg color for each day block
        				# 'relief': 'ridge' # for different dayBlock border styles
        				'labelmargins': 15 # tweak placement of calendar numbers
        			}
        		},
        		'dayBlock.TLabelframe.Label': { # calendar numbers for each day
        			'configure': {
        				'background': lt_med_blue_grey, # color immediately surrounding num
        				'foreground': lt_grey, # font color
        			}
        		},
        		'dayBlock.TLabel': { # style of entries on a calendar day
        			'configure': {
        				'background': med_blue_grey,
        			}
        		},
        		'nullDay.TLabel': {
        			'configure': {
        				'background': med_blue_grey,
        			}
        		}
        	}
        )
        self.theme_use('dracula')
