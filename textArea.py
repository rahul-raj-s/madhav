from tkinter import *
from tkinter.font import Font
from tkinter import filedialog,messagebox
from changeSettings import changeSettings
from constants import *

class TextArea(Text):
    def __init__(self, master=None): 
        self.theme = THEME_SETUP[THEME]
        self.font = Font(size=FONT_SIZE)
        super().__init__(master,bg=self.theme['bg'],width=400,heigh=200,fg=self.theme['fg'],font=self.font,insertbackground=self.theme['cursor'])
        self.current_open_file = ''
        self.lastSaved = ''
        # self.pack(fill=BOTH,expand=1)
        self.tag_configure("method", foreground="red")
        self.tag_configure("keyword", foreground="blue")
        font = Font(font=self['font'])
        tab = font.measure('    ')
        self.config(tabs=tab)
        self.pack_propagate(False)
        self.grid_propagate(False)
    def bindTextArea(self):
        self.bind('<space>',self.maintainColor)
        self.bind('(',self.maintainColor)
        self.bind('<Return>',self.assignTabs)
        self.bind('<Control s>',self.save)

    def new_file(self,event=''):
        if(self.lastSaved != self.get(1.0,END)):
            answer = messagebox.askyesno('exit',"Do you want to save current file")
            if(answer):
                self.save()
        self.delete(1.0,END)
        self.current_open_file= None
        self.lastSaved=''
        # self.frame.configure(text='untitle')

    def save_as_file(self,event=''):
        f = filedialog.asksaveasfile(mode='w')
        if(f):
            text_to_save = self.get(1.0,END)
            f.write(text_to_save)
            self.current_open_file = f.name
            # self.frame.configure(text=f.name)
            self.isSaved = True
            f.close()
    
    def save(self,event=''):
        if(not self.current_open_file):
            self.save_as_file()
        else:
            f = open(self.current_open_file,'w+')
            currentText = self.get(1.0,END)
            f.write(currentText)
            self.lastSaved = currentText
            print(currentText==self.lastSaved)
            # self.frame.configure(text=f.name)
            # self.isSaved = True

    def maintainColor(self,event=''):
        x = self.get('insert-2c wordstart','end-2c wordend')
        type =None
        if(x in PYTHON_KEYWORDS):
            type = 'keyword'
        elif(x in PYTHON_METHODS):
            type ='method'
        if(type):
            self.tag_add(type, 'insert-2c wordstart', 'end-2c wordend')
    
    def assignTabs(self,event=''):
        x = self.get('current linestart',CURRENT)
        print(x)
        if(x[-1]==':'):
            pos = self.index(CURRENT)
            print(pos)
            self.mark_set('insert','current lineend')
            # self.insert('insert','\ndklfald')
            self.mark_set('insert',int(float(pos))+1.4)
            pos = self.index(CURRENT)
            print(pos)
    def copy(self,event=""):
        self.clipboard_clear()
        self.clipboard_append(self.selection_get())

    def cut(self,event=""):
        self.copy()
        self.delete('sel.first','sel.last')

    def paste(self,event=""):
        self.insert(INSERT,self.clipboard_get())

    def change_font_size(self):
        top = Toplevel(width=100)
        top.title("CHANGE FONT SIZE")
        s = Scale(top,from_=10,to=30,orient="horizontal")
        f = open('local_settings.json')
        data = json.load(f)
        f.close()
        s.set(data['fontSize'])
        btn = Button(top,text="SET",command=lambda : self.change_size(s.get(),top))
        s.pack()
        btn.pack()

    def change_size(self,size,top):
        font = Font(size=size)
        self.config(font=font)
        changeSettings(({'fontSize':size}))
        top.destroy()

    def change_theame(self,type='dark'):
        setup = THEME_SETUP[type]
        self.config(bg=setup['bg'],fg=setup['fg'],insertbackground=setup['cursor'])
        changeSettings({'theme':type})