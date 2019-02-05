
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import step_122_main

# center window on user's screen
def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# define gride size (3x3) and weight all cells
def grid_size(self,master):
    rows = 0
    while rows < 3:
        master.rowconfigure(rows,weight=1)
        master.columnconfigure(rows,weight=1)
        rows += 1

# open dialog box and search for file, print file path to GUI window
def askdirectory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        txt_Results.configure(text=dir_path)
    print(dir_path)


if __name__ == "__main__":
    pass
