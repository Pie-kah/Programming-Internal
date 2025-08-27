'''This is the main program, so I interlink all of the components together into
one big program
7/8/2025
Pika Ranzinger 
Version One: coding everything to make sure it all can function together
Version Two: Putting the GUI of all the other components together'''

#imports
import json
import random
import time 
from Challenge_Component.ChallengeV2_2 import Challenge
from Login_Component.loginV2 import Login
from Story_Component.storyV2 import Story 
from Leaderboard_Component.leaderboardV2 import Leaderboard

#file paths
CHALLENGE_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Challenge_Component\challenge.json"
STORY_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story.txt"
LOGIN_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Login_Component\login.json"
LEADERBOARD_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Leaderboard_Component\leaderboard.json"

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

#login or register window 
if __name__ == "__main__":
    login_app = Login(LOGIN_FILE_PATH)
    login_app.run()
    user = login_app.return_username()

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
'''
#challenges and chapters 
heading = titles[num]
text = sections[heading]
story_app = Story(STORY_FILE_PATH, heading, text, titles, sections, CHALLENGE_CHAPTERS, num)
story_app.run()

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
            
            turn += 1 
            attempts = chal.get_attempts()
            total_attempts += attempts   
            
            #then show the section as intended 
            heading = titles[num]
            text = sections[heading]
            story_app = Story(STORY_FILE_PATH, heading, text, titles, sections, CHALLENGE_CHAPTERS, num)
            story_app.run()
            num = story_app.return_num()
            
    for key, value in CHALLENGE_CHAPTERS.items():
        if key in title_sect[num-1]:
            #if the key is in other challenges
            #display challenge
            chal = Challenge(CHALLENGE_FILE_PATH, turn)
            frame = chal.find_frame(CHALLENGE_CHAPTERS[title_sect[num-1]])
            chal.show_frame(frame)
            chal.run()      
            
            #calc total attempts 
            ch_attempts = chal.get_attempts()
            total_attempts += ch_attempts 
    
    #show the story after challenge   
    heading = titles[num]
    text = sections[heading]
    story_app = Story(STORY_FILE_PATH, heading, text, titles, sections,CHALLENGE_CHAPTERS, num)
    story_app.run()
    num = story_app.return_num() '''
        
        
#opening the json file
with open(LEADERBOARD_FILE_PATH) as file:
    leaderboard = json.load(file)
        
#allow user input to enter new names 
total = total_attempts + 25
        
#adding new names+scores and sorting them
leaderboard[user] = total 
top5 = Leaderboard.placement(leaderboard)
        
#dumping back to json file 
with open(LEADERBOARD_FILE_PATH, "w") as f:
    json.dump(top5, f, indent = 2)

#running GUI
leaderboard_app = Leaderboard(user, total, top5)
leaderboard_app.run()