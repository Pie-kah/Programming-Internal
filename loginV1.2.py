'''
A story based game, to continue in the story you must complete various challenges
V1: Write all the barebone code for the different windows 
'''

import json

class Login:
    '''Setting up the login/register system'''

    def __init__(self, username, password):
        #setting up values within class
        self.username = username 
        self.password = password

    def login(self):
        #logging in 
        with open("login.json") as file:
            #opening username and password file
            user = json.load(file)
        
        for key, value in user.items():
            #checking if the username and password is the same on file 
            if key == self.username:
                if value == self.password:
                    return True
        else:
            return False

    def register(self):
        #registering and adding to file 
        with open("login.json") as file:
            #opening username and password file
            user = json.load(file)

        for key, value in user.items():
            while key == self.username:
                #checking that there is not an identical username in use
                print("Username already in use")
                self.username = input("Enter another username: ")
                self.password = input("Enter password: ")
        
        #adding it to the dictionary
        user[self.username] = self.password

        with open("login.json", "w") as f:
            #adding it to file 
            json.dump(user, f, indent = 2)

        return True

### Testing Program ###

   
menu = input("""
1. Login
2. Register
Choice: """)

if menu == '1':
    #login system
    entry = False
    while entry == False:
        #not allowing user to exit until valid username and password entered
        username = input("Enter username: ")
        password = input("Enter password: ")
        entry = Login(username, password)
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
        entry = Login(username, password)
        Login.register(entry)
        if entry == False:
            print("username already in use")
    print("Valid username and password")