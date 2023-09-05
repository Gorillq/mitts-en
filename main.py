import sys
import pyttsx3
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

root = Tk()
root.geometry("220x75")
root.title("TTS")
root.resizable(False, False)

def terminate():
    sys.exit()

def speech():
    engine = pyttsx3.init('sapi5')
    text = simpledialog.askstring("TTS-PL", "TEXT:", parent=root)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    textn = ''.join(text.splitlines())
    engine.say(textn.replace("\n", " "))
    engine.runAndWait()

def speech_en():
    engine = pyttsx3.init('sapi5')
    text = simpledialog.askstring("TTS-EN", "TEXT:", parent=root)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    textn = ''.join(text.splitlines())
    engine.say(textn.replace("\n", " "))
    engine.runAndWait()

mainframe = ttk.Frame(root, padding="6 6 18 18")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
B1 = ttk.Button(mainframe, command=speech, width=10, text='Polski')
B1.grid(column=1, row=1, sticky=W)
B2 = ttk.Button(mainframe, command=speech_en, width=10, text='English')
B2.grid(column=3, row=1, sticky=E)
B3 = ttk.Button(mainframe, command=terminate, width=10, text='Close')
B3.grid(column=2, row=2, sticky=S)


root.mainloop()