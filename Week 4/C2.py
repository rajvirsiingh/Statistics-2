# Title: RadioButton, CheckButton, ComboBox, and ListBox. 
# Description: Python GUI Programming: This code demonstrates basic Widgets RadioButton, CheckButton, ComboBox, and ListBox.
# Copyright: Rajvir Singh 
# 
# Author: Rajvir Singh
# Date: 11-08-2021
# Version: 1.00	    


import tkinter as tk
from tkinter import ttk
from tkinter import *


# Creating tkinter window 
window = tk.Tk() 
window.title('RadioButton, CheckButton, ComboBox & ListBox') 
window.geometry('500x500') 


#This function will be called when ever a radio buttion is selected to 
# declare which radio button is selected
def sel():
   selection = "You selected the option " + str(var.get())
   label2.config(text = selection)


# Dynamic Variables to convey messages 
var = IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

#label text for title
label1 = Label(window, text = "Fitness Club Membership",font = ("Helventica", 15))
label1.pack()


#Label for choosing location
label3 = Label(window, text = "Select Your city:",font = ("Times New Roman", 10))
label3.pack()

# Combobox creation
d = StringVar()
portchoosen = ttk.Combobox(window, width = 27, textvariable = d)
  
# Adding combobox drop down list
portchoosen['values'] = (' Delhi',' Haryana',' Punjab',' Chandigarh',' Himachal pradesh',' Jammu',' Mumbai',' Bangalore',' KolKata')
portchoosen.pack()
portchoosen.current()


#label for experience type
label5 = Label(window, text = "Mention Experience:",font = ("Times New Roman", 10))
label5.pack()

# Listbox creation
Lb1 = Listbox(window)

#Listbox items
Lb1.insert(1, "Newbie")
Lb1.insert(2, "Little Experienced")
Lb1.insert(3, "Amatuer")
Lb1.insert(4, "Pro")

# The radio buttons 
R1 = Radiobutton(window, text="1 Month", variable=var, value=1,command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(window, text="3 Months", variable=var, value=2,command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(window, text="6 Months", variable=var, value=3,command=sel)
R3.pack( anchor = W)

#A label to declare which radio button is selected
label2 = Label(window)
label2.pack()

 
window.mainloop()