'''This is the main program, so I interlink all of the components together into
one big program
7/8/2025
Pika Ranzinger 
Version One: coding everything to make sure it all can function together
Version Two: Putting the GUI of all the other components together
Version Three: Adding the validation '''

#imports
import json
import random
import time 
from tkinter import *
from Challenge_Component.ChallengeV3 import Challenge
from Login_Component.LoginV3 import Login
from Story_Component.StoryV3 import Story 
from Leaderboard_Component.LeaderboardV3 import Leaderboard

def validate_file(file,name):
    if name == "STORY_FILE":
        '''checking that the file exists'''
        try:
            #trying to open the file 
            with open(file, "r", encoding='utf-8') as book:
                #if able to load content return True 
                content = book.read()
                if len(content.strip()) != 1:
                    return True
                else:
                    return False 
        except FileNotFoundError:
            #else return False 
            return False
    else:
        try:
            #trying to open the file 
            with open(file, "r") as f:
                #if able to load content return True 
                content = json.load(f)
                return True
        except FileNotFoundError:
            #else return False 
            return False
        
def error_message(name):
    '''error pop up if the file isn't there'''
    #window
    error_window = Tk()
    error_window.title("Error Message")
    error_window.geometry("325x150")
    error_window.resizable(0,0)
    error_window.configure(bg="#ffe6c9")
    
    #title and label
    error_message_title = Label(error_window, text="Error Message", bg="#ffe6c9",
                                        font="Arial 15 bold", justify="center")
    error_message_title.grid(row=0, column=0, padx=50, pady=20)
            
    error_message_label = Label(error_window, text=f"File ({name}) has not been found",
                                        font="Arial 10", justify="center",bg="#ffe6c9")
    error_message_label.grid(row=1, column=0, padx=25, pady=20)
    error_window.mainloop()

#file paths
files = {"CHALLENGE_FILE": r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Challenge_Component\challenge.json",
         "LEADERBOARD_FILE": r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Leaderboard_Component\leaderboard.json",
         "LOGIN_FILE": r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Login_Component\login.json",
         "STORY_FILE": r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story.txt"}
    

#dictionary placements of all the challenges
CHALLENGE_CHAPTERS = {"Forest of Veymor" : "1.1",
                      "Meeting the Sable-Faced Guide" : "1.2",
                      "Riddle One: The Hollow Recipe" : "2", 
                      "Riddle Two: The Invisible Clock" : "2", 
                      "Riddle Three: A Feather’s Burden" : "2",
                      "The Chamber of Choice" :  "3",
                      "Labors of the Cursed" : "5",
                      "Monsters Worn Like Memories" : "6.1", 
                      "Trial of the Deep Bend" : "6.2",
                      "The Final Stand" : "7", 
                      "Ascending" : "8"}

### Main Program ###
#making a title list
key_list = []
for key, value in CHALLENGE_CHAPTERS.items():
    key_list.append(key)
    
#variables 
total_attempts = 0 
turn = 1
num = 1
checker = 0
all_validation = False
alive = True

#file validation
for key,value in files.items():
    entry = validate_file(value, key)
    if entry is True:
        checker += 1
    elif entry is False:
        error_message(key)

if checker == 4:
    all_validated = True

if all_validated is True:
    #variables 
    STORY_FILE_PATH = files["STORY_FILE"]
    CHALLENGE_FILE_PATH = files["CHALLENGE_FILE"]
    
    while alive is True:
        #login or register window 
        if __name__ == "__main__":
            login_app = Login(files["LOGIN_FILE"])
            login_app.run()
            user = login_app.return_username()
            
            #checking it's alive
            alive = login_app.return_alive()
                
            if alive is False:
                break                  

        #checking it's alive
        alive = login_app.return_alive()
                
        if alive is False:
            break                  
                
        #get sections and story viarables 
        sections = Story.chapters(STORY_FILE_PATH)
        titles = {}
        title_sect = []
        i = 1
        
        for title, content in sections.items():
            if content != "":
                titles[i] = title
                sector = title.split(" - ")
                title_sect.append(sector[-1])
                i += 1
        
        #challenges and chapters 
        heading = titles[num]
        text = sections[heading]
        story_app = Story(STORY_FILE_PATH, heading, text, titles, sections, CHALLENGE_CHAPTERS, num)
        story_app.run()
        
        #checking it's alive
        alive = story_app.return_alive()
        
        if alive is False:
            break                     
        
        while num < len(title_sect):
            num = story_app.return_num()
            if "Riddle" in title_sect[num-1]:
                #if its the riddles 
                for i in range(3):
                    chal = Challenge(CHALLENGE_FILE_PATH, turn)
                    print(title_sect[num-1])
                    frame = chal.find_frame(CHALLENGE_CHAPTERS[title_sect[num-1]])
                    chal.show_frame(frame)
                    chal.run()
                    
                    #checking it's alive 
                    alive = chal.return_alive()
                    
                    if alive is False:
                        break 
                    
                    turn += 1 
                    attempts = chal.get_attempts()
                    total_attempts += attempts   
                    
                    #then show the section as intended 
                    heading = titles[num]
                    text = sections[heading]
                    story_app = Story(STORY_FILE_PATH, heading, text, titles, sections, CHALLENGE_CHAPTERS, num)
                    story_app.run()
                    num = story_app.return_num()
                    
                    #checking it's alive
                    alive = story_app.return_alive()
                    
                    if alive is False:
                        break                                                  
                    
            for key, value in CHALLENGE_CHAPTERS.items():
                if key in title_sect[num-1]:
                    #if the key is in other challenges
                    #display challenge
                    chal = Challenge(CHALLENGE_FILE_PATH, turn)
                    frame = chal.find_frame(CHALLENGE_CHAPTERS[title_sect[num-1]])
                    chal.show_frame(frame)
                    chal.run()  
                    
                    #checking its alive 
                    alive = chal.return_alive()
                    
                    if alive is False:
                        break                     
                    
                    #calc total attempts 
                    ch_attempts = chal.get_attempts()
                    total_attempts += ch_attempts 
            
            #checking it's alive
            alive = chal.return_alive()
            
            if alive is False:
                break             
            
            #show the story after challenge   
            heading = titles[num]
            text = sections[heading]
            story_app = Story(STORY_FILE_PATH, heading, text, titles, sections,CHALLENGE_CHAPTERS, num)
            story_app.run()
            num = story_app.return_num()
            
            #checking it's alive
            alive = story_app.return_alive()
            
            if alive is False:
                break             
         
        #checking it's alive
        alive = chal.return_alive()
            
        if alive is False:
            break        
        
        #checking it's alive
        alive = story_app.return_alive()
        
        if alive is False:
            break          
                
        #opening the json file
        with open(files["LEADERBOARD_FILE"]) as file:
            leaderboard = json.load(file)
                
        #allow user input to enter new names 
        total = total_attempts + 25
                
        #adding new names+scores and sorting them
        leaderboard[user] = total 
        top5 = Leaderboard.placement(leaderboard)
                
        #dumping back to json file 
        with open(files["LEADERBOARD_FILE"], "w") as f:
            json.dump(top5, f, indent = 2)
        
        #running GUI
        leaderboard_app = Leaderboard(user, total, top5)
        leaderboard_app.run()
        
        #checking it's alive
        alive = leaderboard_app.return_alive()
        
        if alive is False:
            break             