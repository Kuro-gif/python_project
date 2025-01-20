import tkinter as tk
from tkinter import ttk
#dictionary of 20 yoruba words with their meanings
yoruba_dictionary = {
    "Owo" : "Money",
    "Ese" : "Leg",
    "Eja" : "Fish",
    "Ila" : "Okra",
    "Oruko" : "Name",
    "Bata" : "Shoe",
    "Omo" : "Child",
    "Aja" : "Cat",
    "Eye" : "Bird",
    "Ewa" : "Beans",
    "Ola" : "Wealth",
    "Wa" : "Come",
    "Lo" : "Go",
    "Ororo" : "Oil",
    "Isu" : "Yam",
    "Omi" : "Water",
    "Oju" : "Face",
    "Ina": "Light",
    "Otutu" : "Cold",
    "Ife" : "Love",
}


# Create the main window
root = tk.Tk()
root . title("Yoruba Dictionary")
root . geometry("400x350")


#create function to display the meaning
def show_meaning():
    word = word_entry . get() . capitalize()
    meaning = yoruba_dictionary . get(word, "Translation not found in dictionary . ")
    result_label . config(text = f"Translation: {meaning}")


#create UI elements
title_label = tk . Label(root, text="Yoruba Dictionary", font=("Time New Roman", 18))
title_label . pack(pady = 10)
word_label = tk.Label(root, text="Search for a Yoruba Word : ")
word_label . pack ()
word_entry = ttk.Entry(root, width=30)
word_entry.pack(pady=5)
search_button = ttk.Button(root, text="Translate", command = show_meaning)
search_button . pack(pady=10)
result_label = tk.Label(root, text= "Translation", font= ("Time New Roman",13))
result_label . pack(pady = 10)

#run the main loop
root . mainloop()


















