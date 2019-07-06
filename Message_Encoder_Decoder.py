# Importing required packages
import tkinter
from tkinter import *
import string

#defining the tkinter window class
class Root:
    __window = Tk()
    def __init__(self):
        self.__window.title("Message Encryption-Decryption")
        self.__window.resizable(0,0)
        self.__ws = self.__window.winfo_screenwidth() # width of the screen
        self.__hs = self.__window.winfo_screenheight() # height of the screen
        self.__w = 1050
        self.__h = 500
        self.__x = (self.__ws/2) - (self.__w/2)
        self.__y = (self.__hs/2) - (self.__h/2)  
        self.__window.geometry('%dx%d+%d+%d' % (self.__w, self.__h, self.__x, self.__y))
        self.__label_head_1 = Label(self.__window,text = "Ceaser Ciphers")
        self.__label_head_1.config(font = ("Courier",44))
        self.__label_head_1.pack(side = TOP)
        self.__label_head_2 = Label(self.__window,text = "Secret Message Generator")
        self.__label_head_2.config(font = ("Courier",18))
        self.__label_head_2.pack(side = TOP)
        self.__f1 = Frame(self.__window, width = self.__w, height = self.__h) 
        self.__f1.pack(side = LEFT) 
        
    # adding label to the window
        self.__label_1 = Label(self.__f1, text="Message    :",font = ('arial', 12, 'bold'))
        self.__label_1.grid(row=0,column=0)
        
    # adding entry column to get the message
        self.__entry_1 = Entry(self.__f1,width = 40,bd = 10, insertwidth = 6, 
                  bg = "powder blue", justify = 'right', font = ('arial', 10, 'bold'))
        self.__entry_1.grid(row=0,column=1)
        
        self.__label_2 = Label(self.__f1, text="Key    :",font = ('arial', 12, 'bold'))
        self.__label_2.grid(row=1,column=0)
        
    # adding entry column to get the key
        self.__entry_2 = Entry(self.__f1,width = 40,bd = 10, insertwidth = 6, 
                  bg = "powder blue", justify = 'right', font = ('arial', 10, 'bold'))
        self.__entry_2.grid(row=1,column=1)
        
        self.__label_3 = Label(self.__f1, text="Mode  :  \n(e for encryption d for decryption)",font = ('arial', 12, 'bold'))
        self.__label_3.grid(row=2,column=0)
        
    # adding entry column to get the mode (encryption/decryption)
        self.__entry_3 = Entry(self.__f1,width = 40,bd = 10, insertwidth = 6, 
                  bg = "powder blue", justify = 'right', font = ('arial', 10, 'bold'))
        self.__entry_3.grid(row=2,column=1)
        
        self.__label_4 = Label(self.__f1, text="Result    :",font = ('arial', 12, 'bold'))
        self.__label_4.grid(row=2,column=2)
        
    # adding entry column to display the result
        self.__entry_4 = Entry(self.__f1,width = 40,bd = 10, insertwidth = 4, 
                  bg = "powder blue", justify = 'right', font = ('arial', 10, 'bold'))
        self.__entry_4.grid(row=2,column=3)
        
        self.__label_5 = Label(self.__f1, text="~"*10,font = ('arial', 30, 'bold'))
        self.__label_5.grid(row=4,column=1)
        
        self.__button_1 = Button(self.__f1,text = "Reset", padx = 12, pady = 6, bd = 10, fg = "black", 
                        font = ('arial', 14, 'bold'), width = 8, 
                        bg = "powder blue",command = self.__reset)
        self.__button_1.grid(row=7,column=1)
        self.__button_1 = Button(self.__f1,text = "Generate", padx = 12, pady = 6, bd = 10, fg = "black", 
                        font = ('arial', 14, 'bold'), width = 8, 
                        bg = "green",command = self.__generate)
        self.__button_1.grid(row=7,column=2)
        self.__button_2 = Button(self.__f1,text = "Exit", padx = 12, pady = 6, bd = 10, fg = "black", 
                        font = ('arial', 14, 'bold'), width = 8, 
                        bg = "red",command = self.__close)
        self.__button_2.grid(row=7,column=3)

# forfully close the window
    def __close(self):
        self.__window.destroy()
        
# to reset each entry box
    def __reset(self):
        self.__entry_1.delete(0,END)
        self.__entry_2.delete(0,END)
        self.__entry_3.delete(0,END)
        self.__entry_4.delete(0,END)

# to call the encoding/decoding function with provided mode value        
    def __generate(self):
        self.__text = self.__entry_1.get()
        self.__key = int(self.__entry_2.get())
        if self.__entry_3.get()=="e" or self.__entry_3.get()=="E":
            self.__show = self.__encrypt(self.__text,self.__key)
        elif self.__entry_3.get()=="d" or self.__entry_3.get()=="D":
            self.__show = self.__decrypt(self.__text,self.__key)
        else:showerror("Error","Invalid Mode.")
        self.__entry_4.delete(0,END)
        self.__entry_4.insert(0,self.__show)
            
#-------------------------------------------------------------------------------
# Encryption function
#-------------------------------------------------------------------------------

    def __encrypt(self,text,key):
        
        encrypted = list(range(len(text)))
        alphabet = string.ascii_lowercase
        
        f_half = alphabet[:key]
        s_half = alphabet[key:]
        
        shifted_alphabet = s_half+f_half
        
        for i,latter in enumerate(text.lower()):
            if latter in alphabet:
                org_index = alphabet.index(latter)
                new_latter = shifted_alphabet[org_index]
                encrypted[i] = new_latter
            else:
                encrypted[i] = latter
        return ''.join(encrypted)

#-------------------------------------------------------------------------------
# Decryption function
#-------------------------------------------------------------------------------
    
    def __decrypt(self,text,key):
        
        decrypted = list(range(len(text)))
        alphabet = string.ascii_lowercase
        
        f_half = alphabet[:key]
        s_half = alphabet[key:]
        
        shifted_alphabet = s_half+f_half
        
        for i,latter in enumerate(text.lower()):
            if latter in alphabet:
                index = shifted_alphabet.index(latter)
                org_latter = alphabet[index]
                decrypted[i] = org_latter
            else:
                decrypted[i] = latter
        return ''.join(decrypted)
        
    def run(self):
        self.__window.mainloop()
        
# root object is created
test = Root()
test.run()
