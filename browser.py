import tkinter as tk
from tkinter import *
import webbrowser
root = tk.Tk()

root.title("Universal search Bar")

label1 = Label(root, text = "Query ")
label1.grid(row=0, column=0)
entry1= Entry(root, width=50)
entry1.grid(row=0, column=1)

def callback():
    webbrowser.open('https://google.com/search?q='+entry1.get())

def get(event):
    webbrowser.open('https://google.com/search?q='+entry1.get())

button = Button(root, text="search", command=callback)
button.grid(row=0, column=2)

entry1.bind('<Return>', get)

root.wm_attributes('-topmost', 1)

root.mainloop()