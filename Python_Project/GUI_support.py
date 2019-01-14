#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
'''Please run this py file in windows operation system, it may have some small
   format problems when running in osx'''
import os
import sys
import pandas as pd
import numpy as np
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
'''Function to generate Tk_var'''

def set_Tk_var():
    global entry
    entry = StringVar()
    global list1
    list1 = StringVar()
    global list2
    list2 = StringVar()
    global list3
    list3 = StringVar()
    global var2
    var2 = StringVar()
    global var3
    var3 = StringVar()
    global var1
    var1 = StringVar()
    global var4
    var4 = StringVar()
    global var5
    var5 = StringVar()
    global var6
    var6 = StringVar()
    global listvar
    listvar = StringVar()
    
'''Function to sort multiply choices'''    
def main(cflag, count, data1, d1Flag, data2=None, d2Flag=None, data3=None, d3Flag=None):
    df = pd.DataFrame(pd.read_csv('files/Master_Data_File.csv', sep=',', encoding='utf-8'))
    if cflag == 'City':
        # If statements to handle the case where the user does not use all fields to rank data
        if count == 1:
            # Create sorted grouping of column based on users interests
            group1 = df.sort_values(by=data1, ascending=d1Flag)
            agggroup = df[data1].rank(ascending=not d1Flag)
            ret = [group1, agggroup]
        elif count == 2:
            # Create sorted grouping of columns based on users interests
            group1 = df.sort_values(by=data1, ascending=d1Flag)
            group2 = df.sort_values(by=data2, ascending=d2Flag)

            # Compute the rank of the values in that column, I negate the flag since I want everything weighted the same
            rank1 = df[data1].rank(ascending=not d1Flag)
            rank2 = df[data2].rank(ascending=not d2Flag)

            agggroup = pd.DataFrame(data=[df['City'], rank1 + rank2], index=['City', 'Rank']).T.sort_values(by='Rank', ascending=False)
            ret = [group1, group2, agggroup]
        else:
            # Create sorted grouping of columns based on users interests
            group1 = df.sort_values(by=data1, ascending=d1Flag)
            group2 = df.sort_values(by=data2, ascending=d2Flag)
            group3 = df.sort_values(by=data3, ascending=d3Flag)

            # Compute the rank of the values in that column, I negate the flag since I want everything weighted the same
            rank1 = df[data1].rank(ascending=not d1Flag)
            rank2 = df[data2].rank(ascending=not d2Flag)
            rank3 = df[data3].rank(ascending=not d3Flag)

            agggroup = pd.DataFrame(data=[df['City'], rank1 + rank2 + rank3], index=['City', 'Rank']).T.sort_values(by='Rank', ascending=False)
            ret = [group1, group2, group3, agggroup]
    else:  # County
        # Some of our columns need to be summed and not averaged, making a list of them here
        sumList = ['Population', 'White Alone', 'Hispanic', 'Two or more races', 'Native Hawaiian', 'Black alone',
                   'Asian alone', 'American Indian alone', 'Other race alone']

        if count == 1:
            # Some of data is being assessed as Object type, even though it is clearly an int, put in this failsafe
            df[data1] = df[data1].astype('float64')
            group = df.groupby('County')
            # Set of if statements to assess if the input data should be summed or averaged
            if data1 in sumList:
                group1 = group[data1].sum().sort_values(ascending=d1Flag)
            else:
                group1 = group[data1].mean().sort_values(ascending=d1Flag)
            agggroup = group1.rank(ascending=not d1Flag)
            ret = [group1, agggroup]
        elif count == 2:
            # Some of data is being assessed as Object type, even though it is clearly an int, put in this failsafe
            df[data1] = df[data1].astype('float64')
            df[data2] = df[data2].astype('float64')
            group = df.groupby('County')

            # Set of if statements to assess if the input data should be summed or averaged
            if data1 in sumList:
                group1 = group[data1].sum().sort_values(ascending=d1Flag)
            else:
                group1 = group[data1].mean().sort_values(ascending=d1Flag)
            if data2 in sumList:
                group2 = group[data2].sum().sort_values(ascending=d2Flag)
            else:
                group2 = group[data2].mean().sort_values(ascending=d2Flag)

            # Compute the rank of the values in that column, I negate the flag since I want everything weighted the same
            rank1 = group1.rank(ascending=not d1Flag)
            rank2 = group2.rank(ascending=not d2Flag)

            agggroup = pd.DataFrame(data=[rank1 + rank2], index=['Rank']).T.sort_values(by='Rank', ascending=False)
            ret = [group1, group2, agggroup]
        else:
            # Some of data is being assessed as Object type, even though it is clearly an int, put in this failsafe
            df[data1] = df[data1].astype('float64')
            df[data2] = df[data2].astype('float64')
            df[data3] = df[data3].astype('float64')
            group = df.groupby('County')

            # Set of if statements to assess if the input data should be summed or averaged
            if data1 in sumList:
                group1 = group[data1].sum().sort_values(ascending=d1Flag)
            else:
                group1 = group[data1].mean().sort_values(ascending=d1Flag)
            if data2 in sumList:
                group2 = group[data2].sum().sort_values(ascending=d2Flag)
            else:
                group2 = group[data2].mean().sort_values(ascending=d2Flag)
            if data3 in sumList:
                group3 = group[data3].sum().sort_values(ascending=d3Flag)
            else:
                group3 = group[data3].mean().sort_values(ascending=d3Flag)

            # Compute the rank of the values in that column, I negate the flag since I want everything weighted the same
            rank1 = group1.rank(ascending=not d1Flag)
            rank2 = group2.rank(ascending=not d2Flag)
            rank3 = group3.rank(ascending=not d3Flag)

            agggroup = pd.DataFrame(data=[rank1 + rank2 + rank3], index=['Rank']).T.sort_values(by='Rank', ascending=False)
            ret = [group1, group2, group3, agggroup]

    print(agggroup)
    return ret

