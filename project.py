"""
Filename: Shoe quiz
Author: shelley
Date: 14.08.23
Description: This is a quiz for the user to figure out what shoe would
suit their lifestyle and style
Version 2:
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is just window setup
root = tk.Tk()
root.geometry("300x400")
root.title("Find your perfect shoe")


        
class Window():
    """
    This class will be used to set up my window
    """


    def __init__(self, window):
        my_frame = tk.Frame(window)
        my_frame.pack()
        self.welcome = tk.Label(window, text = "Welcome to this quiz. Press START to continue")
        self.welcome.pack()
        self.butt = tk.Button(window, text = "START", command=lambda: [self.go(window), self.butt.destroy(),self.welcome.destroy()])
        self.butt.pack(
)
    def go(self,window):
        self.q_a = {"q1":["a1","a2","a3","A4"],
               "q2":["A1","a2","a3","a4"],
               "q3":["a1","A2","a3","a4"],
               "q4":["a1","a2","A3","a4"],}
        self.question_number = 0
        # this gets the question
        q = list(self.q_a.keys())
        print(q[self.question_number])
        self.lb = tk.Label(window, text = q[self.question_number])
        self.lb.pack()


        # this gets the list of the list of answers
        boop = list(self.q_a.values())
        # this gets a list of just the answers for specified q
        needed_boop = boop[self.question_number]
             
        bt_1 = tk.Button(window, text = needed_boop[0])
        bt_1.pack()
        btn_2 = tk.Button(window, text = needed_boop[1])
        btn_2.pack()
        btn_3 = tk.Button(window, text = needed_boop[2])
        btn_3.pack()
        btn_4 = tk.Button(window, text = needed_boop[3])
        btn_4.pack()

        bck_button = tk.Button(window, text = "<")
        bck_button.pack()
        nxt_button = tk.Button(window, text = ">")
        nxt_button.pack()

        numb_lbl = self.question_number + 1
        numb_lbl = tk.Label(window, text = f"{numb_lbl}/{len(q)}")
        numb_lbl.pack()

powr_ranger = Window(root)

root.mainloop()
