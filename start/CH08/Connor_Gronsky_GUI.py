#!/usr/bin/env python3
# Script that dispalys GUI and says name and age as well as positive affirmation.
# By Connor Gronsky on 8/19/2025

import tkinter as tk
from tkinter import messagebox

def greet_user():
    name = name_entry.get()
    age = age_entry.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter your name.")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid age.")
        return

    future_age = age + 2
    greeting = f"Hello {name}!\nToday is going to be a great day!\nIn 2 years, you will be {future_age} years old."
    messagebox.showinfo("Greeting", greeting)

# Create the main window
root = tk.Tk()
root.title("Hello World GUI")

# Create and place widgets
tk.Label(root, text="Enter your name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Enter your age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Button(root, text="Greet Me!", command=greet_user).pack(pady=10)

# Run the application
root.mainloop()
