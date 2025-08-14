'''This is have all the challenges that I will have during the game 
30/7/2025
Pika Ranzinger 
Version one: Write all the code
Version Two: Create the GUI'''
import time 
import random
import json 
from tkinter import *


class Challenge:
    
    def __init__(self, file_path, turn):
        self.file_path = file_path
        self.turn = 0
        
        self.root = Tk()
        self.root.title("Challenge Window")
        
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        title_label = Label(self.root, text = "Challenge", font = "Arial 25")
        title_label.grid(row=0, column=0, pady=20, padx=20)
        
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
    
    def find_frame(self, num, chapters):
        for title, chal_num in CHALLENGE_CHAPTERS.items():
            frame_name = f"Challenge{num}"
            if "riddle" in title.lower():
                frame = frame_name
                self.turn += 1 
            elif num == chal_num:
                frame = frame_name
        
        return frame 
        
    def create_challenge1_1(self):
        frame = Frame(self.container, bg="#ffe6c9")
        frame.grid(row=1, column=0, sticky="nsew")
        text_label = Label(frame, text="Challenge One")
        text_label.grid(row=2, column=0)
        
        return frame
    
    def create_challenge1_2(self):
        frame = Frame(self.container, bg="#ffe6c9")
        frame.grid(row=1, column=0, sticky="nsew")
        text_label = Label(frame, text="Challenge Two")
        text_label.grid(row=2, column=0)
        
        return frame 
    
    def create_challenge2(self):
        pass
    
    def create_challenge3(self):
        pass
    
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

chal = Challenge(CHALLENGE_FILE_PATH, turn)
for num in NUMBERS:
    frame = chal.find_frame(num, CHALLENGE_CHAPTERS)
    chal.run()
    chal.show_frame(frame)