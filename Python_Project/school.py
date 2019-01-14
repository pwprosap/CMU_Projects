#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
'''Please run this py file in windows operation system, it may have some small
   format problems when running in osx'''
'''Import the packages that we need'''
import sys

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

import school_support

import tkinter.font as tkFont
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    school_support.set_Tk_var()
    top = New_Toplevel (root)
    school_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    school_support.set_Tk_var()
    top = New_Toplevel (w)
    school_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("1069x759+503+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        ft1 = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)
        ft2 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
        self.Label1 = Label(top,font = ft1)
        self.Label1.place(relx=0.386, rely=0.013, height=46, width=300)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(borderwidth="3")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Search School''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.084, rely=0.119, height=123, width=203)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=school_support.button1)
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Run Cluster''')

        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.337, rely=0.092, relheight=0.219
                , relwidth=0.63)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=674)
        self.Listbox1.configure(listvariable=school_support.list1)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.337, rely=0.407,height=51, relwidth=0.415)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=school_support.input)

         
        self.Label2 = Label(top)
        self.Label2.place(relx=0.056, rely=0.332, height=46, width=235)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Choose Cluster''')
        self.Combobox1 = ttk.Combobox(top,textvariable=school_support.list3,values=['Cluster1','Cluster2','Cluster3','Cluster4','Cluster5'],postcommand=school_support.combolist)
        self.Combobox1.place(relx=0.34, rely=0.332, height=30, width=150)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.056, rely=0.407, height=66, width=235)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Choose County''')
        
        self.Label4 = Label(top,font=ft2)
        self.Label4.place(relx=0.136, rely=0.507, height=66, width=300)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Schools in Selected Cluster''')
        
        self.Label5 = Label(top,font=ft2)
        self.Label5.place(relx=0.606, rely=0.507, height=66, width=300)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Similar Schools Recommend''')

        self.Listbox2 = Listbox(top)
        self.Listbox2.place(relx=0.065, rely=0.593, relheight=0.39
                , relwidth=0.43)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")
        self.Listbox2.configure(highlightbackground="#d9d9d9")
        self.Listbox2.configure(highlightcolor="black")
        self.Listbox2.configure(selectbackground="#c4c4c4")
        self.Listbox2.configure(selectforeground="black")
        self.Listbox2.configure(width=934)
        self.Listbox2.configure(listvariable=school_support.list2)
        
        self.Listbox3 = Listbox(top)
        self.Listbox3.place(relx=0.525, rely=0.593, relheight=0.39
                , relwidth=0.43)
        self.Listbox3.configure(background="white")
        self.Listbox3.configure(disabledforeground="#a3a3a3")
        self.Listbox3.configure(font="TkFixedFont")
        self.Listbox3.configure(foreground="#000000")
        self.Listbox3.configure(highlightbackground="#d9d9d9")
        self.Listbox3.configure(highlightcolor="black")
        self.Listbox3.configure(selectbackground="#c4c4c4")
        self.Listbox3.configure(selectforeground="black")
        self.Listbox3.configure(width=934)
        self.Listbox3.configure(listvariable=school_support.list4)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.851, rely=0.394, height=63, width=123)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=school_support.button2)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Submit''')
        self.Button3.configure(width=123)






if __name__ == '__main__':
    vp_start_gui()



