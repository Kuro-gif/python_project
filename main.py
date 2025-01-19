import tkinter as tk
from tkinter import ttk
#Dictionary of 20 Ijaw words with their meanings
ijaw_dictionary = {
    "Amabe": "Good morning",
    "Torubara": "Love",
    "Belemu": "Thank you",
    "Keme" : "Water",
    "Ogbo" : "House",
    "Ayibai": "Friend",
    "Ebi": "Family",
    "Buofegha": "Happy",
    "Igoni": "Sky",
    "Tamuno": "God",
    "Tor": "Life",
    "Obo": "Hand",
    "Akpo": "World",
    "Ayiba": 'Kindness',
    "Kuro": "Road",
    "Kabo": "Hello",
    "Bobo": "Child",
    "Furo": "Light",
    "Oku": "Fire",
    "Seigbei": "Peace",
}
# Create the main window
root = tk.Tk()
root . title("Ijaw Dictionary")
root . geometry("400x300")
# Create a function to display the meaning
def show_meaning():
    word = word_entry . get() . capitalize()
    meaning = ijaw_dictionary . get(word, "Word not found in dictionary . ")
    result_label . config(text = f"Meaning: {meaning}")
# Create UI elements
title_label = tk . Label(root,  text="Ijaw Dictionary", font=("Arial", 16))
title_label . pack(pady = 10)
word_label = tk.Label(root, text="Enter an Ijaw Word : ")
word_label . pack()
word_entry = ttk.Entry(root,  width=30)
word_entry.pack(pady=5)
search_button = ttk . Button(root,  text = "search", command = show_meaning)
search_button . pack(pady = 10)
result_label = tk.Label(root,  text = "Meaning:", font = ("Arial", 12))
result_label . pack(pady = 10)
#Run the main loop
root . mainloop()