'''Function to open the school_GUI'''
def print_school():
    print('GUI_support.print_school')
    os.system("python school.py")
    
    
    sys.stdout.flush()

'''Get Information for county or city that user input'''
def print_selection1():
    county_name=entry.get()
    county_format=county_name+'-county'
    print(county_format.lower())
    for i in range(30):
        w.Listbox1.insert(0,"")
    df=pd.read_csv("files/ethnicity.csv")
    npdf = np.array(df)#np.ndarray()
    list=npdf.tolist()#list
    row=0
    if var4.get()=='0':
        for i in range(len(list)):
            if list[i][1].lower()==county_name.lower():
                w.Listbox1.insert(0,("City Name: "+list[i][1]+"  County Name: "+list[i][10]))
                w.Listbox1.insert(1,("Population: "+str(list[i][2])+"  Age: "+str(list[i][3])+"  Average Income: "+str(list[i][4])))
                w.Listbox1.insert(2,("Percent of Men in City: "+str(list[i][5])+"%  Per Capita Income: "+str(list[i][7])+"  Median House Value: "+str(list[i][8])))
                w.Listbox1.insert(3,("Zip Code: "+str(list[i][14])+"  Latitude: "+str(list[i][15])+"  Longitude: "+str(list[i][16])))
                w.Listbox1.insert(4,("Higher Degree: "+str(list[i][11])+"  H.S Diploma: "+str(list[i][12])+"  No H.S Diploma: "+str(list[i][13])))
    if var4.get()=='1':
        for i in range(len(list)):
            if list[i][10].lower()==county_name.lower() or list[i][10].lower()==county_format.lower():
                w.Listbox1.insert(row,("City Name: "+list[i][1]))
                row=row+1
    sys.stdout.flush()

'''Get the sort result and print it on listbox'''
def print_selection2():
    print('GUI_support.print_selection2')
    data1 = list1.get()
    data2 = list2.get()
    data3 = list3.get()
    cflag=""
    if var4.get()=='0':
        cflag="City"
    if var4.get()=='1':
        cflag='County'
    if(data1==""):
        data1='Population'
    count=1;
    if(data2!=""):
        count+=1
    if(data3!=""):
        count+=1
    print(count)
    if var1.get()=='1':
        d1Flag=True
    else:
        d1Flag=False
    if var2.get()=='1':
        d2Flag=True
    else:
        d2Flag=False
    if var2.get()=='1':
        d3Flag=True
    else:
        d3Flag=False
    result=main('County',count,data1,d1Flag,data2,d2Flag,data3,d3Flag)
#    npdf = np.array(result['County'])#np.ndarray()
#    nparr=result[0]['County']
#    result=nparr.tolist()#list
    for i in range(30):
        w.Listbox1.insert(0,"")
    if(count==1 and cflag=='County'):
        row=0
        w.Listbox1.insert(row,("The Top Five "+cflag+" For "+data1))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[0].ix[[i]].index.values[0]))
            row=row+1
        w.Listbox1.insert(row,"")
        row=row+1
        w.Listbox1.insert(row,("The Top Five "+cflag+" Recommend "))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[1].ix[[i]].index.values[0]))
            row=row+1
    if(count==2 and cflag == 'County'):
        row=0
        w.Listbox1.insert(row,("The Top Five "+cflag+" For "+data1))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[0].ix[[i]].index.values[0]))
            row=row+1
        w.Listbox1.insert(row,"")
        row=row+1
        w.Listbox1.insert(row,("The Top Five "+cflag+" For "+data2))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[1].ix[[i]].index.values[0]))
            row=row+1
        w.Listbox1.insert(row,"")
        row=row+1
        w.Listbox1.insert(row,("The Top Five "+cflag+" Recommend"))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[2].ix[[i]].index.values[0]))
            row=row+1
    if(count==3 and cflag =='County'):
        row=0
        w.Listbox1.insert(row,("The Top Five "+cflag+" For "+data1))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[0].ix[[i]].index.values[0]))
            row=row+1
        w.Listbox1.insert(row,"")
        row=row+1
        w.Listbox1.insert(row,("The Top Five "+cflag+" For "+data2))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[1].ix[[i]].index.values[0]))
            row=row+1
        w.Listbox1.insert(row,"")
        row=row+1
        w.Listbox1.insert(row,("The Top Five "+cflag+" For "+data3))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[2].ix[[i]].index.values[0]))
            row=row+1
        w.Listbox1.insert(row,"")
        row=row+1
        w.Listbox1.insert(row,("The Top Five "+cflag+" Recommend"))
        row+=1
        for i in range(5):
            w.Listbox1.insert(row,(cflag+" Name: "+result[3].ix[[i]].index.values[0]))
            row=row+1
    if(cflag=='City'):
        w.Listbox1.insert(0,("Please Choose County Level"))
#    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import GUI
    GUI.vp_start_gui()


