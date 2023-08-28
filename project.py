"""
Filename: Shoe quiz
Author: shelley
Date: 24.08.23
Description: This is a quiz for the user to figure out what shoe would
suit their lifestyle and style
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

# this is just window setup
root = tk.Tk()
root.geometry("300x400")
root.title("Find your perfect shoe")
root.resizable(False,False)

        
class Window:
    """
    This class will be used to set up my window
    """


    def __init__(self, window):
        # this is the grid layout
        window.columnconfigure([0,1,2,3,4], weight = 2)
        window.rowconfigure([0,1,2,3], weight =5)
        self.welcome = tk.Label(window, text = "Welcome to this quiz. Press START to continue")

        self.butt = tk.Button(window, text = "START", command=lambda: [self.go(window), self.butt.destroy(),self.welcome.destroy()])
        self.result_list = []

        self.welcome.grid(row =0, column = 1, columnspan=4, rowspan =2) 
        self.butt.grid(row =2, column = 2, columnspan=2)

        self.q_a = {"q1":["a1","a2","a3","A4"],
                    "q2":["A1","LALA2","CHERRY","RAWR"],
                    "q3":["WOOGA1","CHRISTMAS2","TWILERBEE","a4"],
                    "q4":["SOAP","SHAMPOO","CONFITIONER","TOOTHPASTE"],}
        self.question_number = 0

        

    def go(self,window):
        # this gets the question
        self.q = list(self.q_a.keys())
        #print(self.q[self.question_number])
        self.lb = tk.Label(window, text = self.q[self.question_number])
        self.lb.grid(row=0, column = 1, columnspan = 4)


        # this gets the list of the list of answers
        self.boop = list(self.q_a.values())
        # this gets a list of just the answers for specified q
        self.needed_boop = self.boop[self.question_number]
             
        self.btn_1 = tk.Button(window, text = self.needed_boop[0], command = lambda:self.results(1, self.result_list))
        self.btn_1.grid(row =1, column =1, columnspan =2)
        self.btn_2 = tk.Button(window, text = self.needed_boop[1], command = lambda:self.results(2, self.result_list))
        self.btn_2.grid(row =1, column =3, columnspan =2)
        self.btn_3 = tk.Button(window, text = self.needed_boop[2], command = lambda:self.results(3, self.result_list))
        self.btn_3.grid(row =2, column =1, columnspan =2)
        self.btn_4 = tk.Button(window, text = self.needed_boop[3], command = lambda:self.results(4, self.result_list))
        self.btn_4.grid(row =2, column =3, columnspan =2)

        self.bck_button = tk.Button(window, text = "<")
        self.bck_button.grid(row =3, column =2)
        self.nxt_button = tk.Button(window, text = ">", command = lambda: [self.next_button(window)])
        self.nxt_button.grid(row =3, column =3)

        self.numb_lbl = self.question_number + 1
        self.numb_lbl = tk.Label(window, text = f"{self.numb_lbl}/{len(self.q)}")
        self.numb_lbl.grid(row =3, column =0)

    def next_button(self, window):
        # this lets the user go from question 1 to question 2
        self.question_number += 1
        if self.question_number < len(self.boop) :
            #self.question_number += 1
            # destroy prev. q buttons
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.btn_3.destroy()
            self.btn_4.destroy()
            self.numb_lbl.destroy()
            self.lb.destroy()
            
            self.btn_1 = tk.Button(window, text = self.needed_boop[0], command = lambda:self.results(1, self.result_list))
            self.btn_1.grid(row =1, column =1, columnspan =2)
            self.btn_2 = tk.Button(window, text = self.needed_boop[1], command = lambda:self.results(2, self.result_list))
            self.btn_2.grid(row =1, column =3, columnspan =2)
            self.btn_3 = tk.Button(window, text = self.needed_boop[2], command = lambda:self.results(3, self.result_list))
            self.btn_3.grid(row =2, column =1, columnspan =2)
            self.btn_4 = tk.Button(window, text = self.needed_boop[3], command = lambda:self.results(4, self.result_list))
            self.btn_4.grid(row =2, column =3, columnspan =2)


            self.lb = tk.Label(window, text = self.q[self.question_number])
            self.lb.grid(row=0, column = 1, columnspan = 4)
            self.numb_lbl = self.question_number + 1
            self.numb_lbl = tk.Label(window, text = f"{self.numb_lbl}/{len(self.q)}")
            self.numb_lbl.grid(row =3, column =0)
            
        else:
            # if they reach the end destroy next button. Create finish button
            # when user clicks other stuff happens
            self.nxt_button.destroy()
            self.finish_btn = tk.Button(window, text = ">", command = lambda: self.the_end(window))
            self.finish_btn.grid(row =3, column =3)

    def results(self, num, the_list):
        the_list.append(num)
        print(the_list)
        # if user entered btn_1 add 1
        # if user ent

    def back_button (self,window):
        # the back button will let the user go back to the next question when clicked
        # this lets the user go from question 1 to question 2
        self.question_number += 1
        if self.question_number < len(self.boop) :
            #self.question_number += 1
            # destroy prev. q buttons
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.btn_3.destroy()
            self.btn_4.destroy()
            self.numb_lbl.destroy()
            self.lb.destroy()
            
            self.btn_1 = tk.Button(window, text = self.needed_boop[0], command = lambda:self.results(1, self.result_list))
            #self.btn_1.pack()
            self.btn_2 = tk.Button(window, text = self.needed_boop[1], command = lambda:self.results(2, self.result_list))
            #self.btn_2.pack()
            self.btn_3 = tk.Button(window, text = self.needed_boop[2], command = lambda:self.results(3, self.result_list))
            #self.btn_3.pack()
            self.btn_4 = tk.Button(window, text = self.needed_boop[3], command = lambda:self.results(4, self.result_list))
            #self.btn_4.pack()


            self.lb = tk.Label(window, text = self.q[self.question_number])
            self.lb.grid(row=0, column = 1, columnspan = 4)
            self.numb_lbl = self.question_number + 1
            self.numb_lbl = tk.Label(window, text = f"{self.numb_lbl}/{len(self.q)}")
            #self.numb_lbl.grid(row =)

        else:
            # if they reach the end destroy next button. Create finish button
            # when user clicks other stuff happens
            self.nxt_button.destroy()
            self.finish_btn = tk.Button(window, text = ">", command = lambda: self.the_end(window))
            #self.finish_btn.pack()

        pass
    
    def the_end(self,window):
        # when i start using grid
        # put in frame and just delete frame
        print("RAHHHHHH")

        # destroy everythin inside the window
        self.finish_btn.destroy()
        self.lb.destroy()
        self.numb_lbl.destroy()
        self.btn_1.destroy()
        self.btn_2.destroy()
        self.btn_3.destroy()
        self.btn_4.destroy()
        self.bck_button.destroy()

        # add the end
        # add results
  
    


     
powr_ranger = Window(root)

root.mainloop()
