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


import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog

#import program specific function
'''import step_122_func'''




class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        global dir_path
        
        
        dir_path = tk.StringVar()
        
        # define master frame config
        self.master = master
        self.master.minsize(700,200)
        self.master.maxsize(700,200)
        self.master.title('OPEN')
        self.master.config(bg='#E3E3E3')
        # call function to center window in user's screen
        center_window(self,700,200)
        # call function to define grid
        grid_size(self,master)            
        # create text field and buttons
        self.txt_Results = Entry(self.master,textvariable=dir_path)
        self.txt_Results.grid(row=1,column=0,columnspan=3,padx=(70,20),pady=(15,15),sticky=N+S+E+W)
        self.btn_Browse = Button(self.master,width=12,text='Browse...',font=('Helvetica',12),fg='#000',bg='#fff',command= lambda: askdirectory(self.txt_Results))
        self.btn_Browse.grid(row=0,column=0,padx=(35,0),pady=(30,0),sticky=S+W)
        self.btn_Clear = Button(self.master,width=10,height=2,text='Clear',font=('Helvetica',12),fg='#000',bg='#fff',command=delete_text(self.txt_Results))
        self.btn_Clear.grid(row=2,column=2,padx=(0,20),pady=(10,10),sticky=N+E)
        
                
        


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
def askdirectory(Results):
    dir_path = filedialog.askdirectory()
    Results.insert(10,dir_path)
    print(dir_path)

def delete_text(Results):
        self.txt_Results.delete('')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
