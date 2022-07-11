import tkinter
ROOT = tkinter.Tk()
ROOT.withdraw()
from tkinter import simpledialog
b= simpledialog.askstring(title="HEIGHT AND WEIGHT INDEX" ,prompt="WEIGHT(Kg):")
c= simpledialog.askstring(title="HEIGHT AND WEIGHT INDEX", prompt="HEIGHT(meter with dot):")
b=float(b)
c=float(c)
formula=float((b)/(c**2))

r1=18.4>=formula>=0
if r1 is True: tkinter.messagebox.showwarning(title="WEIGHT",message="THIN")
r2=24.9>=formula>=18.5
if r2 is True: tkinter.messagebox.showwarning(title="WEIGHT",message="FAT")
r3=29.9>=formula>=25
if r3 is True: tkinter.messagebox.showwarning(title="WEIGHT",message="OVERWEIGHT")
r4=34.9>=formula>=30
if r4 is True: tkinter.messagebox.showwarning(title="WEIGHT",message="OBESE")




    



