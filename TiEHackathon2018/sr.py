from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import os
import sys
import sqlite3
from tabulate import tabulate

root = Tk()



Label(root, text="Red Sun", bg="red", fg="white").pack()
Label(root, text="Green Grass", bg="green", fg="black").pack()
Label(root, text="Blue Sky", bg="blue", fg="white").pack()


conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Water_Department')
cur.execute('''CREATE TABLE Water_Department (Name TEXT, Contact INTEGER, water_unit INTEGER, Region TEXT, water_cost INTEGER)''')
#################################################################################################################
water_cost=list()
fname = 'new_sample.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('NCWR: '): continue
    name_pieces = line.split()
    name_pieces[3]
    if (int(name_pieces[3])<20):
    	price=20

    else:
    	price=20+((int(name_pieces[3])-20)*2.5)


    cur.execute('''INSERT INTO Water_Department (Name, Contact, water_unit, Region, water_cost) 
        VALUES (?, ?, ?, ?, ?)''', (name_pieces[1], name_pieces[2], name_pieces[3], name_pieces[4], price))
    
conn.commit()
a=list()
bar=cur.execute('''SELECT * FROM Water_Department ORDER BY Region, water_cost Asc''')
for i in bar:
	a.append(i)
	#if i[4] > 20:
	#	print ("your water consumption has rised up")

print(tabulate(a, headers=['Name', 'Contact', 'water_unit', 'Region', 'water_cost']))	





