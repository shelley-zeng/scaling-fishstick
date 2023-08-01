"""
Filename: Shoe quiz
Author: shelley
Date: 25.07.23
Description: This is a quiz for the user to figure out what shoe would
suit their lifestyle and style
Version 1:
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
# this crrates sizing of the window and title
window.geometry("300x400")
window.title("Find your perfect shoe")

# column and row configuration
window.columnconfigure(0, weight = 5, minsize = 40)
window.columnconfigure(1, weight = 5, minsize = 40)
window.rowconfigure([0,1,2,3], weight = 2, minsize = 20)
Font_tuple = ("Tahoma", 20, "bold")

# question set up
frame=tk.Frame(window, width=200, height=200, bg="#ff0")
quiz_label = tk.Label(frame, text = "Question", font=Font_tuple)

# answer buttons
answer_1 = tk.Button(text = "Answer 1", font = Font_tuple, height = 3)
answer_2 = tk.Button(text = "Answer 2", font = Font_tuple, height = 3)
answer_3 = tk.Button(text = "Answer 3", font = Font_tuple, height = 3)
answer_4 = tk.Button(text = "Answer 4", font = Font_tuple, height = 3)

back_button = tk.Button (text = "<", font = Font_tuple, height = 1)
next_button = tk.Button (text = ">", font = Font_tuple, height = 1)


# grid layout
quiz_label.grid(row = 0, column = 0, columnspan =2, padx=50, pady=50)
answer_1.grid(row = 1, column = 0)
answer_2.grid(row = 1, column = 1)
answer_3.grid(row = 2, column = 0)
answer_4.grid(row = 2, column = 1)
back_button.grid(row=3, column=0)
next_button.grid(row=3, column =1)
frame.grid(row = 0, column = 0, columnspan =2, padx=20, pady=5)

# makes the window not resizable
window.resizable(False, False)
window.mainloop()
