import tkinter as tk
from tkinter import messagebox

dictionaries={
    "french":{
        "thank you":"merci",
        "please":"s'il vous plait",
        "yes":"oui",
        "no":"non",
        "water":"eau",},
    "yoruba":{
        "thank you":"e seun",
        "please":"e joo",
        "yes":'beeni',
        "no":"rara",
        "water":"omi",
        "child":"omo",
        "table":"tebili",
        "fire":"ina",
        "friend":"ore",
        "moon":"osupa",
    },

    "hausa":{
        "thank you":"na gode",
        "no":"a'a",
        "book":"littafi",
        "sit":"zuana",
        "left":"hagu",
        "right":"dama",
        "three":"uku",
        "sleep":"baci",
        "leg":"kafa",
        "house":"gida",
    },
}

#search word function
def search_word():
    selected_dictionary=dictionary_var.get()
    word = entry.get().strip().lower()
    #get user input,trim spaces,and convert to lowercase
    meaning = dictionaries.get(selected_dictionary,{}).get(word)

    if meaning:
        result_label.config(text=f"Meaning { meaning}"),
    else:
        result_label.config(text="")
        messagebox.showinfo(message="There is no such in this dictionary")



root = tk.Tk()
root.title("Multi-Language Dictionary")
welcome_label = tk.Label(root, text="Welcome to our Dictionary",padx=200,pady=100,bg="blue",fg="white",font="Arial 16")
welcome_label.pack()
root.geometry("600x600")

title_label= tk.Label(root, text="Please select a Language")
title_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(text="Search word", command=search_word)
search_button.pack()

result_label = tk.Label(root)
result_label.pack()

dictionary_var=tk.StringVar(value="French")
dictionary_menu = tk.OptionMenu(root, dictionary_var,*dictionaries.keys())
dictionary_menu.pack()

result_label=tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)


root.mainloop()
