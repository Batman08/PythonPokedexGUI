import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3 
from io import BytesIO
from StringHelper import *

ICON_LOCATION = 'WindowIcon/favicon-32x32.png'
WINDOW = tk.Tk()
WINDOW.geometry("600x500")
WINDOW.title("WeSellAnyCode Python Pokedex")
WINDOW.iconphoto(False, tk.PhotoImage(file=ICON_LOCATION))


def create_label(label, label_text, text_size):
    label = tk.Label(WINDOW, text=label_text)
    label.config(font=("Arial", text_size))
    label.pack(padx=10, pady=10)

def create_button():
    BUTTON_LOAD = tk.Button(WINDOW, text="Load Pokemon", command=load_pokemon)
    BUTTON_LOAD.config(font=("Arial", 20))
    BUTTON_LOAD.pack(padx=10, pady=10)

create_label(TITLE_LABEL, WINDOW_TITLE_NAME, 32)

POKEMONE_IMAGE = tk.Label(WINDOW, text=None)
POKEMONE_IMAGE.config(font=("Arial", 32))
POKEMONE_IMAGE.pack(padx=10, pady=10)

POKEMONE_INFORMATION = tk.Label(WINDOW, text=None)
POKEMONE_INFORMATION.config(font=("Arial", 32))
POKEMONE_INFORMATION.pack(padx=10, pady=10)

POKEMONE_TYPES = tk.Label(WINDOW, text=None)
POKEMONE_TYPES.config(font=("Arial", 32))
POKEMONE_TYPES.pack(padx=10, pady=10)

create_label(LABEL_ID_NAME, None, 20)

TEXT_ID_NAME = tk.Text(WINDOW, height=1)
TEXT_ID_NAME.config(font=("Arial", 20))
TEXT_ID_NAME.pack(padx=10, pady=10)

def load_pokemon():
    pokemon = pypokedex.get(name=TEXT_ID_NAME.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    POKEMONE_IMAGE.config(image=img)
    POKEMONE_IMAGE.image = img

    POKEMONE_INFORMATION.config(text=f"{pokemon.dex} - {pokemon.name}")
    POKEMONE_TYPES.config(text=f"{pokemon.types}")


create_button()
WINDOW.mainloop()