from tkinter import *
import tkinter as tk
from support.Trie import Trie

window=tk.Tk()
trie = Trie()

icon_pi = tk.PhotoImage(file = 'img//icons//placeholder.png')
window.iconphoto(False, icon_pi)

key = tk.StringVar(window)
    
def place_label(label_txt, relief_type):
    sgstn_label = tk.Label(window, text=label_txt, borderwidth=2, width =50, relief=relief_type)
    sgstn_label.place(x=25,y=100)

def read_input():
    word = key.get()
    print(word)
    if(trie.search(word)):
        place_label('The word seems to be of correct spelling.', 'flat')
    else:
        qstn_label = tk.Label(window, text='Did you mean?')
        qstn_label.place(x=25,y=75)
        place_label(trie.suggestions_to_String(), 'sunken')
    
txt_entry = tk.Entry(window, textvariable=key, bg='white', fg='black', width=45, bd=5)
txt_entry.place(x=25,y=25)
        
check_btn = tk.Button(window, text='Check', fg='black', command=read_input)
check_btn.place(x=340,y=25)
window.title('Lavangam - A spell checker')
window.geometry("400x300+10+10")
window.mainloop()