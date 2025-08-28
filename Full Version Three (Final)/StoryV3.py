'''this is the entire code for the story text file, in which it splits it 
by chapter and section, allowing challenges to be easily integreated into the 
story
13/8/2025
Pika Ranzinger 
Version One: All basic code for it to run 
Version Two: creating it's GUI
Version Three: adding validation to the files'''
from tkinter import *
import tkinter.font as tkfont


class Story:
    '''the reading and separation of the story by sections '''
    def __init__(self, file_path, title, content, title_lists, sections, challenge_list, num):
        self.file_path = file_path
        self.title_lists = title_lists
        self.num = int(num)
        self.sections = sections
        self.challenge_list = challenge_list
        self.help_button_image_file_path = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\help.png"
        self.story_help_image_file_path = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story_help.png"        
        self.alive = True
        
        #window
        self.root = Tk()
        self.root.title("Storyline") 
        
        #fonts
        self.TITLE_FONT = tkfont.Font(family = "Lucida Handwriting", size=12)
        self.LABEL_FONT = tkfont.Font(family = "Century Gothic", size=10) 
        self.BUTTON_FONT = tkfont.Font(family = "Tahoma", size=14, weight="bold")
        
        #preventing window closure
        self.root.protocol("WM_DELETE_WINDOW", self.exit)        
        
        #preventing resizing 
        self.root.resizable(0, 0) 
        self.root.geometry("700x605")
        self.root.configure(bg="#ffe6c9")
        
        #frames 
        self.container = Frame(self.root, bg="#ffe6c9", highlightthickness=5,
                               width=700, height=605,
                               highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        self.container.grid(row=0, column=0, sticky="nsew") 
        self.container.grid_propagate(False)
        
        #helper button 
        self.help_pic = PhotoImage(file=self.help_button_image_file_path)
        self.help_pic = self.help_pic.subsample(8)        
        help_button = Button(self.container, image=self.help_pic, width=30, height=30,
                             command=lambda: self.help_window())
        help_button.grid(row=0, column=1,padx=(0,10))        
        
        #keeping rows same and everything
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        #frames 
        self.frames = {}
        self.frames["MainFrame"] = self.create_chapter_frame(title, content)
        self.show_frame("MainFrame")
        
    def show_frame(self, name):
            '''display the required name from the dictionary'''
            frame = self.frames[name]
            frame.tkraise() # move frame to the top
            
    def exit(self):
        '''does nothing but it prevents window from closing'''
        self.alive = False
        self.root.destroy()
        pass
    
    def return_alive(self):
        '''returns the statis of window'''
        return self.alive
    
    def help_window(self):
        '''help window to explain the challenges for all the chapters'''
        #making a window and raising it 
        help_window = Toplevel(self.root)
        help_window.resizable(0,0)
        help_window.title("Help Window")    
        
        #the image
        self.help_window_pic = PhotoImage(file=self.story_help_image_file_path)
        help_image = Label(help_window, image=self.help_window_pic)
        help_image.grid(row=0, column=0)     
            
    def next_chapter(self, title, text): 
        '''moving onto the next chapter'''
        self.num += 1
            
        if self.num > 46:
            self.root.destroy()
            
        else: 
            header = self.title_lists[self.num]
            message = self.sections[header]
                
            for name in self.challenge_list:
                if name in header:
                    self.root.destroy()
                    return
            title.config(text=f"{header}")
            text.config(text=message)
                
    def return_num(self):
            return self.num
        
    def create_chapter_frame(self, chapter, section):
            '''creating GUI for the showing of the chapters'''
            frame = Frame(self.container, bg="#ffe6c9", width=660, height=525)
            frame.grid(row=1, column=0, sticky="nsew", pady=(0,20), padx=20)
            story_frame = Frame(frame, bg="#ffe6c9", width=620, height=400)
            story_frame.grid(row=2,column=0, sticky="nsew", pady=10, padx=10)

            frame.grid_rowconfigure(1, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            story_frame.grid_rowconfigure(0, weight=1)
            story_frame.grid_columnconfigure(0, weight=1)

            frame.grid_propagate(False)
            story_frame.grid_propagate(False) 

            title_label = Label(frame, text = f"{chapter}",
                                font = self.TITLE_FONT, bg="#ffe6c9")
            title_label.grid(row=0, column=0, columnspan=2)

            text_label = Label(story_frame, text = section, font = self.LABEL_FONT, 
                   bg="#ffe6c9", justify="center", wraplength=600)
            text_label.grid(row=0, column=0, columnspan=2, sticky="n")

            cont_button = Button(frame, text = "Continue", height = 3, width = 30, 
                     activebackground="#ceb79b", relief=RIDGE, font=self.BUTTON_FONT,
                     bg="#fff3e6", command=lambda: self.next_chapter(title_label, text_label))
            cont_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="s")

            return frame

    def run(self):
            self.root.mainloop()
            
    def chapters(file_path):
            #separating story by sections 
            sections = {}
            current_chapter = None
            current_title = None
            current_content = []
            
            with open(file_path, "r", encoding='utf-8') as book:
                for line in book:
                    #split the lines 
                    line = line.strip()
                    
                    if line.lower().startswith("chapter"):
                        #find and save chapter titles 
                        current_chapter = line 
                    
                    elif line.startswith("~") and line.endswith("~"):
                        if current_title:
                            full_title = f"{current_chapter} - {current_title}" if current_chapter else current_title
                            sections[full_title] = '\n'.join(current_content).strip()
                    
                        current_title = line.strip('~')
                        current_content = []
                    
                    else:
                        if current_title is not None:
                            #appending content
                            current_content.append(line)
                
                #saving last section
                if current_title is not None:
                    #check if current chapter has a saved name  
                    full_title = f"{current_chapter} - {current_title}"
                else:
                    #if no current chapter saved just have section title
                    full_title = current_title
                
                #adding everything to dictionary
                sections[full_title] = "\n".join(current_content).strip()
            
            return sections 

def validate_file(file):
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
    
def error_message(name):
    '''error message that pops up if it's not there'''
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
        
    error_message_label = Label(error_window, text=f"""File ({name}) has not been found
    or is empty.""",
                                font="Arial 10", justify="center",bg="#ffe6c9")
    error_message_label.grid(row=1, column=0, padx=50, pady=20)
    error_window.mainloop()

###MAIN PROGRAM###
'''#file path
files = {"STORY_FILE": r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story.txt"}


#validating file 
entry = validate_file(files["STORY_FILE"])

if entry is True:
    #variables 
    file_path = files["STORY_FILE"]
    titles = {}
    x = []
    i = 1
    num = 1
    challenge = ["wer", "weeww"]
    
    #getting sections
    sections = Story.chapters(file_path)
    
    #getting the title, headers and sectors 
    for title, content in sections.items():
        if content != "":
            #ignoring it if content if blank
            titles[i] = title
            sector = title.split(" - ")
            x.append(sector[-1])
            i += 1
    
    #GUI
    heading = titles[1]
    text = sections[heading]
    app = Story(file_path, heading, text, titles, sections, challenge, num)
    app.run()
else:
    for key in files.keys():
        error_message(key)    '''