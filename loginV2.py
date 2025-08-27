'''
This is a login or register system. 
8.8.2025
Pika Ranzinger
V1: writing all code and testing required for it 
V2: making it's GUI
'''
from tkinter import *
import tkinter.font as tkfont
import json

class Login:
    '''Setting up the login/register system'''

    def __init__(self, file_path):
        #setting up values within class
        self.file_path = file_path
        self.image_file_path = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Login_Component\mainmenupic.png"
        self.username = ""
        
        # main window
        self.root = Tk()
        self.root.title("Login and Register System")
        
        #fonts
        self.title_font = tkfont.Font(family="Lucida Handwriting", size=18)
        self.label_font = tkfont.Font(family="Century Gothic", size=14)
        self.user_label_font = tkfont.Font(family="Century Gothic", size=14, weight="bold")
        self.button_font = tkfont.Font(family="Tahoma", size=16, weight="bold")        
        
        #sizing and unabling resizability
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.configure(bg="#ffe6c9")
        
        # container for frames 
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # dictionary to hold frames
        self.frames = {}
        
        self.frames["MainMenu"] = self.create_main_frame()
        self.frames["LoginFrame"] = self.create_login_frame()
        self.frames["RegisterFrame"] = self.create_register_frame()
        
        # show the intial frame 
        self.show_frame("MainMenu")
    
    def show_frame(self, name):
        '''display the required name from the dictionary'''
        frame = self.frames[name]
        frame.tkraise() # move frame to the top
        
    def run(self):
        '''run the GUI'''
        self.root.mainloop()
        
    def clear_all(self, label):
        '''clears the label when button clicked, like for the error message'''
        label.config(text="")
    
    def return_username(self):
        return self.username     
    
    def create_main_frame(self):
        '''create home screen of app'''
        frame = Frame(self.container, bg="#ffe6c9")
        frame.grid(row=0, column=0, sticky="nsew")
        
        # main heading 
        self.label_title = Label(frame, text = "~~ The Feather and the Flame ~~", 
                            font=self.title_font, bg="#ffe6c9")
        self.label_title.grid(row=0, columnspan=2, padx=10, pady=10)
        
        #image
        self.mainpic = PhotoImage(file=self.image_file_path)
        self.mainpic = self.mainpic.subsample(4)
        self.image = Label(frame, image=self.mainpic, bg="#ffe6c9")
        self.image.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
        
        # buttons: to Login or Register
        self.login_button = Button(frame, text="Login", font = self.button_font, 
                             height=2, width=10, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                                  command=lambda: self.show_frame("LoginFrame"))
        self.login_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.register_button = Button(frame, text="Register", font = self.button_font, 
                             height=2, width=10, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                                  command=lambda: self.show_frame("RegisterFrame"))
        self.register_button.grid(row=2, column=1, padx=10, pady=10)
        
        return frame     
    
    def create_login_frame(self):
        '''create login frame for the system'''
        frame = Frame(self.container, bg="#ffe6c9")
        frame.grid(row=0, column=0, sticky="nsew")
        
        # main heading 
        self.label_title = Label(frame, text = "~~ Login ~~", 
                            font=self.title_font, bg="#ffe6c9")
        self.label_title.grid(row=0, columnspan=2, padx=10, pady=10)
        
        #username label and entry
        login_username_label = Label(frame, text="Username:",
                                     font=self.user_label_font, bg="#ffe6c9")
        login_username_label.grid(row=1, column=0, padx=10, pady=10)
        login_username_entry = Entry(frame, font=self.label_font, bg="#ffe6c9")
        login_username_entry.grid(row=1, column=1, padx=10, pady=10)
        
        #password label and entry
        login_password_label = Label(frame, text="Password:",
                                     font=self.user_label_font, bg="#ffe6c9")
        login_password_label.grid(row=2, column=0, padx=10, pady=10)
        login_password_entry = Entry(frame, font=self.label_font, bg="#ffe6c9")
        login_password_entry.grid(row=2, column=1, padx=10, pady=10)
        
        #error message label
        error_message_label = Label(frame, text="", bg="#ffe6c9")      
        error_message_label.grid(row=3, column=0, columnspan=2)
        
        # buttons: to Login or Main Menu
        login_button = Button(frame, text="Login",font = self.button_font, 
                             height=1, width=15, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                                  command=lambda: self.login(error_message_label,
                                                             login_username_entry,
                                                             login_password_entry))
        login_button.grid(row=4, column=1, padx=10, pady=10)
        
        home_button = Button(frame, text="Return to Home",font = self.button_font, 
                             height=1, width=15, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                                  command=lambda: [self.clear_all(error_message_label),
                                                   self.show_frame("MainMenu")])
        home_button.grid(row=4, column=0, padx=10, pady=10)
        
        return frame 
    
    def create_register_frame(self):
        '''create register frame for the system'''
        frame = Frame(self.container, bg="#ffe6c9")
        frame.grid(row=0, column=0, sticky="nsew")
        
        # main heading 
        self.label_title = Label(frame, text = "~~ Register ~~", 
                            font=self.title_font, bg="#ffe6c9")
        self.label_title.grid(row=0, columnspan=2, padx=10, pady=10)
        
        #username label and entry
        register_username_label = Label(frame, text="Username:",
                                     font=self.user_label_font, bg="#ffe6c9")
        register_username_label.grid(row=1, column=0, padx=10, pady=10)
        register_username_entry = Entry(frame, font=self.label_font, bg="#ffe6c9")
        register_username_entry.grid(row=1, column=1, padx=10, pady=10)
        
        #password label and entry
        register_password_label = Label(frame, text="Password:",
                                     font=self.user_label_font, bg="#ffe6c9")
        register_password_label.grid(row=2, column=0, padx=10, pady=10)
        register_password_entry = Entry(frame, font=self.label_font, bg="#ffe6c9")
        register_password_entry.grid(row=2, column=1, padx=10, pady=10)      
        
        #error message label
        error_message_label = Label(frame, text="", bg="#ffe6c9")
        error_message_label.grid(row=3, column=0, columnspan=2)
        
        # buttons: to Login or Main Menu
        register_button = Button(frame, text="Register",font = self.button_font, 
                             height=1, width=15, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                                  command=lambda: self.register(error_message_label, 
                                                                register_username_entry,
                                                             register_password_entry))
        register_button.grid(row=4, column=1, padx=10, pady=10)
        
        home_button = Button(frame, text="Return to Home",font = self.button_font, 
                             height=1, width=15, relief=RIDGE, bg="#fff3e6",
                             activebackground="#ceb79b",
                                  command=lambda: [self.clear_all(error_message_label),
                                                   self.show_frame("MainMenu")])
        home_button.grid(row=4, column=0, padx=10, pady=10)
        
        return frame 

    def login(self, error_message, username_text, password_text):
        '''the username and password checking system for login'''
        correct = 0
        
        username = username_text.get()
        password = password_text.get()
        
        
        with open(self.file_path) as file:
            #opening username and password file
            user = json.load(file)
        
        for key, value in user.items():
            #checking if the username and password is the same on file 
            if key == username and value == password:
                    error_message.config(text="Correct username or password")
                    correct = 1
                    
                    #adding username to class and closing window 
                    self.username = username 
                    self.root.after(1500, self.root.destroy)
                    
        if correct == 0:
            error_message.config(text="Incorrect username or password")
        
        username_text.delete(0, END)
        password_text.delete(0, END)

    def register(self, error_message, username_text, password_text ):
        '''registering and adding to file '''
        error = 0
        
        username = username_text.get()
        password = password_text.get()
        
        with open(self.file_path) as file:
            #opening username and password file
            user = json.load(file)

        for key, value in user.items():
            if key == username:
                #checking that there is not an identical username in use
                error_message.config(text="Invalid Username")
                error = 1
        
        #adding it to the dictionary
        if error == 0:
            error_message.config(text="Valid Username")
            user[username] = password
            username = username
            password = password
    
            with open(self.file_path, "w") as f:
                #adding it to file 
                json.dump(user, f, indent = 2)
                
                #username to class and closing window 
                self.username = username 
                self.root.after(1500, self.root.destroy)
        
        username_text.delete(0, END)
        password_text.delete(0, END)        
'''
LOGIN_FILE_PATH = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Login_Component\login.json"

if __name__ == "__main__":
    app = Login(LOGIN_FILE_PATH)
    app.run()'''