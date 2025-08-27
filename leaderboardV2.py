'''
This is a leaderboard which shows the top 5 scorers of the game 
13.8.2025
Pika Ranzinger
V1: write all the code and test it before giving it a GUI
V2 : make the entire GUI
'''

from tkinter import *
import tkinter.font as tkfont
import json 

class Leaderboard:
    '''leaderboard system showing top five scorers'''
    
    def __init__(self, username, score, top5):
        '''setting up main GUI/root, and main variables'''
        #variables
        self.username = username
        self.score = int(score)
        self.top5 = top5
        
        #window
        self.root = Tk()
        self.root.title("Leaderboard")
        
        #fonts
        self.title_font = tkfont.Font(family="Lucida Handwriting", size=18)
        self.label_font = tkfont.Font(family="Century Gothic", size=14)
        self.user_label_font = tkfont.Font(family="Century Gothic", size=14, weight="bold")
        self.button_font = tkfont.Font(family="Tahoma", size=16, weight="bold")
        
        #sizeing and removing ability to resize
        self.root.resizable(0,0)
        self.root.configure(bg="#ffe6c9")
        
        #containter for the frame for window
        self.container = Frame(self.root, bg="#ffe6c9")
        self.container.grid(row=0, column=0, sticky="nsew")
        
        #dictionary for all the frames 
        self.frames = {}
        self.frames["LeaderboardFrame"] = self.create_leaderboard_frame()
        
        #showing first frame
        self.show_frame("LeaderboardFrame")
        
    def create_leaderboard_frame(self):
        '''creating GUI for the leaderboard'''
        #setting up frame
        border_frame = Frame(self.container, highlightthickness=5, bg="#ffe6c9",
                             highlightbackground="#ceb79b", highlightcolor="#ceb79b",)
        border_frame.grid(row=0, column=0, sticky="nsew")
        frame = Frame(border_frame, bg="#ffe6c9")
        frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
        
        #variable
        num = 1
        
        #title label
        title_label = Label(frame, text = f" ~~ Leaderboard ~~ ", font = self.title_font,
                            bg="#ffe6c9", justify="center")
        title_label.grid(row = 0, column = 0, columnspan = 3, pady=15)
        
        for user, score in self.top5.items():
            #show top 5 scorers via for loop
            text_label = Label(frame, text = f"{num}. {user} : {score}", 
                               font = self.label_font, justify="left", bg="#ffe6c9")
            text_label.grid(row = num, column = 1, pady=5)
            num += 1
        
        #users own score lable
        user_label = Label(frame, text = f"{self.username} : {self.score}",
                           font = self.user_label_font, bg="#ffe6c9",justify="left")
        user_label.grid(row = 6, column = 1, pady=10)
        
        #a quit button
        quit_button = Button(frame, text = "Quit", font = self.button_font, 
                             height=1, width=15, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                             command=self.quit)
        quit_button.grid(row=7, column=1, pady=10)
        
        return frame 
        
    def placement(leaderboard):
        '''sorting the scores from least to most'''
        usernames = []
        scores = []

        for key, value in leaderboard.items():
            #appending usernames and scores to separate list
            usernames.append(key)
            scores.append(value)
        
        for i in range(len(usernames)):
            for j in range(i):
                #sorting algorithm
                if scores[j] > scores[i]:
                    num = scores[j]
                    scores[j] = scores[i]
                    scores[i] = num
                    name = usernames[j]
                    usernames[j] = usernames[i]
                    usernames[i] = name 
        
        #deleting all but the top 5
        del usernames[5:]
        del scores[5:]
        
        #making the top five into a dictionary 
        final_list = {}
        for c in range(len(usernames)):
            final_list[usernames[c]] = scores[c]
        
        #returning top five dict
        return final_list
    
    def run(self):
        '''Run GUI'''
        self.root.mainloop()
        
    def quit(self):
        '''destroying the window'''
        self.root.destroy()
        
    def show_frame(self, name):
        '''display the required name from the dictionary'''
        frame = self.frames[name]
        frame.tkraise()
    
'''
###Main Program###
#opening the json file
with open("leaderboard.json") as file:
    leaderboard = json.load(file)

#allow user input to enter new names 
user = input("Enter username: ")
total = int(input("Enter score: "))

#adding new names+scores and sorting them
leaderboard[user] = total 
top5 = Leaderboard.placement(leaderboard)

#dumping back to json file 
with open("leaderboard.json", "w") as f:
    json.dump(top5, f, indent = 2)

if __name__ == "__main__":
    app = Leaderboard(user, total)
    app.run()'''