# CS 361, Winter 2020, Oregon State University
## Agile Project: Iteration 2 Code
### Team 13
### (Iteration completed 2/23/2020, README last updated 2/24/2020)

## To Run The App:
Ensure your workstation or virtual environment has Python 3 installed.
Markup :  `python run.py` from your command line

## Current Functionalities:
### Application:
* Tabbed viewing to switch between Calendar and To-Do list
* Menu Bar:
  * File > Export To Do list (Coming soon),
  * File > Export Appointments (Coming soon),
  * File > Exit (Can also use shortcut CTRL + Q)
  * Theme > Dracula
  * Theme > Mint Chocolate Chip (default theme)
  * Help > About

### Calendar:
* Open, View, and Close Calendar Monthly View
* Move Forward and Backward in Calendar Monthly View
* While viewing any month, jump to current month in Calendar tab
* Click ""+"" on any date to add an appointment to that date
* Adding an appointment brings up a modal to enter title and time
* Saved appointments are displayed along with their time on the appropriate date
* Saved appointments are also stored in apptFile.json
* Opening the program loads all appointments saved in apptFile.json

### To-Do List:
* View To-Do list tasks
* Add and Remove from To-Do list
* Set priority of each task (High, Medium, Low)
* Saved tasks are also stored in taskFile.json
* Opening the program loads all tasks saved taskFile.json

## App Screenshot:
![Calendar](https://github.com/wrongenvelope/cs361-w20-app/blob/wrongenvelope/iteration2-readme/iteration_2/screenshots/it2_screenshot1.png)
