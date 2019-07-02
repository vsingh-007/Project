#importing all required libraries

import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    __window = Tk()
    __menubar = Menu(__window)
    __main = Menu(__menubar,tearoff = 0)
    __edit = Menu(__menubar,tearoff = 0)
    __help_ = Menu(__menubar,tearoff = 0)
    __text_area = Text(__window)
    __scrollbar = Scrollbar(__text_area)
    __file = None
    def __init__(self):
        
        #window size manupulation
        
        self.__window.title("Untitled-Notepad")
        self.__ws = self.__window.winfo_screenwidth() # width of the screen
        self.__hs = self.__window.winfo_screenheight() # height of the screen
        self.__w = 800
        self.__h = 500
        self.__x = (self.__ws/2) - (self.__w/2)
        self.__y = (self.__hs/2) - (self.__h/2)  
        self.__window.geometry('%dx%d+%d+%d' % (self.__w, self.__h, self.__x, self.__y))
        self.__window.grid_rowconfigure(0,weight = 1)
        self.__window.grid_columnconfigure(0,weight = 1)
        self.__text_area.grid(sticky = N + E + W + S) 
        
        
    # Menu bar
    # File menu
        self.__main.add_command(label = "New",command = self.__new)
        self.__main.add_command(label = "Open..",command = self.__open)
        self.__main.add_command(label = "Save",command = self.__save)
        self.__main.add_command(label = "Save as..",command = self.__saveas)
        self.__main.add_separator()
        self.__main.add_command(label = "Exit",command = self.__exit)
        self.__menubar.add_cascade(label="File", menu=self.__main)  
        
    # Tool menu
        self.__edit.add_command(label = "Cut",command = self.__cut)
        self.__edit.add_command(label = "Copy",command = self.__copy)
        self.__edit.add_command(label = "Paste",command = self.__paste)
        self.__edit.add_command(label = "Delete",command = self.__delete)
        self.__menubar.add_cascade(label="Edit", menu=self.__edit)  
        
    #help menu
        self.__help_.add_command(label = "Help !",command = self.__help)
        self.__help_.add_separator()
        self.__help_.add_command(label = "About Notepad",command = self.__about)
        self.__menubar.add_cascade(label = "Help",menu = self.__help_)
        
    #window text area auto resizable
        self.__window.config(menu = self.__menubar)
        self.__scrollbar.pack(side = RIGHT,fill = Y)
        self.__scrollbar.config(command=self.__text_area.yview)
        self.__text_area.config(yscrollcommand = self.__scrollbar.set)
    
    def __new(self):
        self.__window.title("Untitled-Notepad")
        self.__file = None
        self.__text_area.delete(0.0,END)
    def __open(self):
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
            # Try to open the file 
            # set the window title 
            self.__window.title(os.path.basename(self.__file) + " - Notepad") 
            self.__text_area.delete(1.0,END)
            file = open(self.__file,"r") 
            self.__text_area.insert(1.0,file.read()) 
            file.close() 
    
    def __save(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                        defaultextension=".txt",
                                                        filetypes=[("All Files","*.*"),
                                                        ("Text Documents","*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file,"w")
                file.write(self.__text_area.get(1.0,END)) 
                file.close() 
                self.__window.title(os.path.basename(self.__file) + " - Notepad")
                
        else:
            file = open(self.__file,"w")
            file.write(self.__text_area.get(1.0,END)) 
            file.close() 

    def __saveas(self):
        self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                        defaultextension=".txt",
                                                        filetypes=[("All Files","*.*"),
                                                        ("Text Documents","*.txt")])
        file = open(self.__file,"w")
        file.write(self.__text_area.get(1.0,END)) 
        file.close() 
        
    def __exit(self):
        self.__window.destroy()
        
    def __cut(self):
        self.__text_area.event_generate("<<Cut>>")
        
    def __copy(self):
        self.__text_area.event_generate("<<Copy>>")
        
    def __paste(self):
        self.__text_area.event_generate("<<Paste>>")
        
    def __delete(self):
        self.__text_area.delete(0.0,END)
        
    def __help(self):
        showerror("Error","File Not Found")
    
    def __about(self):
        showinfo("About","Self designed and created \nBy Vipin Singh") 
        
    def run(self):
        self.__window.mainloop()
        
        
notepad = Notepad()
notepad.run()
