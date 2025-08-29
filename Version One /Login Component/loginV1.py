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
            user = json.load(file)
        
        for key, value in user:
            if key == self.username:
                if value == self.password:
                    return True
        else:
            return False

    def register(self):
        #registering and adding to file 
        with open("login.json") as file:
            user = json.load(file)

        for key, value in user:
            while key.lower() == self.username.lower():
                print("Username already in use")
                self.username = input("Enter another username: ")
                self.password = input("Enter password: ")
            new_user = {

            }
            new_user[self.username] = self.password

        with open("login.json", "a") as f:
            json.dump(new_user, f)

        return True

menu = input("""
1. Login
2. Register
Choice: """)

if menu == '1':
    entry = False
    while entry == False:
        username = input("Enter username: ")
        password = input("Enter password: ")
        entry = Login(username, password)
        Login.login(entry)
        print("Incorrect username or password")
    print("Correct")


if menu == '2':
    entry = False
    username = input("Enter username: ")
    password = input("Enter password: ")
    while entry == False:
        entry = Login.register(username, password)
        print("username already in use")
    print("Valid username and password")



