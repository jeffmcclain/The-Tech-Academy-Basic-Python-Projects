# Python Version:   3.7.1
#
# Author:           Jeff McClain
#
# Purpose:          The Tech Academy - Drill for Step 121.
#                   Write a script that creates a GUI, using
#                   Python 3 and the Tkinter module.


from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        # create window
        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(700,250))
        self.master.title('Check files')
        self.master.config(bg='#DCDCDC')

        # this loop defines grid size, giving weight to all cells (empty or not)
        rows = 0
        while rows < 4:          
            master.rowconfigure(rows,weight=1)
            master.columnconfigure(rows,weight=1)
            rows += 1

        # create buttons
        self.btnBrowse1 = Button(self.master,width=15,height=1,text='Browse...',font=('Helvetica',12),fg='black',bg='#DCDCDC')
        self.btnBrowse1.grid(row=1,column=0,padx=(30,0),pady=(50,0),sticky=N+W)
        self.btnBrowse2 = Button(self.master,width=15,height=1,text='Browse...',font=('Helvetica',12),fg='black',bg='#DCDCDC')
        self.btnBrowse2.grid(row=2,column=0,padx=(30,0),sticky=N+W)
        self.btnCheck = Button(self.master,width=15,height=2,text='Check for files...',font=('Helvetica',12),fg='black',bg='#DCDCDC')
        self.btnCheck.grid(row=3,column=0,padx=(30,0),pady=(0,20),sticky=N+W)
        self.btnClose = Button(self.master,width=15,height=2,text='Close Program',font=('Helvetica',12),fg='black',bg='#DCDCDC')
        self.btnClose.grid(row=3,column=4,padx=(0,20),pady=(0,20),sticky=E)

        # create textboxes
        self.txtBrowse1 = Entry(self.master,width=50,text='')
        self.txtBrowse1.grid(row=1,column=1,columnspan=4,padx=(0,20),pady=(50,20),sticky=W+E+N+S)
        self.txtBrowse2 = Entry(self.master,width=50,text='')
        self.txtBrowse2.grid(row=2,column=1,columnspan=4,padx=(0,20),pady=(0,15),sticky=W+E+N+S)

        






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
