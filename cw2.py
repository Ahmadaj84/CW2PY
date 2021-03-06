#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Nov 28, 2018 10:26:32 AM GMT  platform: Windows NT

import sys
import Control as con
from tkinter import messagebox
import matplotlib.pyplot as plt


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import cw2_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    cw2_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    cw2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def task2aHandler(self):   #docIDTxt userEntr
        controler = con.control(self.fileTxt.get())#sample_400k_lines.json
        if controler.startTask2A(self.docIDTxt.get()) !=False:
              if len(controler.countriesResult)> 0:
               draw(list(controler.countriesResult.keys()),list(controler.countriesResult.values()))

              else:
                 messagebox.showinfo("CW2 Message",'No match Document ID in the file' )
        else:
            messagebox.showinfo("CW2 Message",'problem with file path' )
    def task2bHandler(self):
        controler = con.control(self.fileTxt.get())
        if controler.startTask2B(self.docIDTxt.get()) !=False:
              if len(controler.continit)> 0:
               draw(list(controler.continit.keys()),list(controler.continit.values()))
              else:
                  messagebox.showinfo("CW2 Message",'No match Document ID in the file' )
        else:
            messagebox.showinfo("CW2 Message",'problem with file path' )
    def task3aHandler(self):
        controler = con.control(self.fileTxt.get())
        if controler.startTask3a(self.docIDTxt.get()) != False:
              if len(controler.broser)> 0:
               draw(list(controler.broser.keys()),list(controler.broser.values()))
              else:
                   messagebox.showinfo("CW2 Message",'No match Document ID in the file' )
        else:
            messagebox.showinfo("CW2 Message",'problem with file path' )
    def task3bHandler(self):
        controler = con.control(self.fileTxt.get())
        if controler.startTask3b(self.docIDTxt.get()) != False:
             if len(controler.broserMainName)> 0:
              draw(list(controler.broserMainName.keys()),list(controler.broserMainName.values()))
             else:
                   messagebox.showinfo("CW2 Message",'No match Document ID in the file' )
        else:
            messagebox.showinfo("CW2 Message",'problem with file path' )

    def task4Handler(self):
        controler = con.control(self.fileTxt.get())
        if controler.startTask4(self.docIDTxt.get()) != False:
               if len(controler.ReadersOfdox)> 0:
                 txt = ''
                 for k,v in controler.ReadersOfdox.items():
                   txt += 'Dox Number: '+k[-4:]+': '+str(len(v))+'\n'
                   txt +='---------------------------------\n'
                   txt +='Readers :\n'
                   for d in v:
                     txt +=d[-4:]+'\n'

                 messagebox.showinfo("CW2 Message",txt )
               else:
                  messagebox.showinfo("CW2 Message",'No match Document ID in the file' )
        else:
            messagebox.showinfo("CW2 Message",'problem with file path' )
    def task5Handler(self):
        controler = con.control(self.fileTxt.get())
        if controler.startTask5(self.docIDTxt.get(),self.userEntr.get()) != False:
              messagebox.showinfo("CW2 Message",'a file has been generated')


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.title("CW2 for Industrial Programming by Ahmed")
        top.configure(background="#d2d5d8")
        top.configure(highlightcolor="#646464")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.117, rely=0.089, height=41, width=84)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#616ee2")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''File name''')
        self.Label1.configure(width=84)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.1, rely=0.211, height=31, width=104)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#616ee2")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Document uuid''')
        self.Label2.configure(width=104)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.117, rely=0.3, height=21, width=84)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#616ee2")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''User ID''')
        self.Label3.configure(width=84)

        self.fileTxt = tk.Entry(top)
        self.fileTxt.place(relx=0.3, rely=0.111,height=30, relwidth=0.55)
        self.fileTxt.configure(background="white")
        self.fileTxt.configure(disabledforeground="#616ee2")
        self.fileTxt.configure(font=font10)
        self.fileTxt.configure(foreground="#000000")
        self.fileTxt.configure(insertbackground="white")
        self.fileTxt.configure(selectbackground="#0078d7")
        self.fileTxt.configure(selectforeground="#ffffffffffff")
        self.fileTxt.configure(width=234)

        self.docIDTxt = tk.Entry(top)
        self.docIDTxt.place(relx=0.3, rely=0.222,height=30, relwidth=0.55)
        self.docIDTxt.configure(background="white")
        self.docIDTxt.configure(disabledforeground="#616ee2")
        self.docIDTxt.configure(font=font10)
        self.docIDTxt.configure(foreground="#000000")
        self.docIDTxt.configure(insertbackground="white")
        self.docIDTxt.configure(width=234)

        self.userEntr = tk.Entry(top)
        self.userEntr.place(relx=0.3, rely=0.311,height=30, relwidth=0.55)
        self.userEntr.configure(background="white")
        self.userEntr.configure(disabledforeground="#616ee2")
        self.userEntr.configure(font=font10)
        self.userEntr.configure(foreground="#000000")
        self.userEntr.configure(insertbackground="white")
        self.userEntr.configure(width=234)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.133, rely=0.556, relheight=0.362
                , relwidth=0.733)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#2d3ed8")
        self.Message1.configure(highlightcolor="white")
        self.Message1.configure(width=440)

        self.task2a = tk.Button(top)
        self.task2a.place(relx=0.083, rely=0.422, height=24, width=63)
        self.task2a.configure(activebackground="#ececec")
        self.task2a.configure(activeforeground="#000000")
        self.task2a.configure(background="#d9d9d9")
        self.task2a.configure(disabledforeground="#616ee2")
        self.task2a.configure(foreground="#000000")
        self.task2a.configure(highlightbackground="#d9d9d9")
        self.task2a.configure(highlightcolor="white")
        self.task2a.configure(pady="0")
        self.task2a.configure(text='''Task 2 a''')
        self.task2a.configure(width=63)
        self.task2a.configure(command=self.task2aHandler)

        self.task2b = tk.Button(top)
        self.task2b.place(relx=0.233, rely=0.422, height=24, width=64)
        self.task2b.configure(activebackground="#ececec")
        self.task2b.configure(activeforeground="#000000")
        self.task2b.configure(background="#d9d9d9")
        self.task2b.configure(disabledforeground="#616ee2")
        self.task2b.configure(foreground="#000000")
        self.task2b.configure(highlightbackground="#d9d9d9")
        self.task2b.configure(highlightcolor="white")
        self.task2b.configure(pady="0")
        self.task2b.configure(text='''Task 2 b''')
        self.task2b.configure(width=64)
        self.task2b.configure(command=self.task2bHandler)

        self.task3 = tk.Button(top)
        self.task3.place(relx=0.4, rely=0.422, height=24, width=64)
        self.task3.configure(activebackground="#ececec")
        self.task3.configure(activeforeground="#000000")
        self.task3.configure(background="#d9d9d9")
        self.task3.configure(disabledforeground="#616ee2")
        self.task3.configure(foreground="#000000")
        self.task3.configure(highlightbackground="#d9d9d9")
        self.task3.configure(highlightcolor="white")
        self.task3.configure(pady="0")
        self.task3.configure(text='''Task 3''')
        self.task3.configure(width=64)
        self.task3.configure(command=self.task3aHandler)

        self.task3b = tk.Button(top)
        self.task3b.place(relx=0.55, rely=0.422, height=24, width=64)
        self.task3b.configure(activebackground="#ececec")
        self.task3b.configure(activeforeground="#000000")
        self.task3b.configure(background="#d9d9d9")
        self.task3b.configure(disabledforeground="#616ee2")
        self.task3b.configure(foreground="#000000")
        self.task3b.configure(highlightbackground="#d9d9d9")
        self.task3b.configure(highlightcolor="white")
        self.task3b.configure(pady="0")
        self.task3b.configure(text='''Task 3B''')
        self.task3b.configure(width=64)
        self.task3b.configure(command=self.task3bHandler)


        self.task4 = tk.Button(top)
        self.task4.place(relx=0.7, rely=0.422, height=24, width=64)
        self.task4.configure(activebackground="#ececec")
        self.task4.configure(activeforeground="#000000")
        self.task4.configure(background="#d9d9d9")
        self.task4.configure(disabledforeground="#616ee2")
        self.task4.configure(foreground="#000000")
        self.task4.configure(highlightbackground="#d9d9d9")
        self.task4.configure(highlightcolor="white")
        self.task4.configure(pady="0")
        self.task4.configure(text='''Task 4''')
        self.task4.configure(width=64)
        self.task4.configure(command=self.task4Handler)

        self.task5 = tk.Button(top)
        self.task5.place(relx=0.85, rely=0.422, height=24, width=64)
        self.task5.configure(activebackground="#ececec")
        self.task5.configure(activeforeground="#000000")
        self.task5.configure(background="#d9d9d9")
        self.task5.configure(disabledforeground="#616ee2")
        self.task5.configure(foreground="#000000")
        self.task5.configure(highlightbackground="#d9d9d9")
        self.task5.configure(highlightcolor="white")
        self.task5.configure(pady="0")
        self.task5.configure(text='''Task 5''')
        self.task5.configure(width=64)
        self.task5.configure(command=self.task5Handler)
