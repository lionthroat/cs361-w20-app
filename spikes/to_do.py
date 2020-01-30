############################################################
# Spike: Testing Front-End To-Do List Design
# Oregon State University, Winter 2020: CS 361, Week 4
# Agile Project: Release Cycle 1
#
# Pair Programming:
# Heather DiRuscio & Paige Enoch
# @wrongenvelope and
#
# January 29, 2020
############################################################


##### BELOW IS EXAMPLE CODE ONLY, I DID NOT WRITE THIS ######
# Source: https://www.youtube.com/watch?v=OAHLwtmdqUk

import tkinter as tk

def add_task():
    return

def rem_task():
    return

root = tk.Tk()

lbl_title = tk.Label(root, text="To-Do List", bg="white")
lbl_title.pack()

lbl_display = tk.Label(root, text="", bg="white")
lbl_display.pack()

txt_input = tk.Entry(root, width=15)
txt_input.pack()

btn_add_task = tk.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_rem_task = tk.Button(root, text="Remove task", fg="green", bg="white", command=rem_task)
btn_rem_task.pack()

root.mainloop()
