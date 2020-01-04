# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO COPY OR MOVE FILES FROM ONE DIRECTORY TO ANOTHER DIRECTORY USING THE shutil MODULE
#
# The shutil module offers a number of high-level operations on files and collections of files.
# In particular, functions are provided which support file copying and removal.
#
# shutil.copy(src, dst, *, follow_symlinks=True) - Copies the file src to the file or directory dst.
# src and dst should be strings. If dst specifies a directory, the file will be copied into dst using
# the base filename from src. Returns the path to the newly created file.
#
# shutil.move(src, dst, copy_function=copy2) - Recursively move a file or directory (src) to another
# location (dst) and return the destination.

# Importing necessary packages
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    linkLabel = Label(root, text="SELECT THE FILE TO COPY : ", bg="deepskyblue4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    source_browseButton = Button(root, text="BROWSE", command=SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3, pady=5, padx=5)

    destinationLabel = Label(root, text="SELECT THE DESTINATION : ", bg="deepskyblue4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=50, textvariable=destinationLocation)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5, columnspan = 2)

    dest_browseButton = Button(root, text="BROWSE", command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=2, column=3, pady=5, padx=5)

    copyButton = Button(root, text="COPY FILE", command=CopyFile, width=15)
    copyButton.grid(row=3, column=1, pady=5, padx=5)

    moveButton = Button(root, text="MOVE FILE", command=MoveFile, width=15)
    moveButton.grid(row=3, column=2, pady=5, padx=5)

def SourceBrowse():
    # Opening the file-dialog directory prompting the user to select files to copy using
    # filedialog.askopenfilenames() method. Setting initialdir argument is optional
    # Since multiple files may be selected, converting the selection to list using list()
    root.files_list = list(filedialog.askopenfilenames(initialdir="/Users/abhijithwarrier/Documents/PythonExample"))

    # Displaying the selected files in the root.sourceText Entry using root.sourceText.insert()
    root.sourceText.insert('1', root.files_list)

def DestinationBrowse():
    # Opening the file-dialog directory prompting the user to select destination folder to
    # which files are to be copied using the filedialog.askopendirectory() method.
    # Setting initialdir argument is optional
    destinationdirectory = filedialog.askdirectory(initialdir="/Users/abhijithwarrier/Documents/PythonExample")

    # Displaying the selected directory in the root.destinationText Entry using root.destinationText.insert()
    root.destinationText.insert('1', destinationdirectory)

def CopyFile():
    # Retrieving the source file selected by the user in the SourceBrowse() and storing it in a
    # variable named files_list
    files_list = root.files_list

    # Retrieving the destination location from the textvariable using destinationLocation.get() and
    # storing in destination_location
    destination_location = destinationLocation.get()

    # Looping through the files present in the list
    for f in files_list:
        # Copying the file to the destination using the copy() of shutil module
        # copy take the source file and the destination folder as the arguments
        shutil.copy(f, destination_location)

    messagebox.showinfo("SUCCESS", "FILES COPIED SUCCESSFULLY")

def MoveFile():
    # Retrieving the source file selected by the user in the SourceBrowse() and storing it in a
    # variable named files_list
    files_list = root.files_list

    # Retrieving the destination location from the textvariable using destinationLocation.get() and
    # storing in destination_location
    destination_location = destinationLocation.get()

    # Looping through the files present in the list
    for f in files_list:
        # Moving the file to the destination using the move() of shutil module
        # copy take the source file and the destination folder as the arguments
        shutil.move(f, destination_location)

    messagebox.showinfo("SUCCESS", "FILES MOVED SUCCESSFULLY")

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color disabling the resizing property
root.geometry("830x120")
root.title("FILES COPY-MOVE APP")
root.config(background = "deepskyblue4")

# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
