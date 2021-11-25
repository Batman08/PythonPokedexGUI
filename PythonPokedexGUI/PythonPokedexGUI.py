import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3 
from io import BytesIO

WINDOW_TITLE_NAME = "WeSellAnyCode Pokedex"
TITLE_LABEL =""
POKEMONE_IMAGE=""
POKEMONE_INFORMATION=""
POKEMONE_TYPES=""

LABEL_ID_NAME=""
TEXT_ID_NAME=""
BUTTON_LOAD=""

WINDOW = tk.Tk()
WINDOW.geometry("600x500")
WINDOW.title("WeSellAnyCode Python Pokedex")


def create_label(label, label_text, text_size):
    label = tk.Label(WINDOW, text=label_text)
    label.config(font=("Arial", text_size))
    label.pack(padx=10, pady=10)

def create_text_field():
    TEXT_ID_NAME = tk.Text(WINDOW, height=1)
    TEXT_ID_NAME.config(font=("Arial", 20))
    TEXT_ID_NAME.pack(padx=10, pady=10)

def create_button():
    BUTTON_LOAD = tk.Label(WINDOW, text="Load Pokemon")
    BUTTON_LOAD.config(font=("Arial", 20))
    BUTTON_LOAD.pack(padx=10, pady=10)

def create_window_labels():
    create_label(TITLE_LABEL, WINDOW_TITLE_NAME, 32)
    create_label(POKEMONE_IMAGE, None, 32)
    create_label(POKEMONE_INFORMATION, None, 32)
    create_label(POKEMONE_TYPES, None, 32)
    create_label(LABEL_ID_NAME, None, 20)
    create_text_field()
    create_button()

create_window_labels()   
WINDOW.mainloop()