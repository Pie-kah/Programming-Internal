'''
This is a leaderboard which shows the top 5 scorers of the game 
29.7.2025
Pika Ranzinger
V1: write all the code and test it before giving it a GUI
'''

import json 

class Leaderboard:
    '''leaderboard system showing top five scorers'''
    
    def __init__(self, username, score,):
        self.username = username
        self.score = int(score)
        
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

num = 1 
for key, value in top5.items():
    #print final leaderboard
    print(f" {num}. {key} : {value}")
    num = num + 1 

#dumping back to json file 
with open("leaderboard.json", "w") as f:
    json.dump(top5, f, indent = 2)'''