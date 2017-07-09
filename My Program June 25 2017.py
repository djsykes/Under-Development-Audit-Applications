# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:42:39 2017

@author: jmsyk
"""

from tkinter import *
from tkinter import filedialog

window=Tk()

def getfile():
    filename = filedialog.askopenfilename(filetypes= (("HowCode files", "*.hc"),("All Files","*.*")))
    t1.insert(END,filename)

def getloc():
    fileloc = filedialog.askdirectory()
    t2.insert(END,fileloc)

b1=Button(window, text="Input File", command=getfile,width=15)
b1.grid(row=1, column=0)

b2=Button(window, text="Output Location", command=getloc,width=15)
b2.grid(row=2, column=0)

b3=Button(window, text="Execute Action",width=15)
b3.grid(row=3, column=0)

t1=Text(window, height=1, width=60)
t1.grid(row=1,column=2)

t2=Text(window, height=1, width=60)
t2.grid(row=2,column=2)

label1=Label(window, text="Purpose:", height=1, width=15)
label1.grid(row=0,column=0)

label2=Label(window, text="To check for duplicates based on the fields indicated by user.", height=1, width=60)
label2.grid(row=0,column=2)

window.mainloop()

