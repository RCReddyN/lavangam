from tkinter import *
import tkinter as tk
from support.Trie import Trie

window=tk.Tk()
trie = Trie()

icon_pi = tk.PhotoImage(file = 'img//icons//placeholder.png')
window.iconphoto(False, icon_pi)

key = tk.StringVar(window)
def read_input():
    sug = ''
    sgstn_label = tk.Label(window, text=sug, borderwidth=2, width =50, relief='sunken')
    sgstn_label.place(x=25,y=100)
    print(key.get())
    if(trie.search(key.get())):
        sug=''
        sgstn_label = tk.Label(window, text=sug, borderwidth=2, width =50, relief='sunken')
        sgstn_label.place(x=25,y=100)
    else:
        qstn_label = tk.Label(window, text='Did you mean?')
        qstn_label.place(x=25,y=75)
        sug = trie.suggestions_to_String()
        sgstn_label = tk.Label(window, text=sug, borderwidth=2, width =50, relief='sunken')
        sgstn_label.place(x=25,y=100)
    
txt_entry = tk.Entry(window, textvariable=key, bg='white', fg='black', width=45, bd=5)
txt_entry.place(x=25,y=25)
        
check_btn = tk.Button(window, text='Check', fg='black', command=read_input)
check_btn.place(x=340,y=25)
        
window.title('Lavangam - A spell checker')
window.geometry("400x300+10+10")
window.mainloop()
