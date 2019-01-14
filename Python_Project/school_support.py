#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

'''Please run this py file in windows operation system, it may have some small
   format problems when running in osx'''
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

'''Generate the var we may neeed'''
def set_Tk_var():
    global list1
    list1 = StringVar()
    global input
    input = StringVar()
    global list2
    list2 = StringVar()
    global list3
    list3 = StringVar()
    global list4
    list4 = StringVar()

'''print information about different cluster'''
def button1():
    print('school_support.button1')
    df=pd.read_csv("files/frame.csv")
    npdf = np.array(df)#np.ndarray()
    list=npdf.tolist()#list
    print(list[0])
    for i in range(30):
        w.Listbox1.insert(0,"")
    w.Listbox1.insert(0,("          % Advanced     % Proficient  % Basic  % Below Basic  Conduct OSS"))
    w.Listbox1.insert(1,(list[0][0]+"  "+str(list[0][1])[:6]+"         "+str(list[0][2])[:6]+"        "+str(list[0][3])[:6]+"   "+str(list[0][4])[:6]+"         "+str(list[0][5])[:6]))
    w.Listbox1.insert(2,(list[1][0]+"  "+str(list[1][1])[:6]+"         "+str(list[1][2])[:6]+"        "+str(list[1][3])[:6]+"   "+str(list[1][4])[:6]+"         "+str(list[1][5])[:6]))
    w.Listbox1.insert(3,(list[2][0]+"  "+str(list[2][1])[:6]+"         "+str(list[2][2])[:6]+"        "+str(list[2][3])[:6]+"   "+str(list[2][4])[:6]+"         "+str(list[2][5])[:6]))
    w.Listbox1.insert(4,(list[3][0]+"  "+str(list[3][1])[:6]+"         "+str(list[3][2])[:6]+"        "+str(list[3][3])[:6]+"   "+str(list[3][4])[:6]+"         "+str(list[3][5])[:6]))
    w.Listbox1.insert(5,(list[4][0]+"  "+str(list[4][1])[:6]+"         "+str(list[4][2])[:6]+"        "+str(list[4][3])[:6]+"   "+str(list[4][4])[:6]+"         "+str(list[4][5])[:6]))
    sys.stdout.flush()


'''Show Information on listbox3'''
def combolist():
    print('school_support.combolist')
    for i in range(30):
        w.Listbox3.insert(0,"")
    cluster = list3.get()
    if cluster == "":
        cluster = "Cluster1"
    if cluster =='Cluster1':
        df=pd.read_csv("files/Cluster1.csv")
    if cluster =='Cluster2':
        df=pd.read_csv("files/Cluster2.csv")
    if cluster =='Cluster3':
        df=pd.read_csv("files/Cluster3.csv")
    if cluster =='Cluster4':
        df=pd.read_csv("files/Cluster4.csv")
    if cluster =='Cluster5':
        df=pd.read_csv("files/Cluster5.csv")
    npdf = np.array(df)#np.ndarray()
    list=npdf.tolist()#list
    for i in range(len(list)):
        w.Listbox3.insert(0,("School Name: "+list[i][4]))
        w.Listbox3.insert(1,("County Name: "+list[i][3]))
        w.Listbox3.insert(2,"")

'''Get information from the cluster and county that user chooses'''
def button2():
    for i in range(30):
        w.Listbox2.insert(0,"")
    
    if list3.get()=='Cluster1':
        df=pd.read_csv("files/Cluster1.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
            
    if list3.get()=='Cluster2':
        df=pd.read_csv("files/Cluster2.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    if list3.get()=='Cluster3':
        df=pd.read_csv("files/Cluster3.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    if list3.get()=='Cluster4':
        df=pd.read_csv("files/Cluster4.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    if list3.get()=='Cluster5':
        df=pd.read_csv("files/Cluster5.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    sys.stdout.flush()

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
    import school
    school.vp_start_gui()


