'''
This is a login or register system. 
24.7.2025
Pika Ranzinger
V1: writing all code and testing required for it 
'''

import json

class Login:
    '''Setting up the login/register system'''

    def __init__(self, username, password, file_path):
        #setting up values within class
        self.username = username 
        self.password = password
        self.file_path = file_path
        
        

    def login(self, file_path):
        #logging in 
        with open(file_path) as file:
            #opening username and password file
            user = json.load(file)
        
        for key, value in user.items():
            #checking if the username and password is the same on file 
            if key == self.username:
                if value == self.password:
                    return True
        else:
            return False

    def register(self, file_path):
        #registering and adding to file 
        with open(file_path) as file:
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
        username = self.username
        password = self.password

        with open("login.json", "w") as f:
            #adding it to file 
            json.dump(user, f, indent = 2)

        return True and username and password