def draw(lst1,lst2):
    fig, ax = plt.subplots()
    ax.barh(lst1,lst2)
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) == 9:
      c = con.control(sys.argv[8])#sample_400k_lines.json
      if sys.argv[6] == '2a':
          if c.startTask2A(sys.argv[4]) !=False:
              if len(c.countriesResult)> 0:
               draw(list(c.countriesResult.keys()),list(c.countriesResult.values()))

              else:
                  print ('No match Document ID in the file')

      elif sys.argv[6] == '2b':
          if c.startTask2B(sys.argv[4]) !=False:
              if len(c.continit)> 0:
               draw(list(c.continit.keys()),list(c.continit.values()))
              else:
                  print ('No match Document ID in the file')
      elif sys.argv[6] == '3a':
          if c.startTask3a(sys.argv[4]) != False:
              if len(c.broser)> 0:
               draw(list(c.broser.keys()),list(c.broser.values()))
              else:
                  print ('No match Document ID in the file')
      elif sys.argv[6] == '3b':
         if c.startTask3b(sys.argv[4]) != False:
             if len(c.broserMainName)> 0:
              draw(list(c.broserMainName.keys()),list(c.broserMainName.values()))
             else:
                  print ('No match Document ID in the file')
      elif sys.argv[6] == '4d':
          if c.startTask4(sys.argv[4]) != False:
               if len(c.ReadersOfdox)> 0:
                 for k,v in c.ReadersOfdox.items():
                   print('Dox Number: '+k[-4:]+': '+str(len(v)))
                   print('---------------------------------')
                   print('Readers :')
                   for d in v:
                     print(d[-4:])
               else:
                  print ('No match Document ID in the file')
      elif sys.argv[6] == '5':
          if c.startTask5(sys.argv[4],sys.argv[2]) != False:
              print('a file has been generated')
      else:
          print('Wrong Task code entered')
    else:
     print ('test GUI')
     vp_start_gui()





