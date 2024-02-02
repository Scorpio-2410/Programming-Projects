################################################################################################################
# Project title: To Do List 
# Project description: Program that allows end-users to manage thier day to day tasks efficiently.
# Author: Nabidul Islam
# Project commencement date: 25/11/2023
# Version: V2
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
master.geometry("400x400")

userEntry = Entry(master)
userEntry.place(x=60, y=20, width=280)
userEntry.insert(0,"New Task")
userEntry.config(justify="center")

mediumRadButton =  Radiobutton(master, text="low")
mediumRadButton.place(x=80, y=60)

highRadButton =  Radiobutton(master, text="medium")
highRadButton.place(x=160, y=60)

lowRadButton =  Radiobutton(master, text="high")
lowRadButton.place(x=260, y=60)

taskBox = Listbox(master, width=50, height=14)
taskBox.place(x=50, y=100)

completeButton = tk.Button(master, text='Complete', width=10)
completeButton.place(x=60, y=350)

deleteButton = tk.Button(master, text='Delete', width=10)
deleteButton.place(x=160, y=350)

changeButton = tk.Button(master, text='Change', width=10)
changeButton.place(x=260, y=350)

userEntry.bind('<FocusIn>', onclick)


master.mainloop()
