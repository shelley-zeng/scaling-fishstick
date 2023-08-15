"""
Filename: Shoe quiz
Author: shelley
Date: 16.08.23
Description: This is a quiz for the user to figure out what shoe would
suit their lifestyle and style
Version 3:
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
               "q2":["A1","LALA2","CHERRY","RAWR"],
               "q3":["WOOGA1","CHRISTMAS2","TWILERBEE","a4"],
               "q4":["SOAP","SHAMPOO","CONFITIONER","TOOTHPASTE"],}
        self.question_number = 0
        # this gets the question
        self.q = list(self.q_a.keys())
        print(self.q[self.question_number])
        self.lb = tk.Label(window, text = self.q[self.question_number])
        self.lb.pack()


        # this gets the list of the list of answers
        self.boop = list(self.q_a.values())
        # this gets a list of just the answers for specified q
        self.needed_boop = self.boop[self.question_number]
             
        self.btn_1 = tk.Button(window, text = self.needed_boop[0])
        self.btn_1.pack()
        self.btn_2 = tk.Button(window, text = self.needed_boop[1])
        self.btn_2.pack()
        self.btn_3 = tk.Button(window, text = self.needed_boop[2])
        self.btn_3.pack()
        self.btn_4 = tk.Button(window, text = self.needed_boop[3])
        self.btn_4.pack()

        bck_button = tk.Button(window, text = "<")
        bck_button.pack()
        nxt_button = tk.Button(window, text = ">", command = lambda: [self.next_button(window), self.lb.destroy()])
        nxt_button.pack()

        self.numb_lbl = self.question_number + 1
        self.numb_lbl = tk.Label(window, text = f"{self.numb_lbl}/{len(self.q)}")
        self.numb_lbl.pack()

    def next_button(self, window):
        # this lets the user go from question 1 to question 2
        self.question_number += 1
        self.needed_boop = self.boop[self.question_number]
        # destroy prev. q buttons
        self.btn_1.destroy()
        self.btn_2.destroy()
        self.btn_3.destroy()
        self.btn_4.destroy()
        self.numb_lbl.destroy()
        
        self.btn_1 = tk.Button(window, text= self.needed_boop[0])
        self.btn_1.pack()
        self.btn_2 = tk.Button(window, text = self.needed_boop[1])
        self.btn_2.pack()
        self.btn_3 = tk.Button(window, text = self.needed_boop[2])
        self.btn_3.pack()
        self.btn_4 = tk.Button(window, text = self.needed_boop[3])
        self.btn_4.pack()

        print(self.q)
        print(self.question_number)
        self.new_lbl = tk.Label(window, text = self.q[self.question_number])
        self.new_lbl.pack()
        self.numb_lbl = self.question_number + 1
        self.numb_lbl = tk.Label(window, text = f"{self.numb_lbl}/{len(self.q)}")
        self.numb_lbl.pack()


powr_ranger = Window(root)

root.mainloop()
