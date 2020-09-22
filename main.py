#!/usr/bin/env python3
import loader
from tkinter import *
# from textEditor import text_editor
from textArea import TextArea
from sideBar import Sidebar
from menu import MainMenu
root = Tk()
root.geometry('1200x600+120+120')
def nothing():
    print('nothing')
middle_frame = Frame(root)
text_area = TextArea(middle_frame)
side_bar = Sidebar(middle_frame)
side_bar.pack(side='left')
text_area.pack(side ='right')
main_menu = MainMenu(master=root,text_area=text_area)
middle_frame.pack(fill=BOTH,expand=1)
root.config(menu = main_menu)
root.mainloop()