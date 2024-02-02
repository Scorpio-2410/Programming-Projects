#################################################################################################################
# Project title: To Do List 
# Project description: Program that allows end-users to manage thier day to day tasks efficiently.
# Author: Nabidul Islam
# Project commencement date: 25/11/2023
# Version: V4
# ###############################################################################################################


# Import libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def onclick(event):
    if userEntry.get() == "New Task":
        userEntry.delete(0, "end")

def addTask(event):
    if userEntry.get() == "New Task" or userEntry.get() == "" or r.get()==0:
        messagebox.showerror("Error", "Enter Task or add priority")
        
    else:
        newTask = userEntry.get()
        if r.get()==1:
            taskBox.insert(END, newTask)
            taskBox.itemconfig(END,{'fg': 'green'})
        if r.get()==2:
            index = int(taskBox.size() / 2) + taskBox.size() % 2
            taskBox.insert(index, newTask)
            taskBox.itemconfig(index, {'fg': 'yellow'})
        if r.get()==3:
            taskBox.insert(0, newTask)
            taskBox.itemconfig(0,{'fg': 'red'})
        userEntry.delete(0, "end")
        r.set(0)

def completeTask():
    selectTask = taskBox.curselection()
    if not selectTask:
        messagebox.showerror("Error", "Select a task to complete")
        return
    taskBox.delete(selectTask)

def changeTask():
    selectTask = taskBox.curselection()
    if not selectTask:
        messagebox.showerror("Error", "Select a task to change")
        return
    getTask = taskBox.get(selectTask)
    userEntry.insert(0, getTask)
    taskBox.delete(END, selectTask)

master=tk.Tk()
master.title("Task Scheduler")
master.geometry("400x400")
userEntry = Entry(master)
userEntry.place(x=60, y=20, width=280)
userEntry.insert(0,"New Task")
userEntry.config(justify="center")

# IntVar function in Tkinter allows to track changes
r = IntVar()

lowRadButton =  Radiobutton(master, text="low", variable=r, value=1)
lowRadButton.place(x=80, y=60)

mediumRadButton =  Radiobutton(master, text="medium", variable=r, value=2)
mediumRadButton.place(x=160, y=60)

highRadButton =  Radiobutton(master, text="high", variable=r, value=3)
highRadButton.place(x=260, y=60)

taskBox = Listbox(master, width=50, height=14)
taskBox.place(x=50, y=100)

completeButton = tk.Button(master, text='Complete', width=10, command=completeTask)
completeButton.place(x=80, y=350)

changeButton = tk.Button(master, text='Change', width=10, command=changeTask)
changeButton.place(x=240, y=350)

userEntry.bind('<FocusIn>', onclick)
userEntry.bind("<Return>", addTask)

taskBox.bind("<<ListboxSelect>>")

master.mainloop()
