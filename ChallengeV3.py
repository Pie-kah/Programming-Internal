'''This is have all the challenges that I will have during the game 
30/7/2025
Pika Ranzinger 
Version one: Write all the code
Version Two: Create the GUI
Version Three: Adding validation and fixing errors'''
import time 
import random
import json 
import tkinter.font as tkfont
from tkinter import *
from tkinter import ttk


class Challenge:
    
    def __init__(self, file_path, turn):
        #variables
        self.file_path = file_path
        self.turn = int(turn)
        self.attempts = 0
        self.i = 1
        self.round_checker = 1
        self.bot_num = random.randint(1,100)
        self.math_q = []
        self.math_a = []
        self.num6 = 0    
        self.image_file_path = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Challenge_Component\help.png"
        
        #root/window
        self.root = Tk()
        self.root.title("Challenge Window")
        
        #sizeing and removing ability to resize
        self.root.resizable(0,0)
        self.root.configure(bg="#ffe6c9")
        
        #preventing window closure
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        
        #fonts
        self.title_font = tkfont.Font(family="Lucida Handwriting", size=24)
        self.num_font = tkfont.Font(family="Century Gothic", size=24)
        self.label_font = tkfont.Font(family="Century Gothic", size=16)
        self.challenge_font = tkfont.Font(family="Century Gothic", size=20)
        self.text_font = tkfont.Font(family="Century Gothic", size=14)
        self.combo_font = tkfont.Font(family="Century Gothic", size=20)
        self.error_font = tkfont.Font(family="Century Gothic", size=12)
        self.button_font = tkfont.Font(family="Tahoma", size=16, weight="bold")        
        
        #containter for the frame for window
        self.container = Frame(self.root, bg="#ffe6c9")
        self.container.grid(row=0, column=0, sticky="nsew")
        
        #column and row configurations 
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)        
        
        #main title
        title_label = Label(self.container, text = "Challenge", bg="#ffe6c9", font = self.title_font)
        title_label.grid(row=0, column=0, pady=20, padx=20)
        
        #helper button 
        self.help_pic = PhotoImage(file=self.image_file_path)
        self.help_pic = self.help_pic.subsample(8)        
        help_button = Button(self.container, image=self.help_pic, width=30, height=30,
                             command=lambda: self.help_window())
        help_button.grid(row=0, column=5, pady=10, padx=10)
        
        #dictionary for frames
        self.frames = {}
        self.frames["Challenge1.1"] = self.create_challenge1_1()
        self.frames["Challenge1.2"] = self.create_challenge1_2()
        self.frames["Challenge2"] = self.create_challenge2()
        self.frames["Challenge3"] = self.create_challenge3()
        self.frames["Challenge5"] = self.create_challenge5()
        self.frames["Challenge6.1"] = self.create_challenge6_1()
        self.frames["Challenge6.2"] = self.create_challenge6_2()
        self.frames["Challenge7"] = self.create_challenge7()
        self.frames["Challenge8"] = self.create_challenge8()
    
    def show_frame(self, name):
        '''display the required name from the dictionary'''
        frame = self.frames[name]
        frame.tkraise() # move frame to the top
    
    def help_window(self):
        '''help window to explain the challenges for all the chapters'''
        help_window = Toplevel(self.root)
        help_window.geometry("500x500")
        help_window.title("Help Window")
        
    
    def exit(self):
        '''does nothing but it prevents window from closing'''
        pass
        
    def run(self):
        '''run the GUI'''
        self.root.mainloop() 
    
    def get_attempts(self):
        '''returning the attempts'''
        return self.attempts
    
    def find_frame(self, num):
        '''finding the frame for challenge'''
        return f"Challenge{num}"
        
    def create_challenge1_1(self):
        '''chapter one, challenge one'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 1.1", bg="#ffe6c9", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=20)
        
        #challenge label
        challenge_label = Label(frame, text= """ 
                T  __ E     U  __ I  V  E  __ __ E     I  __    __    
                26 16 19    7  23 21 13 19 15 20 19    21 20    1
                D  __ __ K     F  __ __ E  __ T  
                6  1  15 22    2  25 15 19 20 26""", 
                               font=("Courier", 15), justify="left",
                               bg="#ffe6c9")
        
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20, padx=20)
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=0, columnspan=4)
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=1,pady=20)
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font)
        answer_entry.grid(row=5, column=2, sticky="we",pady=20)
        
        #button
        checker_button = Button(frame, text="Check Answer",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge1_1(answer_entry, checker_label))
        checker_button.grid(row=6, column=1, columnspan=2, sticky="we", pady=20, padx=20)
        
        
        return frame
    
    def create_challenge1_2(self):
        '''chapter one, challenge two'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 1.2", bg="#ffe6c9", font=self.label_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=(100,0))
        
        #challenge label
        challenge_label = Label(frame, text="", justify="center", bg="#ffe6c9", font=self.num_font)
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20,padx=(100,0))
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=0, columnspan=4)
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=2 ,pady=20, padx=(150,0))
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font)
        answer_entry.grid(row=5, column=3, sticky="we",pady=20)
        
        #buttons
        start_button = Button(frame, text="Start",height=3, width=20, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge1_2_start(challenge_label, start_button))
        start_button.grid(row=6, column=2, sticky="we",  padx=(150,0))        
        
        
        checker_button = Button(frame, text="Check Answer",height=3, width=20, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge1_2_check(answer_entry, checker_label))
        checker_button.grid(row=6, column=3, sticky="we", padx=10)        
        
        
        return frame
    
    def create_challenge2(self):
        '''chapter two challenge'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 2", bg="#ffe6c9", justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=(250,0))
        
        #riddle title label
        title_label = Label(frame, text = f"Riddle {self.turn}", bg="#ffe6c9", justify="center", font=self.challenge_font)
        title_label.grid(row=3, column=0, columnspan=4, pady=20, padx=(250,0))        
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.label_font, 
                                justify="left", bg="#ffe6c9")
        
        challenge_label.grid(row=4, column=1, columnspan=4, pady=20, padx=(125,0))
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=5, column=1, columnspan=4,padx=(250,0))
        
        #hint label
        hint_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        hint_label.grid(row=6, column=1, columnspan=4,padx=(250,0))        
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=7, column=1,pady=20,padx=(250,0))
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font)
        answer_entry.grid(row=7, column=2, sticky="we",pady=20)
        
        #button
        checker_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge2(answer_entry, challenge_label, checker_button, checker_label, hint_label))
        checker_button.grid(row=8, column=1, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        return frame 
    
    def create_challenge3(self):
        '''chapter three challenge'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 3", bg="#ffe6c9", justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=(150,0))
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.text_font, 
                                justify="left", bg="#ffe6c9")
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20, padx=(100,0))
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=1, columnspan=4)
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font)
        answer_entry.grid(row=5, column=1, sticky="w",pady=20)
        
        #button
        checker_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge3(challenge_label, answer_entry, checker_button, checker_label, answer_label))
        checker_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        return frame 
    
    def create_challenge5(self):
        '''chapter five challenge'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #fonts 
        frame.option_add("*TCombobox*Listbox*Font", self.combo_font)
        
        #title label
        title_label = Label(frame, text = "Challenge 5", bg="#ffe6c9", justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=3, pady=20, padx=(150,0))
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.label_font, 
                                justify="left", bg="#ffe6c9")
        challenge_label.grid(row=3, column=1, columnspan=3, pady=20, padx=(100,0))
        
        #answer combo box
        combo_box = ttk.Combobox(frame, state="readonly", font=self.combo_font, 
                                 values=["rock", "paper", "scissors", "lizard", "spock"])
        combo_box.grid(row=4, column=1, pady =20, padx=(200,0))
        combo_box.set("Select an option")
        
        #button
        checker_button = Button(frame, text="Confirm Choice",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge5(challenge_label, combo_box))
        checker_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        return frame
    
    def create_challenge6_1(self):
        '''chapter six, challenge one'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 6.1", bg="#ffe6c9", 
                            justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=(150,0))
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.text_font, 
                                justify="left", bg="#ffe6c9")
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20, padx=(100,0))
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=1, columnspan=4)
        
        #answer label and entry
        answer_label = Label(frame, text="Enter Number:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font, width=10)
        answer_entry.grid(row=5, column=1, sticky="w",pady=20)
        
        #button
        checker_button = Button(frame, text="Check",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge6_1(challenge_label, answer_entry))
        checker_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        return frame 
    
    def create_challenge6_2(self):
        '''chapter six, challenge two'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 6.2", bg="#ffe6c9", 
                            justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=(150,0))
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.text_font, 
                                justify="left", bg="#ffe6c9")
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20, padx=(100,0))
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=0, columnspan=4, padx=(150,0))
        
        #answer label and entry
        answer_label = Label(frame, text="Enter Number:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font, width=10)
        answer_entry.grid(row=5, column=1, sticky="w",pady=20)
        
        answer_label.grid_remove()
        answer_entry.grid_remove()
        
        #buttons
        checker_button = Button(frame, text="Check",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge6_2_check(answer_label, checker_label, answer_entry, start_button))
        checker_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        start_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge6_2_start(start_button, answer_label, answer_entry))
        start_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))        
        
        return frame 
    
    def create_challenge7(self):
        '''chapter seven challenge'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 7", bg="#ffe6c9", 
                            justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=1, columnspan=2, pady=20, )
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.text_font, 
                                justify="left", bg="#ffe6c9")
        challenge_label.grid(row=3, column=1, columnspan=2, pady=20, )
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=1, columnspan=2, )
        
        #buttons
        choice = 1
        button_choices = []
        
        for i in range(4):
            choice_button = Button(frame, text="Confirm Choice",height=2, width=15, font = self.button_font, 
                                    relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                    command=lambda i=i: self.challenge7_choice(i, button_choices, 
                                    checker_label, challenge_label, start_button))
            choice += 1
            button_choices.append(choice_button)
        
        start_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                    relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                    command=lambda: self.challenge7_start(button_choices, start_button, challenge_label))
        start_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))        
            
        return frame
    
    def create_challenge8(self):
        '''chapter eight challenge'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 8", bg="#ffe6c9", justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=1, columnspan=2, pady=20, padx=(250))
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=3, column=1, columnspan=2,padx=(250))
        
        #hint label
        hint_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        hint_label.grid(row=4, column=1, columnspan=2,padx=(250))        
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font,width=15)
        
        #button
        checker_button = Button(frame, text="Check",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge8_check(answer_label, checker_label, answer_entry, start_button, hint_label))
        checker_button.grid(row=7, column=1, columnspan=2, sticky="", pady=20, padx=(250))
        
        start_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                    relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                    command=lambda: self.challenge8_start(start_button, answer_label, answer_entry))
        start_button.grid(row=7, column=1, columnspan=2, sticky="", pady=20, padx=(250))          
        
        return frame 
    
    def challenge1_1(self, answer_text, checker):
        '''checking if the answer for challenge 1.1 is correct'''
        #answer
        sentence = "The universe is a dark forest"
        
        #user answer
        answer = answer_text.get()
        
        if answer.lower() == sentence.lower():
            #checking if the answer matches the sentence
            checker.config(text = "Correct Answer")
            self.root.after(1500, self.root.destroy)
        else:
            checker.config(text="Wrong Answer")
            self.attempts += 1
        
        #clearing the entry
        answer_text.delete(0, END)
    
    def challenge1_2_start(self, label, button):
        '''starting challenge 1.2'''
        #reseting variables 
        self.numbers = []
        i = 0
        
        #after first press the button becomes a restart rather than start
        button.config(text="Restart")
        
        while i < 5:
            #5 random numbers printed for 2 seconds each 
            number = random.randint(0,9)
            self.numbers.append(number)
            label.after(i*2000, lambda n=number: label.config(text=n))
            i += 1
        #cleared after the final one 
        label.after(10000, lambda: label.config(text=""))   
    
    def challenge1_2_check(self, answer_text, checker):
        '''checking challenge 1.2'''
        #variables
        answers = []
        answer = answer_text.get()
        
        #splitting answer
        answer.split()
        for items in answer:
            #making it a integer and then appending it to a list
            items = int(items)
            answers.append(items)
        
        if answers == self.numbers:
            #checking if it's matching 
            checker.config(text = "Correct Answer")
            self.root.after(1500, self.root.destroy)
        else:
            #adds attempts if wrong 
            checker.config(text="Wrong Answer")
            self.attempts += 1            
        
        #clearing the entry
        answer_text.delete(0, END)             
    
    def challenge2(self, answer_text, label, button, checker, hint):
        '''challenge 2 checker'''
        #variables
        user_answer = answer_text.get()
        
        if self.turn == 1:
                #riddle one 
                answer1 = "regret"
                button.config(text="Check")
                label.config(text="""
                        Start with silence in a heavy bowl,
                        Stir with shadows from a sleepless soul.
                        Sprinkle years lost to shame and pride—
                        Then bake until the truth can’t hide.
                        Tell me, wanderer, what is it I make?""")
                if user_answer.lower() == answer1 and user_answer != "":
                    #checks if user answer and answer are same
                    checker.config(text = "Correct Answer")
                    self.root.after(1500, self.root.destroy)
                    hint.config(text="")
                elif user_answer.lower() != answer1 and user_answer != "":
                    #adds attempts if wrong 
                    checker.config(text="Wrong Answer")
                    self.attempts += 1 
                    if self.attempts >= 5:
                        hint1 = list(answer1)
                        if self.i == len(answer1):
                            hint.config(text=f"Hint: answer is {answer1}")
                        else:
                            hint.config(text=f"Hint: answer starts with {hint1[0:self.i]}")
                            self.i += 1                       
                else:
                    pass
                   
                    
        elif self.turn == 2:
                #riddle two
                answer2 = ["an absence", "absence", "absences"]
                button.config(text="Check")
                label.config(text="""
                I tick but make no sound,
                I’m neither lost nor found.
                I measure time through lack,
                Yet wear no numbered plaque.
                What am I? """)
                if user_answer.lower() in answer2 and user_answer != "":
                    #checks if user answer and answer are same
                    checker.config(text = "Correct Answer")
                    self.root.after(1500, self.root.destroy)
                    hint.config(text="")
                elif user_answer.lower() not in answer2 and user_answer != "":
                    #adds attempts if wrong 
                    checker.config(text="Wrong Answer")
                    self.attempts += 1  
                    if self.attempts >= 5:
                        hint2 = list(answer2[1])
                        if self.i == len(answer2[1]):
                            hint.config(text=f"Hint: answer is {answer2[1]}")
                        else:
                            hint.config(text=f"Hint: answer starts with {hint2[0:self.i]}")
                            self.i += 1                       
                else:
                    pass
                    
        elif self.turn == 3:
                #riddle three
                answer3 = ["a word", "word", "words"]
                button.config(text="Check")
                label.config(text="""
                I fall, yet never sink.
                I lift, yet carry weight.
                I shine, yet never blind.
                I wound, though soft and light.
                I am part of pain and beauty both.
                What am I? """)
                if user_answer.lower() in answer3 and user_answer != "":
                    #checks if user answer and answer are same
                    checker.config(text = "Correct Answer")
                    self.root.after(1500, self.root.destroy)
                    hint.config(text="")
                elif user_answer.lower() not in answer3 and user_answer != "":
                    #adds attempts if wrong 
                    checker.config(text="Wrong Answer")
                    self.attempts += 1  
                    if self.attempts >= 5:
                        hint3 = list(answer3[1])
                        if self.i == len(answer3[1]):
                            hint.config(text=f"Hint: answer is {answer3[1]}")
                        else:
                            hint.config(text=f"Hint: answer starts with {hint3[0:self.i]}")
                            self.i += 1                      
                else:
                    pass
        else:
                pass
                
        #clearing the entry
        answer_text.delete(0, END)         
            
    def challenge3(self, label, answer_text, button, checker_label, answer_label):
        '''challenge for chapter 3'''
        #variables 
        answer = answer_text.get()
        
        #config button
        button.config(text="Continue")
        
        if self.round_checker == 1:
            #first set
            #setting it up
            answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
            answer_text.grid(row=5, column=1, sticky="w",pady=20)
            checker_label.config(text="")
            button.config(text="Go Down Route")
            #printing everything 
            label.config(text="""
                    1. A knight missing its heart, silent and unmoving.
                    2. A scholar chained to burning books, eyes closed in contemplation.
                    3. A child with eyes that blinked stars, holding a feather soaked in ink.
    
                    Each offered a price:
                    “Take my path and lose your pride.”
                    “Take mine and lose your name.”
                    “Take mine and face the truth that breaks.”
                       """)
            #incase of accidental clicks or start buttons/continue 
            if answer == "":
                pass
            elif int(answer) == 3:
                #if the answer is correct
                checker_label.config(text="Correct Answer")
                button.config(text="Continue")
                answer_text.grid_remove()
                answer_label.grid_remove()
                self.round_checker = 2 
                label.config(text="Lysander arrives at another set of doors, this one has five doors.")
            else: 
                #if the answer is wrong 
                self.attempts += 1 
                checker_label.config(text="Incorrect")
                button.config(text="Continue")
                answer_text.grid_remove()
                answer_label.grid_remove()
                self.round_checker = 1  
                label.config(text="""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)
        
        elif self.round_checker == 2:
            #second set
            #setting everything up
            answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
            answer_text.grid(row=5, column=1, sticky="w",pady=20)
            checker_label.config(text="")
            button.config(text="Go Down Route")
            #printing the challenge
            label.config(text="""
                1. Denial   -   depicting as a man aggressively shaking 
                                his head refusing to even look at Lysander
                2. Anger    -   depicting as a woman screaming towards Lysander
                3. Bargaining - depicting a person on their knees with their 
                                hands clasped praying for something 
                4. Depression - depicting a man with his back against a wall 
                                hunching over a picture frame
                5. Acceptance - depicting a woman standing at a gravestone, 
                                she smiling sadly
                """)
            #incase of misclicks or continue 
            if answer == "":
                pass
            elif int(answer) == 4:
                #if answer is correct
                checker_label.config(text="Correct Answer")
                button.config(text="Continue")
                answer_text.grid_remove()
                answer_label.grid_remove()
                self.round_checker = 3 
                label.config(text="""
                Lysander arrives in a circular room. The room had 7 doors when
                you excluded the door Lysander had just entered from.""")
            else: 
                #if answer is wrong 
                self.attempts += 1 
                checker_label.config(text="Incorrect")
                button.config(text="Continue")
                answer_text.grid_remove()
                answer_label.grid_remove()
                self.round_checker = 1  
                label.config(text="""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)
                
        elif self.round_checker == 3:
            #last set
            #setting everything up
            answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
            answer_text.grid(row=5, column=1, sticky="w",pady=20)
            checker_label.config(text="")
            button.config(text="Go Down Route")
            #printing the challenge text
            label.config(text="""
            Each door each had just one word written on it.
                    1. Pride
                    2. Greed
                    3. Wrath
                    4. Envy
                    5. Lust
                    6. Gluttony
                    7. Sloth
                    """)
            #in case of continue or misclicks 
            if answer == "":
                pass
            elif int(answer) == 6:
                #if answer is correct
                checker_label.config(text="Correct Answer")
                button.grid_remove()
                answer_text.grid_remove()
                answer_label.grid_remove()
                self.root.after(1500, self.root.destroy)
            else: 
                #if answer is wrong 
                self.attempts += 1 
                checker_label.config(text="Incorrect")
                button.config(text="Continue")
                answer_text.grid_remove()
                answer_label.grid_remove()
                self.round_checker = 1  
                label.config(text="""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)       
                
        #clearing the entry
        answer_text.delete(0, END)         
    
    def challenge5(self, label, combo):
        options = ["rock", "paper", "scissors", "lizard", "spock"]
        bot = options[random.randint(0,4)]
        user = combo.get()
        
        #if statements for what beats what 
        if bot == "rock" and (user == "scissors" or user == "lizard"):
            self.attempts += 1 
            label.config(text="Bot wins")
        elif bot == "paper" and (user == "rock" or user == "spock"):
            self.attempts += 1 
            label.config(text="Bot wins")
        elif bot == "scissors" and (user == "paper" or user == "lizard"):
            self.attempts += 1 
            label.config(text="Bot wins")
        elif bot == "lizard" and (user == "paper" or user == "spock"):
            self.attempts += 1 
            label.config(text="Bot wins")
        elif bot == "spock" and (user == "rock" or user == "scissors"):
            self.attempts += 1 
            label.config(text="Bot wins")
        elif user == "Select an option":
            pass
        elif user == bot:
            self.attempts += 1 
            label.config(text="It's a tie")
        else: 
            label.config(text="Victory!")  
            self.root.after(1500, self.root.destroy)
    
    def challenge6_1(self, label, answer_text):
        #getting the user input 
        user = answer_text.get()
        user = int(user)
        
        if user != self.bot_num:
            #checking if the incorrect num is higher or lower 
            self.attempts += 1 
            if user > self.bot_num:
                label.config(text="Lower")
            elif user < self.bot_num:
                label.config(text="Higher")
        elif user == self.bot_num:
            #if correct 
            label.config(text="Correct")
            self.root.after(1500, self.root.destroy)
        
        #clearing the entry
        answer_text.delete(0, END)  
        
    def challenge6_2_start(self, button, answer_label, answer_entry):
        self.start_time = time.time()
        button.grid_remove()
        self.math_q = []
        self.math_a = []
        self.num6 = 0 
        
        with open(self.file_path) as file:
            #opens the file 
            questions = json.load(file)
            for chapter, challenge in questions.items():
                #finds the correct set for this challenge
                if chapter == "ch6.2":
                    maths = challenge
        
        self.math_q = random.sample(list(maths.keys()), 10)
        self.math_a = [maths[q] for q in self.math_q]
        
        answer_label.config(text=self.math_q[self.num6])
        
        answer_label.grid(row=5, column=0,pady=20,padx=(250,0), sticky="w")
        answer_entry.grid(row=5, column=1, sticky="w",pady=20)        
    
    def challenge6_2_check(self, label, correct, answer_text, start_button):
        answer = answer_text.get()
        answer = int(answer)
        
        if self.num6 == 10:
            #reached the end of question
            pass
        elif answer == self.math_a[self.num6]:
            #if answer is correct
            self.num6 += 1
            correct.config(text="Correct")
        else:
            self.attempts += 1 
            correct.config(text="Wrong Answer")
        
        #clearing the entry
        answer_text.delete(0, END)         
        
        if self.num6 == 10:
            end_time = time.time()
            total_time = end_time - self.start_time
            if total_time < 60:
                #if less than 60 seconds
                correct.config(text="You Win")
                label.grid_remove()
                answer_text.grid_remove()
                self.root.after(1500, self.root.destroy) 
            else:
                #doesn't beat the needed time 
                correct.config(text="Try Again")
                start_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))
                label.grid_remove()
                answer_text.grid_remove()
        else:
            #continue onto next question if not done 
            label.config(text=self.math_q[self.num6])
    
    def challenge7_start(self, button_lists, start_button, label):
        #variables
        self.score = 0
        self.num7 = 0 
        self.question7 = []
        self.answer7 = []
        self.choices7 = []
        
        #removing start button
        start_button.grid_remove()
        
        #read json file 
        with open(self.file_path) as f:
            file = json.load(f)
            for key, value in file.items():
                if key == "ch7":
                    quiz = value
        
        for key, value in quiz.items():
            q = value["question"]
            c = value["choices"]
            a = value["answer"]
            
            #shuffle choices
            random.shuffle(c)
            
            #add to lists
            self.question7.append(q)
            self.answer7.append(a)
            self.choices7.append(c)
            
        first_set = self.choices7[self.num7]
        choice_text = 0
        i = 0 
        
        for btn in button_lists:
            #showing the button with choices
            row_num = i//2 
            col_num = i%2
            btn.grid(row=(row_num+5), column=col_num+1, padx=(80,0), pady=10, sticky="we")
            btn.config(text=first_set[choice_text])
            choice_text += 1
            i += 1
        
        #showing the question 
        question = self.question7[self.num7]
        label.config(text=question)   
    
    def challenge7_choice(self, index, button_list, correct, label, start_button):
        #inputs
        selected = self.choices7[self.num7]
        choice = selected[index]
        
        #checker
        if choice == self.answer7[self.num7]:
            #if answer is correct
            self.score += 1
            correct.config(text="Correct Answer", fg = "green")
        else:
            #if answer is incorrect
            self.attempts += 1
            correct.config(text="Incorrect", fg = "red")
        
        #onto next question
        self.num7 += 1
        
        if self.num7 != 15:
            #checking it isnt end of questions 
            choice_set = self.choices7[self.num7]
            choice_text = 0
            i = 0
            
            for btn in button_list:
                #showing the button with choices 
                row_num = i//2 
                col_num = i%2
                btn.grid(row=(row_num+5), column=col_num+1, padx=(50), pady=10, sticky="we")
                btn.config(text=choice_set[choice_text])
                choice_text += 1
                i += 1
            
            #showing the question
            question = self.question7[self.num7]
            label.config(text=question)
        
        elif self.num7 == 15:
            #if the end is reached 
            if self.score >= 12:
                #checking you have winning score
                correct.config(text="You Win!", fg="black")
                self.root.after(1500, self.root.destroy) 
            else:
                #if not try again 
                correct.config(text="You Lose", fg="black")
                for btn in button_list:
                    btn.grid_remove()
                start_button.grid(row=6, column=0, columnspan=2, sticky="we", pady=20, padx=(250,0))
                        
    
    def challenge8_start(self, button, answer_label, answer_entry):
        #variables 
        self.num8 = 0
        self.questions8 = []
        self.choices8 = []
        self.answers8 = []
        
        #remove start button
        button.grid_remove()
        
        #read json file 
        with open(self.file_path) as f:
            file = json.load(f)
            
            for key, value in file.items():
                if key == "ch8":
                    quiz = value
        
        for key, value in quiz.items():
            #getting the values
            q = value["question"]
            a = value["answer"]
            c = value["choices"]
            
            #add to lists 
            self.questions8.append(q)
            self.answers8.append(a)
            self.choices8.append(c)
            
        #showing answer
        answer_label.config(text=self.questions8[self.num8])
        
        #showing answer label and entry
        answer_label.grid(row=5, column=1,columnspan=2,pady=20, padx=(250))
        answer_entry.grid(row=6, column=1, columnspan=2,pady=20, padx=(250))        
    
    def challenge8_check(self, label, correct, answer_text, start_button, hint):
        answer = answer_text.get()
        
        if self.num8 == 15:
            #checking its not max
            pass
        elif answer.lower() == self.answers8[self.num8].lower():
            self.num8 += 1 
            correct.config(text="Correct Answer", fg="green")
            hint.config(text="")
        else:
            self.attempts += 1
            correct.config(text="Incorrect", fg="red")
        
        if self.num8 != 15:
            hints = self.choices8[self.num8]
            all_text = ""
        
        if self.attempts >= ((self.num8+1)*5):
            for i in range(len(hints)):
                sentence = f"{i+1}. {hints[i]}"
                all_text = all_text+"\n"+sentence
            
            hint.config(text=f""" Hint:
            {all_text}""")
            
        
        answer_text.delete(0, END)
        
        if self.num8 == 15:
            #if the end is reached 
            correct.config(text="You Win!", fg="black")
            self.root.after(1500, self.root.destroy) 
        else:
            #if not continue on 
            label.config(text=self.questions8[self.num8])
            

CHALLENGE_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Challenge_Component\challenge.json"
CHALLENGE_CHAPTERS = {"Forest of Veymor" : "1.1",
                      "Meeting the Sable-Faced Guide" : "1.2",
                      "Riddle One: The Hollow Recipe" : "2", 
                      "Riddle Two: The Invisible Clock" : "2", 
                      "Riddle Three: A Feather's Burden" : "2",
                      "The Chamber of Choice" :  "3",
                      "Labors of the Cursed" : "5",
                      "Monsters Worn Like Memories" : "6.1", 
                      "Trial of the Deep Bend" : "6.2",
                      "The Final Stand" : "7", 
                      "Ascending in Confession" : "8"}
NUMBERS = ["1.1", "1.2", "2", "2", "2", "3", "5", "6.1", "6.2", "7", "8"]

turn = 2

chal = Challenge(CHALLENGE_FILE_PATH, turn)
frame = chal.find_frame(NUMBERS[2])
chal.show_frame(frame)
chal.run()

attempts = chal.get_attempts()
print(attempts)

#for i in range(3):
    #chal = Challenge(CHALLENGE_FILE_PATH, turn)
    #frame = chal.find_frame(NUMBERS[2])
    #chal.show_frame(frame)
    #chal.run()
    
    #turn += 1 
    #attempts = chal.get_attempts()
    #print(attempts)    
