"""
Filename: Shoe quiz.

Author: shelley

Date: 19.09.23

Description: This is a quiz for the user to figure out what shoe would
suit their lifestyle and style.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Button

# this is just window setup
root = tk.Tk()
root.geometry("300x400")
root.title("Find your perfect shoe")
root.resizable(False, False)


class Window:
    """This class does basically everythinhg to run the program."""

    def __init__(self, window):
        """Create grid and also
        the things for the start page
        and also the questions and answers for the quiz.
        """
        # this is the grid layout
        window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=2)
        window.rowconfigure([0, 1, 2, 3], weight=5)
        # background colour of window
        window.configure(bg="#fff")

        # start page welcome text and START button
        start_font = ("Tahoma",10)
        welcome_text = "Welcome to this quiz.\nPress START to continue"
        self.welcome = tk.Label(window,
                                text=welcome_text,
                                font = start_font,
                                bg="#FFF")
        self.start = Button(window,
                            text="\nSTART\n",
                            command=lambda: [self.welcome.destroy(),
                                            self.start.destroy(),
                                            self.next_button(window)])

        # grid for the start page
        self.welcome.grid(row=0, column=1, columnspan=6, rowspan=2)
        self.start.grid(row=2, column=2, columnspan=4)

        # this is a list of what the user clicks
        self.result_list = []

        # use \n for the button so that they aren't small
        # dictionary of all the questions and answers
        self.q_a = {"\nWhat colours do you like?": ["\nBlack/White\n",
                                                    "\nNeutral\n",
                                                    "\nPastel\n", "\nBold\n"],
                    "What does most of your\nday consist of?": ["\nWalking\n",
                                                                "\nSitting\n",
                                                                "\nRunning\n",
                                                                "\nZiplining\n"
                                                                ],
                    "What matters to you in\na pair of shoes?": ["\nComfort\n",
                                                                "\nEasy to run\n",
                                                                "\nThey're cool\n",
                                                                "\nAdds height\n"
                                                                ],
                    "  What is your personal\nclothing style?": ["\nMinimalist\n",
                                                                "\nStreetwear\n",
                                                                "\nAcademia\n",
                                                                "\nJust clothes\n"
                                                                ]}

        # this is the starting question number
        self.q_number = 0

        # this gets ALL the question and adds it to a list
        "self.q = list(self.q_a.keys())"
        self.question_list = list(self.q_a.keys())
        # this gets the list of answers and puts it in a list
        "self.boop = list(self.q_a.values())"
        self.answer_list = list(self.q_a.values())
        self.users_answer_list = []

        #the font tuple for the questions
        self.font_tuple = ("Tahoma", 9, "bold")

        self.user_retry = 0

    def next_button(self, window):
        """Return the next question."""

        # FROM 2nd q. up only if the user has entered
        # something in their previous question
        if 0 < self.q_number < len(self.answer_list):
            if self.user_retry > 0:
                self.btn_1.destroy()
                self.btn_2.destroy()
                self.btn_3.destroy()
                self.btn_4.destroy()
                self.numb_lbl.destroy()
                self.question_label.destroy()
                self.question_frame.destroy()
                self.nxt_button.destroy()
            else:
                pass
            self.the_answers = self.answer_list[self.q_number]

            # destroy prev. q buttons and labels
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.btn_3.destroy()
            self.btn_4.destroy()
            self.numb_lbl.destroy()
            self.question_label.destroy()
            self.question_frame.destroy()
            self.nxt_button.destroy()


            
            self.btn_1 = Button(window, text=self.the_answers[0],
                                command=lambda: self.results(1))
            self.btn_1.grid(row=1, column=1, columnspan=2)
            self.btn_2 = Button(window, text=self.the_answers[1],
                                command=lambda: self.results(2))
            self.btn_2.grid(row=1, column=3, columnspan=2)
            self.btn_3 = Button(window, text=self.the_answers[2],
                                command=lambda: self.results(3))
            self.btn_3.grid(row=2, column=1, columnspan=2)
            self.btn_4 = Button(window, text=self.the_answers[3],
                                command=lambda: self.results(4))
            self.btn_4.grid(row=2, column=3, columnspan=2)

            # questions
            self.question_frame = tk.Frame(master=window, bg="#ECECEC",
                                           width=200, height=50)
            self.question_label = tk.Label(self.question_frame,
                                           text=self.question_list[self.q_number
                                                                   ],
                                           bg="#ECECEC", fg="#609F63",
                                           font = self.font_tuple)
            self.question_frame.grid(row=0, column=1, columnspan=4)
            self.question_frame.grid_propagate(False)
            self.question_label.grid(padx=15, pady = 5)

            self.nxt_button = Button(window, text=">",
                                     command=lambda: [self.save_answer(window),
                                                      self.next_button(window)
                                                      ],
                                     width=3)
            self.nxt_button.grid(row=3, column=3)

            # question number
            q_num_lbl =f"{self.q_number+1}/{len(self.question_list)}"

            self.numb_lbl = tk.Label(window,
                                     text=q_num_lbl,
                                     bg= "#fff")
            self.numb_lbl.grid(row=3, column=0, sticky = "E")

        # this is for the first question
        elif (self.q_number < len(self.answer_list)
              and len(self.result_list) == self.q_number):
            if self.user_retry > 0:
                self.btn_1.destroy()
                self.btn_2.destroy()
                self.btn_3.destroy()
                self.btn_4.destroy()
                self.numb_lbl.destroy()
                self.question_label.destroy()
                self.question_frame.destroy()
                self.bck_button.destroy()
                self.nxt_button.destroy()
            else:
                pass
            self.user_retry += 1
            # this adds the question and adds it into the window
            self.question_frame = tk.Frame(master=window, bg="#ECECEC",
                                           width=200, height=50)
            self.question_label = tk.Label(self.question_frame,
                                           text=self.question_list[self.q_number],
                                           bg="#ECECEC", fg="#609F63",
                                           font = self.font_tuple)
            self.question_frame.grid(row=0, column=1, columnspan=4)
            self.question_frame.grid_propagate(False)
            self.question_label.grid(padx=20)

            # this gets a list of just the answers for specified q
            self.the_answers = self.answer_list[self.q_number]

            # all the answer buttons + gridded
            self.btn_1 = Button(window, text=self.the_answers[0],
                                command=lambda: self.results(1))
            self.btn_1.grid(row=1, column=1, columnspan=2)
            self.btn_2 = Button(window, text=self.the_answers[1],
                                command=lambda: self.results(2))
            self.btn_2.grid(row=1, column=3, columnspan=2)
            self.btn_3 = Button(window, text=self.the_answers[2],
                                command=lambda: self.results(3))
            self.btn_3.grid(row=2, column=1, columnspan=2)
            self.btn_4 = Button(window, text=self.the_answers[3],
                                command=lambda: self.results(4))
            self.btn_4.grid(row=2, column=3, columnspan=2)

            # back button and next button
            self.bck_button = Button(window, text="<",
                                     command=lambda: [self.back_question(),
                                                      self.back_button(window)
                                                      ],
                                     width=3)
            self.bck_button.grid(row=3, column=2)
            self.nxt_button = Button(window, text=">",
                                     command=lambda: [self.save_answer(window),
                                                      self.next_button(window)
                                                      ],
                                     width=3)
            self.nxt_button.grid(row=3, column=3)

            # this adds the question number into a list
            q_num_lbl =f"{self.q_number+1}/{len(self.question_list)}"
            self.numb_lbl = tk.Label(window,
                                     text=q_num_lbl,
                                     bg = "#FFF")
            self.numb_lbl.grid(row=3, column=0, sticky = "E")

        elif self.q_number == len(self.answer_list):
            # destroy prev. q buttons and labels.
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.btn_3.destroy()
            self.btn_4.destroy()
            self.numb_lbl.destroy()
            self.question_label.destroy()
            self.question_frame.destroy()
            # if the user is on the last question
            self.the_end(window)
        else:
            pass
    def add_question(self):
        """Add to the question number."""
        self.q_number += 1

    def back_question(self):
        """Reduce the question nummber to go back."""
        if self.q_number >= 1:
            self.q_number -= 1
        else:
            pass

    def results(self, num):
        """Add result the user chose into a list."""
        # must change append so that when user goes
        # back the question thats meant to be changed is changed
        self.users_answer_list.append(num)
        # if user entered btn_1 add 1
        # if user ent
        return self.users_answer_list

    def no_answer(self, window):
        """Display popup if user doesn't give an answer."""
        pop_up = Toplevel(window)
        pop_up.geometry("170x80")
        pop_up.resizable(False, False)
        error_label = tk.Label(pop_up,
                               text="Select an option before\ncontinuing")
        error_label.grid(padx=15)
        close_butt = Button(pop_up, text="CLOSE",
                            command=lambda: pop_up.destroy())
        close_butt.grid()

    def results_conjugate(self, num):
        """Add result the user chose into a list."""
        # this is for questions when the user clicked the back button
        self.users_answer_list.append(num)

    def save_answer(self, window):
        """Save user answer to a list"""
        if len(self.users_answer_list) == 1:
            self.result_list = self.result_list + self.users_answer_list
            self.add_question()
        elif len(self.users_answer_list) > 1:
            self.result_list.append(self.users_answer_list[-1])
            self.add_question()
        else:
            # if the user gives no answer
            self.no_answer(window)
        self.users_answer_list.clear()

    def saved_from_back(self, window):
        """Save users answer to a list when they've clicked back"""
        if len(self.users_answer_list) == 1:
            self.result_list.insert(self.q_number,
                                    self.users_answer_list[0])
            self.add_question()

        elif len(self.users_answer_list) > 1:
            self.result_list[self.q_number] = self.users_answer_list[-1]
            self.add_question()

        else:
            # if the user gives no answer display popup window
            self.no_answer(window)

        self.users_answer_list.clear()

    def back_button (self,window):
        # the back button will let the user go back
        # to the next question when clicked
        # this lets the user go from question 1 to question 2
        # if user clicks back button, the question nunber is back one
        if 0 <= self.q_number < len(self.answer_list):

            self.the_answers = self.answer_list[self.q_number]
            # destroy prev. q buttons
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.btn_3.destroy()
            self.btn_4.destroy()
            self.numb_lbl.destroy()
            self.question_label.destroy()
            self.nxt_button.destroy()
            self.question_frame.destroy()

            self.btn_1 = Button(window, text=self.the_answers[0],
                                command=lambda: self.results_conjugate(1))
            self.btn_1.grid(row=1, column=1, columnspan =2)
            self.btn_2 = Button(window, text=self.the_answers[1],
                                command=lambda: self.results_conjugate(2))
            self.btn_2.grid(row=1, column=3, columnspan =2)
            self.btn_3 = Button(window, text=self.the_answers[2],
                                command=lambda: self.results_conjugate(3))
            self.btn_3.grid(row=2, column=1, columnspan =2)
            self.btn_4 = Button(window, text=self.the_answers[3],
                                command = lambda: self.results_conjugate(4))
            self.btn_4.grid(row=2, column=3, columnspan =2)

            self.question_frame = tk.Frame(master=window, bg="#ECECEC",
                                           width=200, height=50)
            self.question_label = tk.Label(self.question_frame,
                                           text=self.question_list[self.q_number
                                                                   ],
                                           bg="#ECECEC", fg="#609F63",
                                           font = self.font_tuple)
            self.question_frame.grid(row=0, column=1, columnspan=4)
            self.question_frame.grid_propagate(False)
            self.question_label.grid(padx=15, pady = 5)

            #print(type(self.numb_lbl))
            lbl_text = f"{self.q_number+1}/{len(self.question_list)}"
            self.numb_lbl = tk.Label(window,
                                     text= lbl_text,
                                     bg = "#fff")
            self.numb_lbl.grid(row=3, column=0, sticky = "E")

            self.nxt_button = Button(window, text=">",
                                     command=lambda: [
                                         self.saved_from_back(window),
                                                      self.next_button(window)
                                                      ], width=3)
            self.nxt_button.grid(row=3, column=3)

        else:
            self.q_number += 1

    def the_end(self,window):
        # when i start using grid
        # put in frame and just delete frame

        # destroy everythin inside the window
        #self.finish_btn.destroy()
        self.question_label.destroy()
        self.numb_lbl.destroy()
        self.btn_1.destroy()
        self.btn_2.destroy()
        self.btn_3.destroy()
        self.btn_4.destroy()
        self.bck_button.destroy()
        self.nxt_button.destroy()
        # add the end
        # add results
        if sum(self.result_list) > 0 and sum(self.result_list) <= 4:
            final_label = tk.Label(text="sneakers", bg="#fff")
        elif sum(self.result_list) > 4 and sum(self.result_list) <= 15:
            final_label = tk.Label(text="Boots :P", bg = "#fff")
        elif sum(self.result_list) > 15 and sum(self.result_list) <= 26:
            final_label = tk.Label(text="Platform Sneakers", bg="#fff")
        else:
            print("-------------\nYour total is", sum(self.result_list))
            final_label = tk.Label(text="Loafers", bg="#fff")
            print(self.result_list)
        final_label.grid(row=1, column=1, rowspan=2, columnspan=6)

open_window = Window(root)

root.mainloop()
