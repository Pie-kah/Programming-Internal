'''This is the main program, so I interlink all of the components together into
one big program
7/8/2025
Pika Ranzinger 
Version One: coding everything to make sure it all can function together'''

import json
import random
import time 
from Challenge_Component.challengeV1 import Challenge as chal
from Login_Component.loginV1_2 import Login
from Story_Component.storyV1_2 import Story 
from Leaderboard_Component.leaderboardV1 import Leaderboard

CHALLENGE_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Challenge_Component\challenge.json"
STORY_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story.txt"
LOGIN_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Login_Component\login.json"
LEADERBOARD_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Leaderboard_Component\leaderboard.json"

CHALLENGE_CHAPTERS = {"Forest of Veymor" : chal.ch1_1_challenge,
                      "Meeting the Sable-Faced Guide" : chal.ch1_2_challenge,
                      "Riddle One" : chal.ch2_challenge, 
                      "Riddle Two" : chal.ch2_challenge, 
                      "Riddle Three" : chal.ch2_challenge,
                      "The Chamber of Choice" :  chal.ch3_challenge,
                      "Labors of the Cursed" : chal.ch5_challenge,
                      "Monsters Worn Like Memories" : chal.ch6_1_challenge, 
                      "Trial of the Deep Bend" : chal.ch6_2_challenge,
                      "The Final Stand" : chal.ch7_challenge, 
                      "Ascending in Confession" : chal.ch8_challenge}

### Main Program ###
total_attempts = 0 
turn = 1

menu = input("""
1. Login
2. Register

Choice: """)
print("")

if menu == '1':
    #login system
    entry = False
    while entry == False:
        #not allowing user to exit until valid username and password entered
        username = input("Enter username: ")
        password = input("Enter password: ")
        entry = Login(username, password, LOGIN_FILE_PATH)
        Login.login(entry)
        if entry == False:
            print("Incorrect username or password")
    print("Correct")


if menu == '2':
    #register system 
    entry = False
    username = input("Enter username: ")
    password = input("Enter password: ")
    while entry == False:
        #not allowing user to exit until valid username and password entered 
        entry = Login(username, password, LOGIN_FILE_PATH)
        Login.register(entry)
        if entry == False:
            print("username already in use")
    print("Valid username and password")

#get sections
story = Story.chapters(STORY_FILE_PATH)

#continue num
cont = "1"

for title, content in story.items():
    if len(content) == 0:
        pass
    else:
        if cont == "1":
            if "riddle" in title.lower():
                section_attempts = chal.ch2_challenge(CHALLENGE_FILE_PATH, turn)
                total_attempts += section_attempts  
                turn += 1 
            else:
                print(f""" 
                === {title} ===
                
                {content}
                
                """)
                for key, value in CHALLENGE_CHAPTERS.items():
                    if key in title:
                        section_attempts = value(CHALLENGE_FILE_PATH)
                        total_attempts += section_attempts
                    
            cont = "0"
        cont = input("Press 1 to continue: ")
        
        
#opening the json file
with open(LEADERBOARD_FILE_PATH) as file:
    leaderboard = json.load(file)
        
#allow user input to enter new names 
user = username
total = total_attempts
        
#adding new names+scores and sorting them
leaderboard[user] = total 
top5 = Leaderboard.placement(leaderboard)
        
num = 1 
for key, value in top5.items():
    #print final leaderboard
    print(f" {num}. {key} : {value}")
    num = num + 1 
        
#dumping back to json file 
with open(LEADERBOARD_FILE_PATH, "w") as f:
    json.dump(top5, f, indent = 2)
