#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:08:39 2020

@author: vikrant
"""
from cns_model_use import model
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('URL Phishing Detection')
window.geometry('500x500')

lbl1 = tk.Label(window, text = 'Enter URL for checking:')
lbl1.place(x = 12, y = 30)

enter_url = tk.Entry(window, width = 30)
enter_url.place(x = 200, y = 30)
enter_url.focus()

def clicked():
    url = enter_url.get()
    ans = model(url)
    result(ans)

def blank():
    enter_url.delete(0 ,END)
    
def result(ans):
   if ans == 1:
       txt = 'The URL is legitimate!'
       tk.messagebox.showinfo("Legitimate URL!", txt)
   else:
       txt = 'The URL is phishing!'
       tk.messagebox.showinfo("Phishing URL!", txt)
        
submit = tk.Button(window, text = 'Check URL',  command = clicked)
submit.place(x = 100, y = 60 )

reset = tk.Button(window, text = "Reset", command = blank)
reset.place(x = 200, y = 60)

window.mainloop()