from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()

    if filepath != ():
        file = open(filepath, 'r')
        file.close()

window = Tk()

button = Button(text='open', command=open_file)
button.pack()

window.mainloop()
