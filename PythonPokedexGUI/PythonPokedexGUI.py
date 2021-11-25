import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3 
from io import BytesIO

WINDOW =tk.Tk()
WINDOW.geometry("600x500")
WINDOW.title("WeSellAnyCode Python Pokedex")

TITLE_LABEL = tk.Label(WINDOW, text="WeSellAnyCode Pokedex")
TITLE_LABEL.config(font=("Arial", 32))
TITLE_LABEL.pack(padx=10, pady=10)

WINDOW.mainloop()