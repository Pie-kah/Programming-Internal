'''This is have all the challenges that I will have during the game 
30/7/2025
Pika Ranzinger 
Version one: Write all the code
Version Two: Create the GUI'''
import time 
import random
import json 
import tkinter.font as tkfont
from tkinter import *


class Challenge:
    
    def __init__(self, file_path, turn):
        #variables
        self.file_path = file_path
        self.turn = int(turn)
        self.attempts = 0
        
        #root/window
        self.root = Tk()
        self.root.title("Challenge Window")
        
        #sizeing and removing ability to resize
        self.root.resizable(0,0)
        self.root.configure(bg="#ffe6c9")
        
        #fonts
        self.title_font = tkfont.Font(family="Lucida Handwriting", size=24)
        self.num_font = tkfont.Font(family="Century Gothic", size=24)
        self.label_font = tkfont.Font(family="Century Gothic", size=16)
        self.challenge_font = tkfont.Font(family="Century Gothic", size=20)
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
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.label_font, 
                                justify="left", bg="#ffe6c9")
        
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20, padx=20)
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=0, columnspan=4)
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=1,pady=20,padx=(250,0))
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font)
        answer_entry.grid(row=5, column=2, sticky="we",pady=20)
        
        #button
        checker_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge2(answer_entry, challenge_label, checker_button, checker_label))
        checker_button.grid(row=6, column=1, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        return frame 
    
    def create_challenge3(self):
        '''chapter three challenge'''
        #frame
        frame = Frame(self.container,  bg="#ffe6c9", highlightthickness=5,
                      highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        frame.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)
        
        #title label
        title_label = Label(frame, text = "Challenge 3", bg="#ffe6c9", justify="center", font=self.challenge_font)
        title_label.grid(row=2, column=0, columnspan=4, pady=20, padx=(250,0))
        
        #challenge label
        challenge_label = Label(frame, text= "", font=self.label_font, 
                                justify="left", bg="#ffe6c9")
        
        challenge_label.grid(row=3, column=0, columnspan=4, pady=20, padx=20)
        
        #checker label
        checker_label = Label(frame, text="", bg="#ffe6c9", font=self.error_font)
        checker_label.grid(row=4, column=0, columnspan=4)
        
        #answer label and entry
        answer_label = Label(frame, text="Answer:", bg="#ffe6c9", font=self.label_font)
        answer_label.grid(row=5, column=1,pady=20,padx=(250,0))
        
        answer_entry = Entry(frame, bg="#ffe6c9", font=self.label_font)
        answer_entry.grid(row=5, column=2, sticky="we",pady=20)
        
        #button
        checker_button = Button(frame, text="Start",height=3, width=30, font = self.button_font, 
                                relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                                command=lambda: self.challenge3(answer_entry, challenge_label, checker_button, checker_label))
        checker_button.grid(row=6, column=1, columnspan=2, sticky="we", pady=20, padx=(250,0))
        
        return frame 
    
    def create_challenge5(self):
        pass
    
    def create_challenge6_1(self):
        pass
    
    def create_challenge6_2(self):
        pass
    
    def create_challenge7(self):
        pass
    
    def create_challenge8(self):
        pass
    
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
    
    def challenge2(self, answer_text, label, button, checker): #issue
        '''challenge 2 checker'''
        #variables
        clear = 0
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
                elif user_answer.lower() != answer1 and user_answer != "":
                    #adds attempts if wrong 
                    checker.config(text="Wrong Answer")
                    self.attempts += 1   
                else:
                    pass
                    
        elif self.turn == 2:
                #riddle two
                answer2 = "an absence"
                button.config(text="Check")
                label.config(text=""""
                I tick but make no sound,
                I’m neither lost nor found.
                I measure time through lack,
                Yet wear no numbered plaque.
                What am I? """)
                if user_answer.lower() == answer2 and user_answer != "":
                    #checks if user answer and answer are same
                    checker.config(text = "Correct Answer")
                    self.root.after(1500, self.root.destroy)
                elif user_answer.lower() != answer2 and user_answer != "":
                    #adds attempts if wrong 
                    checker.config(text="Wrong Answer")
                    self.attempts += 1   
                else:
                    pass
                    
        elif self.turn == 3:
                #riddle three
                answer3 = "a word"
                button.config(text="Check")
                label.config(text="""
                I fall, yet never sink.
                I lift, yet carry weight.
                I shine, yet never blind.
                I wound, though soft and light.
                I am part of pain and beauty both.
                What am I? """)
                if user_answer.lower() == answer3 and user_answer != "":
                    #checks if user answer and answer are same
                    checker.config(text = "Correct Answer")
                    self.root.after(1500, self.root.destroy)
                elif user_answer.lower() != answer3 and user_answer != "":
                    #adds attempts if wrong 
                    checker.config(text="Wrong Answer")
                    self.attempts += 1   
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
            print("""
                    1. A knight missing its heart, silent and unmoving.
                    2. A scholar chained to burning books, eyes closed in contemplation.
                    3. A child with eyes that blinked stars, holding a feather soaked in ink.
    
                    Each offered a price:
                    “Take my path and lose your pride.”
                    “Take mine and lose your name.”
                    “Take mine and face the truth that breaks.”
                       """)            
            
            if answer != 3:
                #wrong choice
                print("""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)
                self.attempt += 1
                
            elif answer == 3:
                #correct choice continues on
                choices.append(choice1)
                print(""" 
                Lysander arrives at another set of doors, this one has five doors.
                They look at the moving pictures featured on the doors and recognise them 
                as the five stages of grief: """)
                
        elif self.round_checker == 2:
                ("""
                1. Denial - depicting as a man aggressively shaking his head refusing to even look at Lysander
                2. Anger - depicting as a woman screaming towards Lysander
                3. Bargaining - depicting a person on their knees with their hands clasped praying for something 
                4. Depression - depicting a man with his back against a wall hunching over a picture frame
                5. Acceptance - depicting a woman standing at a gravestone, she smiling sadly
                """)            
                
                if choice2 != 4:
                    #wrong choice
                    print("""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)
                    attempt += 1 
                    
                elif choice2 == 4:
                    #correct choice and continues on
                    choices.append(choice2)
                    print("""
                        Lysander arrives in a circular room. The room had 7 doors when
                        you excluded the door Lysander had just entered from. Each door each had
                        just one word written on it.
                                1. Pride
                                2. Greed
                                3. Wrath
                                4. Envy
                                5. Lust
                                6. Gluttony
                                7. Sloth
                                       """) 
                    
                    choice3 = int(input("Choice: "))
                    
                    if choice3 != 6:
                        #wrong choice
                        print("""
                    Lysander is lead to a narrow corridor, filled with continous twists and turns
                    until they finally see a light at the end of the tunnel. They exit 
                    this hours long maze they've trekked through to see they have 
                    arrived at the same three statues.
                    """)
                        attempt += 1 
                    
                    elif choice3 == 6:
                        #correct choice and continues on 
                        choices.append(choice3)
    
    def challenge5(self):
        pass
    
    def challenge6_1(self):
        pass
    
    def challenge6_2(self):
        pass
    
    def challenge7(self):
        pass
    
    def challenge8(self):
        pass

CHALLENGE_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Challenge_Component\challenge.json"
CHALLENGE_CHAPTERS = {"Forest of Veymor" : "1.1",
                      "Meeting the Sable-Faced Guide" : "1.2",
                      "Riddle One" : "2", 
                      "Riddle Two" : "2", 
                      "Riddle Three" : "2",
                      "The Chamber of Choice" :  "3",
                      "Labors of the Cursed" : "5",
                      "Monsters Worn Like Memories" : "6.1", 
                      "Trial of the Deep Bend" : "6.2",
                      "The Final Stand" : "7", 
                      "Ascending in Confession" : "8"}
NUMBERS = ["1.1", "1.2", "2", "2", "2", "3", "5", "6.1", "6.2", "7", "8"]

turn = 1 

#chal = Challenge(CHALLENGE_FILE_PATH, turn)
#frame = chal.find_frame(NUMBERS[3])
#chal.show_frame(frame)
#chal.run()

#attempts = chal.get_attempts()
#print(attempts)

for i in range(3):
    chal = Challenge(CHALLENGE_FILE_PATH, turn)
    frame = chal.find_frame(NUMBERS[2])
    chal.show_frame(frame)
    chal.run()
    
    turn += 1 
    attempts = chal.get_attempts()
    print(attempts)    
