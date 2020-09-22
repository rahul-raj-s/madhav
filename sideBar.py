from tkinter import *

class Sidebar(Frame):
    def __init__(self, master=None):
        print(master)
        super().__init__(master=master,bg='red',height=800,width=400)
        self.header = Label(self,text='Explorer')
        self.header.pack(side='top')
        self.files =['hello.py','check.py','myfile.py']
        headers = []
        for i in self.files:
            headers.append(Label(self,text=i))
        for i in headers:
            i.pack()