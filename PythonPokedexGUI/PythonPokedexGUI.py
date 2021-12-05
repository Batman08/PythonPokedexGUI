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

pokemon_image = tk.Label(WINDOW, text=None)
pokemon_image.config(font=("Arial", 32))
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(WINDOW, text=None)
pokemon_information.config(font=("Arial", 32))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(WINDOW, text=None)
pokemon_types.config(font=("Arial", 32))
pokemon_types.pack(padx=10, pady=10)

create_label(LABEL_ID_NAME, None, 20)

text_id_name = tk.Text(WINDOW, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")


create_button()
WINDOW.mainloop()