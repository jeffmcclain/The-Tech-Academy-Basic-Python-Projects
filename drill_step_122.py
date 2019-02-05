# Python Version:   3.7.1
#
# Author:           Jeff McClain
#
# Description:      - Python Drill Step 122 -
#                   Write a script that creates a GUI with a button widget
#                   and a text widget. The script will also include a function
#                   that when called will invoke a dialog modal which will
#                   allow users to select a folder directory from their system.
#                   The script will also show the user's selected directory
#                   path within the text field.
#
# Requirements:     -Script will need to use Python 3 and Tkinter module.
#                   -Script will need to use askdirectory() method from
#                   Tkinter module.
#                   -Script will need to have a function linked to the button
#                   widget so that once the button has been clicked it will
#                   take the user's selected file path retained by the
#                   askdirectory() method and print it within your GUI's
#                   text widget.


from tkinter import *
import tkinter as tk

#import program specific function
import step122_fileSearch_func








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
