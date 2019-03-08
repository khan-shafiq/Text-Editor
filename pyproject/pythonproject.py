"""Developed by AIS
   Basic text Editor using file handling
"""
#first plz install pyautogui "pip install pyautogui in cmd"
import pyautogui
from tkinter import *
from tkinter import filedialog

class MenuBar:

    def __init__(self,root):

        self.menubar=Menu(root)   #Creating menubar
        root.config(menu=self.menubar)

        self.filemenu=Menu(root,tearoff=0)
        self.t=Text(root,width=1100,height=700,wrap=WORD)
        self.t.pack()

        self.filemenu.add_command(label="New", command=self.new)
        self.filemenu.add_command(label="Open...", command=self.open)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_command(label="Save As...", command=self.saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        
        self.editmenu=Menu(root,tearoff=0)


        self.editmenu.add_command(label="Undo", command=self.undo)
        self.editmenu.add_command(label="Redo", command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)

        self.formatmenu=Menu(root,tearoff=0)
        self.formatmenu.add_command(label="Word Wrap", command=self.donothing)
        self.formatmenu.add_command(label="Font...", command=self.donothing)
        self.menubar.add_cascade(label="Format",menu=self.formatmenu)

        self.viewmenu=Menu(root,tearoff=0)
        self.viewmenu.add_command(label="Status Bar", command=self.donothing)
        self.menubar.add_cascade(label="View",menu=self.viewmenu)

        self.helpmenu=Menu(root,tearoff=0)
        self.helpmenu.add_command(label="View Help", command=self.help)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About AIS Notepad", command=self.about)
        self.menubar.add_cascade(label="Help",menu=self.helpmenu)
          
    def donothing(self):
        pass

    def open(self):
        self.filename=filedialog.askopenfilename(parent=root,title='OPEN',filetypes=(("Text Documents","*.txt"),("All Files","*.*")))

        try:
          if self.filename!=None:
            f=open(self.filename,'r')
            content=f.read()
            self.t.delete(1.0,END)
            self.t.insert(1.0,content)
            f.close()

        except:
           pass

    def saveas(self):
        self.filename=filedialog.asksaveasfilename(parent=root,defaultextension=".txt")
        try:
          if self.filename!=None:
            f=open(self.filename,"w")
            content=str(self.t.get(1.0,END))
            f.write(content)
            f.close()

        except:
            pass
        
    def save(self):
        self.filename=filedialog.asksaveasfilename(parent=root,defaultextension=".txt")
        try:
          if self.filename!=None:
            f=open(self.filename,"w")
            content=str(self.t.get(1.0,END))
            f.write(content)
            f.close()

        except:
           pass
        
    def new(self):
        self.t.delete(1.0,END)
    def help(self):
        j="""For any help plz contact any of the given below no:
1)ABDULLAH    -:   7021599658
2)IZHAR       -:   7684558245
3)SHAFIQULLAH -:   9137264694"""

        self.t.delete(1.0,END)
        self.t.insert(1.0,j)
        

    def about(self):
        a="""This is a free software (version 2.20) made by ABDULLAH, IZHAR, and SHAFIQULLAH (AIS).
The purpose of making this project is to deal with mini project of Open Source Tech Lab guided by Prof. Asadullah Shaikh Sir. 
The AIS is the name of the software, it stand for its owners."""
        self.t.delete(1.0,END)
        self.t.insert(1.0,a)

    def copy(self):
        pyautogui.hotkey('ctrl','c')

    def paste(self):
        pyautogui.hotkey('ctrl','v')

    def cut(self):
        pyautogui.hotkey('ctrl','x')

    def undo(self):
        c=str(self.t.get(1.0,END))
        pyautogui.hotkey('ctrl','z')

    def redo(self):
        pyautogui.hotkey('ctrl','y')
     

root=Tk()                            #create window
root.title("AIS Notepad")            #gives title to window
obj=MenuBar(root)
root.geometry("1200x720")            #gives size to window
root.wm_iconbitmap('notepad.ico')   #set icon of window
root.mainloop()                      #display window
