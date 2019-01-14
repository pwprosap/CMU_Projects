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

import GUI_support
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    GUI_support.set_Tk_var()
    top = New_Toplevel (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    GUI_support.set_Tk_var()
    top = New_Toplevel (w)
    GUI_support.init(w, top, *args, **kwargs)
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

        top.geometry("843x893+554+35")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.308, rely=0.045,height=51, relwidth=0.467)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=GUI_support.entry)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.071, rely=0.056, height=36, width=175)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Input Name of County:''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.842, rely=0.045, height=53, width=83)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=GUI_support.print_selection1)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.747, rely=0.134, height=53, width=163)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=GUI_support.print_school)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Show School Info''')
        
        self.Label1_1 = Label(top)
        self.Label1_1.place(relx=0.037, rely=0.156, height=36, width=175)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Choose Level:''')
        
        self.Radiobuttion1 = Radiobutton(top)
        self.Radiobuttion1.place(relx=0.2, rely=0.150, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion1.configure(activebackground="#d9d9d9")
        self.Radiobuttion1.configure(activeforeground="#000000")
        self.Radiobuttion1.configure(background="#d9d9d9")
        self.Radiobuttion1.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion1.configure(foreground="#000000")
        self.Radiobuttion1.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion1.configure(highlightcolor="black")
        self.Radiobuttion1.configure(justify=LEFT)
        self.Radiobuttion1.configure(text='''City''')
        self.Radiobuttion1.configure(variable=GUI_support.var4,value=0)
        
        self.Radiobuttion2 = Radiobutton(top)
        self.Radiobuttion2.place(relx=0.3, rely=0.150, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion2.configure(activebackground="#d9d9d9")
        self.Radiobuttion2.configure(activeforeground="#000000")
        self.Radiobuttion2.configure(background="#d9d9d9")
        self.Radiobuttion2.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion2.configure(foreground="#000000")
        self.Radiobuttion2.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion2.configure(highlightcolor="black")
        self.Radiobuttion2.configure(justify=LEFT)
        self.Radiobuttion2.configure(text='''County''')
        self.Radiobuttion2.configure(variable=GUI_support.var4,value=1)
#.pack(side='left')
        self.Label5 = Label(top,text='First Selection： ')
        self.Label5.place(relx=0.09, rely=0.28, height=30, width=100)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Combobox1 = ttk.Combobox(top,textvariable=GUI_support.list1,values=['Population','Age','Average Income','Percent of Men in City','Percent of Women in City','Per Capita Income','Median House Value','Higher Degree','H.S Diploma','No H.S Diploma','White alone','Hispanic','Two or more races','Native Hawaiian','Black alone','Asian alone','American Indian alone','Other race alone','Doctorate M'])
        self.Combobox1.place(relx=0.09, rely=0.32, height=30, width=150)
        
        
        self.Label4 = Label(top,text='   Second Selection： ')
        self.Label4.place(relx=0.34, rely=0.28, height=30, width=100)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Combobox2 = ttk.Combobox(top,textvariable=GUI_support.list2,values=['Population','Age','Average Income','Percent of Men in City','Percent of Women in City','Per Capita Income','Median House Value','Higher Degree','H.S Diploma','No H.S Diploma','White alone','Hispanic','Two or more races','Native Hawaiian','Black alone','Asian alone','American Indian alone','Other race alone','Doctorate M'])
        self.Combobox2.place(relx=0.34, rely=0.32, height=30, width=150)
        
    
        
        self.Label6 = Label(top,text='Third Selection： ')
        self.Label6.place(relx=0.59, rely=0.28, height=30, width=100)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Combobox3 = ttk.Combobox(top,textvariable=GUI_support.list3,values=['Population','Age','Average Income','Percent of Men in City','Percent of Women in City','Per Capita Income','Median House Value','Higher Degree','H.S Diploma','No H.S Diploma','White alone','Hispanic','Two or more races','Native Hawaiian','Black alone','Asian alone','American Indian alone','Other race alone','Doctorate M'])
        self.Combobox3.place(relx=0.59, rely=0.32, height=30, width=150)
#        self.Combobox.configure(activebackground="#f9f9f9")
#        self.Combobox.configure(activeforeground="black")
#        self.Combobox.configure(background="#d9d9d9")
#        self.Combobox.configure(disabledforeground="#a3a3a3")
#        self.Combobox.configure(foreground="#000000")
#        self.Combobox.configure(highlightbackground="#d9d9d9")
#        self.Combobox.configure(highlightcolor="black")
#        self.Combobox.configure(text='''Label''')
        self.Radiobuttion1_1 = Radiobutton(top)
        self.Radiobuttion1_1.place(relx=0.07, rely=0.36, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion1_1.configure(activebackground="#d9d9d9")
        self.Radiobuttion1_1.configure(activeforeground="#000000")
        self.Radiobuttion1_1.configure(background="#d9d9d9")
        self.Radiobuttion1_1.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion1_1.configure(foreground="#000000")
        self.Radiobuttion1_1.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion1_1.configure(highlightcolor="black")
        self.Radiobuttion1_1.configure(justify=LEFT)
        self.Radiobuttion1_1.configure(text='''High''')
        self.Radiobuttion1_1.configure(variable=GUI_support.var1,value=1)
        
        self.Radiobuttion1_2 = Radiobutton(top)
        self.Radiobuttion1_2.place(relx=0.17, rely=0.36, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion1_2.configure(activebackground="#d9d9d9")
        self.Radiobuttion1_2.configure(activeforeground="#000000")
        self.Radiobuttion1_2.configure(background="#d9d9d9")
        self.Radiobuttion1_2.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion1_2.configure(foreground="#000000")
        self.Radiobuttion1_2.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion1_2.configure(highlightcolor="black")
        self.Radiobuttion1_2.configure(justify=LEFT)
        self.Radiobuttion1_2.configure(text='''Low''')
        self.Radiobuttion1_2.configure(variable=GUI_support.var1,value=0)
        
        self.Radiobuttion2_1 = Radiobutton(top)
        self.Radiobuttion2_1.place(relx=0.32, rely=0.36, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion2_1.configure(activebackground="#d9d9d9")
        self.Radiobuttion2_1.configure(activeforeground="#000000")
        self.Radiobuttion2_1.configure(background="#d9d9d9")
        self.Radiobuttion2_1.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion2_1.configure(foreground="#000000")
        self.Radiobuttion2_1.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion2_1.configure(highlightcolor="black")
        self.Radiobuttion2_1.configure(justify=LEFT)
        self.Radiobuttion2_1.configure(text='''High''')
        self.Radiobuttion2_1.configure(variable=GUI_support.var2,value=1)
        
        self.Radiobuttion2_2 = Radiobutton(top)
        self.Radiobuttion2_2.place(relx=0.42, rely=0.36, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion2_2.configure(activebackground="#d9d9d9")
        self.Radiobuttion2_2.configure(activeforeground="#000000")
        self.Radiobuttion2_2.configure(background="#d9d9d9")
        self.Radiobuttion2_2.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion2_2.configure(foreground="#000000")
        self.Radiobuttion2_2.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion2_2.configure(highlightcolor="black")
        self.Radiobuttion2_2.configure(justify=LEFT)
        self.Radiobuttion2_2.configure(text='''Low''')
        self.Radiobuttion2_2.configure(variable=GUI_support.var2,value=2)
        
        self.Radiobuttion3_1 = Radiobutton(top)
        self.Radiobuttion3_1.place(relx=0.57, rely=0.36, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion3_1.configure(activebackground="#d9d9d9")
        self.Radiobuttion3_1.configure(activeforeground="#000000")
        self.Radiobuttion3_1.configure(background="#d9d9d9")
        self.Radiobuttion3_1.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion3_1.configure(foreground="#000000")
        self.Radiobuttion3_1.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion3_1.configure(highlightcolor="black")
        self.Radiobuttion3_1.configure(justify=LEFT)
        self.Radiobuttion3_1.configure(text='''High''')
        self.Radiobuttion3_1.configure(variable=GUI_support.var3,value=1)
        
        self.Radiobuttion3_2 = Radiobutton(top)
        self.Radiobuttion3_2.place(relx=0.67, rely=0.36, relheight=0.057
                , relwidth=0.1)
        self.Radiobuttion3_2.configure(activebackground="#d9d9d9")
        self.Radiobuttion3_2.configure(activeforeground="#000000")
        self.Radiobuttion3_2.configure(background="#d9d9d9")
        self.Radiobuttion3_2.configure(disabledforeground="#a3a3a3")
        self.Radiobuttion3_2.configure(foreground="#000000")
        self.Radiobuttion3_2.configure(highlightbackground="#d9d9d9")
        self.Radiobuttion3_2.configure(highlightcolor="black")
        self.Radiobuttion3_2.configure(justify=LEFT)
        self.Radiobuttion3_2.configure(text='''Low''')
        self.Radiobuttion3_2.configure(variable=GUI_support.var3,value=0)
        
        self.Label3 = Label(top)
        self.Label3.place(relx=0.036, rely=0.209, height=66, width=255)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Please Select Three Metrics:''')
        
        self.Button3 = Button(top)
        self.Button3.place(relx=0.819, rely=0.407, height=53, width=103)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=GUI_support.print_selection2)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Submit''')

        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.036, rely=0.515, relheight=0.455
                , relwidth=0.93)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=784)
        self.Listbox1.configure(listvariable=GUI_support.listvar)
'''
        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.356, rely=0.246, relheight=0.057
                , relwidth=0.218)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''''')
        self.Checkbutton2.configure(variable=GUI_support.var2)

        self.Checkbutton2_1 = Checkbutton(top)
        self.Checkbutton2_1.place(relx=0.664, rely=0.235, relheight=0.057
                , relwidth=0.218)
        self.Checkbutton2_1.configure(activebackground="#d9d9d9")
        self.Checkbutton2_1.configure(activeforeground="#000000")
        self.Checkbutton2_1.configure(background="#d9d9d9")
        self.Checkbutton2_1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2_1.configure(foreground="#000000")
        self.Checkbutton2_1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2_1.configure(highlightcolor="black")
        self.Checkbutton2_1.configure(justify=LEFT)
        self.Checkbutton2_1.configure(text='''''')
        self.Checkbutton2_1.configure(variable=GUI_support.var3)

        self.Checkbutton2_2 = Checkbutton(top)
        self.Checkbutton2_2.place(relx=0.071, rely=0.258, relheight=0.035
                , relwidth=0.153)
        self.Checkbutton2_2.configure(activebackground="#d9d9d9")
        self.Checkbutton2_2.configure(activeforeground="#000000")
        self.Checkbutton2_2.configure(background="#d9d9d9")
        self.Checkbutton2_2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2_2.configure(foreground="#000000")
        self.Checkbutton2_2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2_2.configure(highlightcolor="black")
        self.Checkbutton2_2.configure(justify=LEFT)
        self.Checkbutton2_2.configure(text='''''')
        self.Checkbutton2_2.configure(variable=GUI_support.var1)

        self.Checkbutton2_3 = Checkbutton(top)
        self.Checkbutton2_3.place(relx=0.024, rely=0.325, relheight=0.057
                , relwidth=0.325)
        self.Checkbutton2_3.configure(activebackground="#d9d9d9")
        self.Checkbutton2_3.configure(activeforeground="#000000")
        self.Checkbutton2_3.configure(background="#d9d9d9")
        self.Checkbutton2_3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2_3.configure(foreground="#000000")
        self.Checkbutton2_3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2_3.configure(highlightcolor="black")
        self.Checkbutton2_3.configure(justify=LEFT)
        self.Checkbutton2_3.configure(text='''''')
        self.Checkbutton2_3.configure(variable=GUI_support.var4)

        self.Checkbutton2_4 = Checkbutton(top)
        self.Checkbutton2_4.place(relx=0.391, rely=0.325, relheight=0.057
                , relwidth=0.242)
        self.Checkbutton2_4.configure(activebackground="#d9d9d9")
        self.Checkbutton2_4.configure(activeforeground="#000000")
        self.Checkbutton2_4.configure(background="#d9d9d9")
        self.Checkbutton2_4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2_4.configure(foreground="#000000")
        self.Checkbutton2_4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2_4.configure(highlightcolor="black")
        self.Checkbutton2_4.configure(justify=LEFT)
        self.Checkbutton2_4.configure(text='''''')
        self.Checkbutton2_4.configure(variable=GUI_support.var5)

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.641, rely=0.314, relheight=0.08
                , relwidth=0.301)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''''')
        self.Checkbutton1.configure(variable=GUI_support.var6)'''
        
        
        

#        self.Label4 = Label(top)
#        self.Label4.place(relx=0.095, rely=0.437, height=36, width=135)
#        self.Label4.configure(background="#d9d9d9")
#        self.Label4.configure(disabledforeground="#a3a3a3")
#        self.Label4.configure(foreground="#000000")
#        self.Label4.configure(text='''Label''')
#        self.Label4.configure(width=135)






if __name__ == '__main__':
    vp_start_gui()



