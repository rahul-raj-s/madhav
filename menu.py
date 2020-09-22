from tkinter import *
from constants import *
from tkinter import filedialog,messagebox

class MainMenu(Menu):
    def  __init__(self,master,text_area=''):
        self.text_area = text_area
        super().__init__(master,bg='#ffffff',fg='blue')
        self.master = master
        self.addFileMenu()
        self.addEditMenu()
        self.addSettingsMenu()
        

    def addFileMenu(self):
        self.file_menu = Menu(self,tearoff=False,bg='#ffffff')
        self.file_menu.add_command(label='New file',command= self.text_area.new_file)
        self.file_menu.add_command(label="Open file",command=self.openFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save as ",command=self.text_area.save_as_file)
        self.file_menu.add_command(label="Save",command=self.text_area.save)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command= self.master.quit)
        self.add_cascade(label="File",menu = self.file_menu)

    def addEditMenu(self):
        self.edit_menu = Menu(self,tearoff=False,bg='#ffffff')
        self.edit_menu.add_command(label="Copy",command=self.nothing)
        self.edit_menu.add_command(label="Cut",command=self.nothing)
        self.edit_menu.add_command(label="Paste",command=self.nothing)
        self.edit_menu.add_command(label="Undo",command=self.nothing)
        self.edit_menu.add_command(label="Redo",command=self.nothing)
        self.add_cascade(label="Edit",menu = self.edit_menu)
    
    def addSettingsMenu(self):
        self.settings_menu = Menu(self,tearoff=False,bg='#ffffff')
        self.settings_menu.add_command(label="Font-size",command=self.text_area.change_font_size)

        #theme menu
        self.theme_menu = Menu(self.settings_menu,tearoff=False,bg='#ffffff')
        self.theme_menu.add_command(label='dark',command=self.text_area.change_theame)
        self.theme_menu.add_command(label='light',command=lambda :self.text_area.change_theame('light'))
        self.settings_menu.add_cascade(label="Theame",menu=self.theme_menu)

        self.add_cascade(label="Settings",menu = self.settings_menu)

    def nothing(self):
        print('hello')

    def openFile(self,event=''):
        if(self.text_area.lastSaved != self.text_area.get(1.0,END)):
            answer = messagebox.askyesno('exit',"Do you want to save current file")
            if(answer):
                self.save()
        open_return = filedialog.askopenfile(initialdir='/home/in-lt-31',title='Select file',filetypes=FILE_TYPES)
        if(open_return):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
            self.text_area.current_open_file = open_return.name
            self.lastSaved=self.text_area.get(1.0,END)
            # self.frame.configure(text=open_return.name)
            open_return.close()