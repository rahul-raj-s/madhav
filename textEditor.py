from tkinter import *
from tkinter import filedialog,messagebox
from settingMenu import *
from constants import *
import subprocess
import os

class text_editor:
    current_open_file = None
    def __init__(self,master):
        self.master = master
        self.lastSaved = ''
        self.font = Font(size=FONT_SIZE)
        self.theme = THEME_SETUP[THEME]
        self.master.title('madhavi')
        self.frame = LabelFrame(self.master,text='untitled')
        self.text_area = Text(self.frame,bg=self.theme['bg'],fg=self.theme['fg'],font=self.font,insertbackground=self.theme['cursor'])
        self.frame.pack(fill=BOTH,expand=1)
        self.text_area.pack(fill=BOTH,expand=1)
        self.bindTextArea()
        # self.main_menu = Menu(bg='#ffffff',fg='blue')
        # self.master.config(menu = self.main_menu)

        #file menu
        self.file_menu = Menu(self.main_menu,tearoff=False,bg='#ffffff')
        self.file_menu.add_command(label='New file',command= self.new_file)
        self.file_menu.add_command(label="Open file",command=self.openFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save as ",command=self.save_as_file)
        self.file_menu.add_command(label="Save",command=self.save)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command= self.master.quit)

        #edit menu 
        self.edit_menu = Menu(self.main_menu,tearoff=False,bg='#ffffff')
        self.edit_menu.add_command(label="Copy",command=self.copy)
        self.edit_menu.add_command(label="Cut",command=self.cut)
        self.edit_menu.add_command(label="Paste",command=self.paste)
        self.edit_menu.add_command(label="Undo",command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo",command=self.text_area.edit_redo)

        #setting menu
        self.settings = Settings(self.main_menu,self.master,self.text_area).getmenu()

        self.main_menu.add_cascade(label="File",menu = self.file_menu)
        self.main_menu.add_cascade(label="Edit",menu = self.edit_menu)
        self.main_menu.add_cascade(label="Settings",menu = self.settings)
        self.main_menu.add_command(label="run",command=self.run)
    def bindTextArea(self):
        self.text_area.tag_configure("method", foreground="red")
        self.text_area.tag_configure("keyword", foreground="blue")
        self.text_area.bind('<space>',self.maintainColor)
        self.text_area.bind('(',self.maintainColor)
        self.text_area.bind('<Return>',self.assignTabs)
        font = Font(font=self.text_area['font'])
        tab = font.measure('    ')
        self.text_area.config(tabs=tab)

    def openFile(self,event=''):
        if(self.lastSaved != self.text_area.get(1.0,END)):
            answer = messagebox.askyesno('exit',"Do you want to save current file")
            if(answer):
                self.save()
        open_return = filedialog.askopenfile(initialdir='/home/in-lt-31',title='Select file',filetypes=FILE_TYPES)
        if(open_return):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
            text_editor.current_open_file = open_return.name
            self.lastSaved=self.text_area.get(1.0,END)
            self.frame.configure(text=open_return.name)
            open_return.close()

    def save_as_file(self,event=''):
        f = filedialog.asksaveasfile(mode='w')
        if(f):
            text_to_save = self.text_area.get(1.0,END)
            f.write(text_to_save)
            text_editor.current_open_file = f.name
            self.frame.configure(text=f.name)
            self.isSaved = True
            f.close()

    def save(self,event=''):
        if(not text_editor.current_open_file):
            self.save_as_file()
        else:
            f = open(self.current_open_file,'w+')
            currentText = self.text_area.get(1.0,END)
            f.write(currentText)
            self.lastSaved = currentText
            print(currentText==self.lastSaved)
            self.frame.configure(text=f.name)
            self.isSaved = True

    def new_file(self,event=''):
        print('lastSaved',self.lastSaved)
        print('curent',self.text_area.get(1.0,END))
        if(self.lastSaved != self.text_area.get(1.0,END)):
            answer = messagebox.askyesno('exit',"Do you want to save current file")
            if(answer):
                self.save()
        self.text_area.delete(1.0,END)
        text_editor.current_open_file= None
        self.lastSaved=''
        self.frame.configure(text='untitle')

    def copy(self,event=""):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut(self,event=""):
        self.copy()
        self.text_area.delete('sel.first','sel.last')
    def paste(self,event=""):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())

    def run(self):
        # x = subprocess.check_output('python3 '+self.current_open_file,shell=True,)
        # print(x)
        print("under test")


    def maintainColor(self,event=''):
        x = self.text_area.get('insert-2c wordstart','end-2c wordend')
        type =None
        if(x in PYTHON_KEYWORDS):
            type = 'keyword'
        elif(x in PYTHON_METHODS):
            type ='method'
        if(type):
            self.text_area.tag_add(type, 'insert-2c wordstart', 'end-2c wordend')
    
    def assignTabs(self,event=''):
        x = self.text_area.get('current linestart',CURRENT)
        print(x)
        if(x[-1]==':'):
            pos = self.text_area.index(CURRENT)
            print(pos)
            self.text_area.mark_set('insert','current lineend')
            # self.text_area.insert('insert','\ndklfald')
            self.text_area.mark_set('insert',int(float(pos))+1.4)
            pos = self.text_area.index(CURRENT)
            print(pos)