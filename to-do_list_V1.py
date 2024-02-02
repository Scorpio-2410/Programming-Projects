################################################################################################################
# Project title: To Do List 
# Project description: Program that allows end-users to manage thier day to day tasks efficiently.
# Author: Nabidul Islam
# Project commencement date: 25/11/2023
# Version: V1
# ##############################################################################################################


# Import libraries
import tkinter as tk
from tkinter import *


def onclick(event):
    if userEntry.get() == "New Task":
        userEntry.delete(0, "end") 

""" New Task
def addTask():
    task = getNewTask()
    addTaskToList(task)
    clearInput()

def selectTask()
    task = getSelectedTask()
    markCompletedTask(task)

def deleteTask()
    task = getSelectedTask()
    deleteTask(task)
"""

master=tk.Tk()
master.title("Task Scheduler")
master.geometry("300x300")

userEntry = Entry(master)
userEntry.place(x=60, y=20, width=200)
userEntry.insert(0,"New Task")
userEntry.config(justify="center")

Checkbutton(master, text="option", variable=IntVar()).place(x=50, y=70)

deleteButton = tk.Button(master, text='Delete', width=5)
deleteButton.place(x=130, y=250)

userEntry.bind('<FocusIn>', onclick)


master.mainloop()
