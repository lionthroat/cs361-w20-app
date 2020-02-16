from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk

# Color Palette for Mint Chocolate Chip theme
white            = '#FFFFFF'
super_light_gray = '#F5F5F5'
light_gray       = '#EBEBEB'
medium_gray      = '#C7C4C3'
dark_gray        = '#8E8E8E'
darkest_gray     = '#3F4141'
mint_green       = '#D2FFDF'
icy_blue         = '#8DF9FA'

# Color Palette for dracula theme
holo_green       = '#d2ffd2'
monster_green    = '#50fa7b'
dk_blue_grey     = '#282a36'
med_blue_grey    = '#44475a'
lt_med_blue_grey = '#515366'
lt_grey          = '#f8f8f2'
neon_yellow      = '#f1fa8c'
lt_red           = '#ff5555'
cyan             = '#8be9fd'

class AppStyle(ttk.Style):
    def __init__(self, parent):
        ttk.Style.__init__(self) # instantiate Style() widget
        self.theme_create('mintChocolateChip', parent='alt', settings=
        	{
        	    'TNotebook': {
        			'configure': {
        				'tabmargins': [2, 5, 2, 0],
        				'background':  light_gray, # tab bar bg color
        				'relief': 'groove',

        			}
        		},
        	    'TNotebook.Tab': {
        	        'configure': {
        				'padding': [50, 10], # [x-padding, y-padding for tab labels]
        				'background': mint_green, # bg for deselected tab labels
        				'foreground': darkest_gray, # text color for tabs
        				'font': ('Open Sans', 10, 'bold'), # example: ('Arial', 12, 'bold')
        				'focuscolor': white,
        				'relief': 'groove'
        			},
        	        'map': {
        				'background': [('selected', white)], # selected tab bg color
        				'foreground': [('selected', darkest_gray)], # text color for selected tabs
        			}
        		},
        		'TLabel': {
        			'configure': {
                        'background': 'white',
                        'foreground': dark_gray
                        }
        		},
        		'TFramelabel': {
        			'configure': {'background': 'white', 'foreground': dark_gray}
        		},
        		'TButton': {
        			'configure': {
        				'background': 'white', # default button bg color
        				'foreground': dark_gray,
        				'focuscolor': white,
        			},
        			'map': {
        		    	'foreground': [('pressed', darkest_gray), ('active', darkest_gray)],
        		    	'background': [
        					('pressed', '!disabled', 'readonly', medium_gray),
        					('active', mint_green)
        				],
        				'focuscolor': [
        					('active', mint_green),
        					('pressed', '!disabled', 'readonly', white)
        				],
        			}
        		},
                'newTask.TButton': {
                    'configure': {
                        'padding': [40, 3],
                        'background': mint_green,
                        'font': ('Open Sans', 14, 'bold'),
                        'relief': 'flat',
                        'borderwidth': 2,
    				    'labelmargins': 10,
                    }
                },
                'saveBtn.TButton': {
                    'configure': {
                        'padding': [20, 30],
                        'background': mint_green,
                        'foreground': darkest_gray,
                        'font': ('Open Sans', 13, 'bold'),
                        'relief': 'flat',
                        'borderwidth': 2,
    				    'labelmargins': 10,
                        'focuscolor': mint_green,
                    },
        			'map': {
        		    	'foreground': [('pressed', darkest_gray), ('active', darkest_gray)],
        		    	'background': [
        					('pressed', '!disabled', 'readonly', cyan),
        					('active', cyan)
        				],
        				'focuscolor': [
        					('active', cyan),
        					('pressed', '!disabled', 'readonly',cyan)
        				],
                    }
                },
                'showButton.TButton': {
                    'configure': {
                        #'padding': [20, 30],
                        'background': mint_green,
                        'foreground': darkest_gray,
                        'font': ('Open Sans', 8, 'bold'),
                        'relief': 'flat',
                        'borderwidth': 2,
    				    'labelmargins': 10,
                        'focuscolor': mint_green,
                    },
        			'map': {
        		    	'foreground': [('pressed', darkest_gray), ('active', darkest_gray)],
        		    	'background': [
        					('pressed', '!disabled', 'readonly', cyan),
        					('active', cyan)
        				],
        				'focuscolor': [
        					('active', cyan),
        					('pressed', '!disabled', 'readonly',cyan)
        				],
                    }
                },
                'Treeview': {
                    'configure': {
                        'background': 'white',
                        'fieldbackground': 'white',
                        'padding': [2,2]
                    },
                    'map': {
                        'background': [
                            ('selected', mint_green) # active item on to-do list
                        ]
                    }
                },
        		'taskBlock.TLabelframe.Label': {
        			'configure': {
        				'background': 'white',
        				'foreground': dark_gray,
        				'font': ('Open Sans', 11, 'bold'),
        			}
        		},
        		'taskBlock.TLabelframe': {
        			'configure': {
        				'background': 'white',
        				'foreground': medium_gray,
        				'padding': [50, 50], # x and y padding that places the to-do list
        			},
        		},
                'TEntry': {
                    'configure': {
                        'bordercolor': mint_green,
                        'foreground': dark_gray,
                        'padding': [5,5],
                        'font': ('Open Sans', 11)
                    }
                },
                'TCombobox': {
                    'configure': {
                        'bordercolor': mint_green,
                        'foreground': dark_gray,
                        'padding': [5,5],
                        'font': ('Open Sans', 11, 'bold')
                    }
                },
        		'monthBlock.TLabelframe.Label': { # style of month title
        			'configure': {
        				'background': 'white',
        				'foreground': darkest_gray,
        				'font': ('Open Sans', 13, 'bold')
        			}
        		},
        		'monthBlock.TLabelframe': {
        			'configure': {
        				'background': 'white', # calendar background color
        				'padding': [15, 15], # x and y padding that places the calendar
        			},
        		},
        		'calNav.TLabelframe.Label': {
        			'configure': {
        				'background': 'white',
        				'foreground': medium_gray,
        			}
        		},
        		'calNav.TLabelframe': {
        			'configure': {
        				'background': 'white',
        				'foreground': 'white',
        				'padding': [10, 10] # position frame containing calendar navigation buttons
        			}
        		},
        		'timeInput.TLabelframe.Label': {
        			'configure': {
        				'background': super_light_gray,
        				'foreground': medium_gray,
        			}
        		},
        		'timeInput.TLabelframe': {
        			'configure': {
        				'background': super_light_gray,
        				'foreground': 'white',
        				'padding': [10, 10] # position frame containing calendar navigation buttons
        			}
        		},
        		'dayBlock.TLabelframe': {
        			'configure': {
        				'background': 'white', # bg color for each day block
        				'relief': 'solid', # for different dayBlock border styles
        				'labelmargins': 1, # tweak margins around calendar numbers
                        'padding': [2,2] # add padding to content within a calendar block
        			}
        		},
        		'dayBlock.TLabelframe.Label': { # calendar numbers for each day
        			'configure': {
        				'background': white, # color immediately surrounding num
        				'foreground': dark_gray, # font color for calendar numbers
        				'font': ('Open Sans', 9, 'bold')
        			}
        		},
        		'dayBlock.TLabel': { # style of entries on a calendar day
        			'configure': {
        				'background': 'white',
        			}
        		},
        		'todayBlock.TLabelframe': {
        			'configure': {
        				'background': mint_green, # bg color for each day block
        				'relief': 'solid', # for different dayBlock border styles
        				'labelmargins': 1, # tweak margins around calendar numbers
                        'padding': [2,2] # add padding to content within a calendar block
                        #'bordercolor': mint_green
        			}
        		},
        		'todayBlock.TLabelframe.Label': { # calendar numbers for each day
        			'configure': {
        				'background': mint_green, # color immediately surrounding num
        				'foreground': darkest_gray, # font color for today's date
        				'font': ('Open Sans', 9, 'bold'),
        			}
        		},
        		'todayBlock.TLabel': { # style of entries on a calendar day
        			'configure': {
        				'background': mint_green
        			}
        		},
        		'pastBlock.TLabelframe': {
        			'configure': {
        				'background': white, # bg color for each day block
        				'relief': 'solid', # for different dayBlock border styles
        				'labelmargins': 1, # tweak margins around calendar numbers
                        'padding': [2,2] # add padding to content within a calendar block
        			}
        		},
        		'pastBlock.TLabelframe.Label': { # calendar numbers for each day
        			'configure': {
        				'background': white, # color immediately surrounding num
        				'foreground': light_gray, # font color for calendar numbers
        				'font': ('Open Sans', 9, 'bold')
        			}
        		},
        		'pastBlock.TLabel': { # style of entries on a calendar day
        			'configure': {
        				'background': white,
        			}
        		},
        		'nullDay.TLabel': {
        			'configure': {
        				'background': 'white',
        			}
        		}
        	}
        )
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
        		'timeInput.TLabelframe.Label': {
        			'configure': {
        				'background': super_light_gray,
        				'foreground': medium_gray,
        			}
        		},
        		'timeInput.TLabelframe': {
        			'configure': {
        				'background': super_light_gray,
        				'foreground': 'white',
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
        		'todayBlock.TLabelframe': {
        			'configure': {
        				'background': lt_med_blue_grey, # bg color for each day block
        				# 'relief': 'ridge' # for different dayBlock border styles
        				'labelmargins': 15 # tweak placement of calendar numbers
        			}
        		},
        		'todayBlock.TLabelframe.Label': { # calendar numbers for each day
        			'configure': {
        				'background': lt_med_blue_grey, # color immediately surrounding num
        				'foreground': lt_grey, # font color
        			}
        		},
        		'todayBlock.TLabel': { # style of entries on a calendar day
        			'configure': {
        				'background': med_blue_grey,
        			}
        		},
        		'pastBlock.TLabelframe': {
        			'configure': {
        				'background': lt_med_blue_grey, # bg color for each day block
        				# 'relief': 'ridge' # for different dayBlock border styles
        				'labelmargins': 15 # tweak placement of calendar numbers
        			}
        		},
        		'pastBlock.TLabelframe.Label': { # calendar numbers for each day
        			'configure': {
        				'background': lt_med_blue_grey, # color immediately surrounding num
        				'foreground': lt_grey, # font color
        			}
        		},
        		'pastBlock.TLabel': { # style of entries on a calendar day
        			'configure': {
        				'background': 'red',
        			}
        		},
        		'nullDay.TLabel': {
        			'configure': {
        				'background': med_blue_grey,
        			}
        		}
        	}
        )

        # IMPORTANT!!! THIS LINE SETS DEFAULT THEME
        self.theme_use('mintChocolateChip')
