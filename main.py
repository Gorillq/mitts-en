import pyttsx3
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

root = Tk()
root.geometry("100x100")
root.title("TTS")
root.resizable(False, False)

def speech():
    engine = pyttsx3.init('sapi5')
    text = simpledialog.askstring("input", "TEXT:", parent=root)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    textn = ''.join(text.splitlines())
    engine.say(textn.replace("\n", " "))
    engine.runAndWait()

mainframe = ttk.Frame(root, padding="6 6 18 18")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
B1 = ttk.Button(mainframe, command=speech, width=10, text='Decode')
B1.grid(column=1, row=1, sticky=N)

root.mainloop()