# Project 2: Regression in Python.
# Description: A Tkinter application to calculate regression
# Copyright: Rajvir Singh Â© 2021-25-09 
# Author: Rajvir Singh
# Version: 1.00	2021-25-09 Baseline computes regression
#          1.01 2021-05-10 Data read and write features added
# importing necessary Libraries


from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog as fd
import collections, math, xlrd, openpyxl,csv, array, matplotlib.pyplot as plt, numpy as np, tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from scipy.stats import spearmanr


xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True


# Creating GUI size and title 
top = Tk()  
top.geometry("900x900")
top.title("Project 2: Regression in Python")


# global variables declared here
text = StringVar()               # dynamic variable to show the result
data = []                        # it recieves the extracted datas and puts them in the treeView
corx = []                        # it contains all the X-coordinates values
corY = []                        # it contains all the Y-coordinates values

# This functions browses through the folders and extracts X and Y coordinates from the selected .xlsx file and stores  
# the data and adds the data in treeView
def browse():
	
	name = fd.askopenfilename()
	loc = (name)
	book = xlrd.open_workbook(loc)
	worksheet = book.sheet_by_name('Sheet1') 
	worksheet = book.sheet_by_index(0) 	
	i=1
	
	while (i<11):
		a = worksheet.cell(i, 0)
		b = worksheet.cell(i, 1)
		print(" ", int(a.value), " ", int(b.value)) #, " ", int(mrks.value))		
		data.append((int(a.value),int(b.value)))
		corx.append(int(a.value))
		corY.append(int(b.value))
		i=i+1
	
	for d in data:
		tree.insert('', tk.END, values=d)
	
	def item_selected(event):
		for selected_item in tree.selection():
			# dictionary
			item = tree.item(selected_item)
			# list
			record = item['values']
			showinfo(title='Information',message=','.join(record))
	tree.bind('<<TreeviewSelect>>', item_selected)


# This function computes linear regression, finds the regression coefficients and then prints
# the result in the result area. 
def cofficient():
	i=0
	sumAB=0
	sumA=0
	sumB=0
	sumA2=0
	sumB2=0
	while(i<10):
		sumA += corx[i]
		sumB += corY[i]
		sumA2 += (corx[i]*corx[i])
		sumB2 += (corY[i]*corY[i])
		sumAB += (corx[i]*corY[i])
		i = i+1
	nEab= sumAB*10
	nEa2= sumA2*10
	EaEb= sumA*sumB
	nEb2 = sumB2*10
	Ea2 = sumA*sumA
	Eb2 = sumB*sumB
	B_ab=(nEab-sumA*sumB)/(nEb2-Eb2)
	B_ab=round(B_ab,2-int(math.floor(math.log10(abs(B_ab))))-1)
	B_ba=(nEab-sumA*sumB)/(nEa2-Ea2)
	B_ba=round(B_ba,2-int(math.floor(math.log10(abs(B_ba))))-1)
	result="Regression x on y: "+str(B_ab)+"\nRegression y on x: "+str(B_ba)
	text.set(result)
	field = ['B_ab','B_ba']
	row=[[B_ab],[B_ba]]
	filename = "Regression coefficients.csv"	# name of csv file
	with open(filename, 'w') as csvfile:	# writing to csv file
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(field)
		csvwriter.writerow(row)


#This function graphically represents the datas in a line graph 
def linegraph():
	plt.plot(corx,corY,color='blue')
	plt.xlabel('x-values')
	plt.ylabel('y-values')
	plt.title('line plot')
	plt.show()
	plt.place(x=50,y=370)


#This function represents data in form of pie-chart
def pie():
	plt.subplot(211)
	plt.pie(corx)
	plt.subplot(212)
	plt.pie(corY)
	plt.title('Pie Chart')
	plt.show()


#this title is for giving hint to the user
heading = Label(top, text = "Select the data file .xls/.xlsx")
heading.config(font=('Helvetica bold',20))
heading.place(x = 100,y = 10)


#this label shows the results after every calculation
res = Label(top, text = "", textvariable=text, fg='#00008b',font=('Helvetica bold',15)).place(x=50,y=400)
text.set("The Result will be shown here")


# columns for the treeView
columns = ('#1', '#2')


#Creating tree
tree = ttk.Treeview(top, columns=columns, show='headings')


# The headings of the column are defined here
tree.heading('#1', text='X Coordinates')
tree.heading('#2', text='Y coordinates')
tree.place(x=50,y=100,width=400,height=250)      #the position and size of the tree is declared here


#this button calls the browse function which is used to select file by the user
browseButton = Button(top, text = "Browse File",command=browse).place(x=200, y=350)


#This button calls the cofficient() method which computes regression coefficients 
coeffButton = Button(top, text = "Regression Coefficients",command=cofficient).place(x = 50, y = 450,width=150)


#This button graphically represents the datas in a linegraph
lineButton = Button(top, text = "Line-Graph", command= linegraph).place(x = 50, y = 500,width=150)


#This button graphically represents the datas in a Pie-graph
pieButton = Button(top, text = "Pie Graph", command=pie).place(x = 300, y = 500,width=150)


#This button closes or destrys the GUI
ExitButton= Button(top, text = "EXIT", fg='#ff0000', command = top.destroy).place(x=240,y =550)


#This runs the application
top.mainloop()  