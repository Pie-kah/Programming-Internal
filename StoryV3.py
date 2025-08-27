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
        self.root.geometry("700x525")
        self.root.configure(bg="#ffe6c9")
        
        #frames 
        self.container = Frame(self.root, bg="#ffe6c9", highlightthickness=5,
                               width=700, height=525,
                               highlightbackground="#ceb79b", highlightcolor="#ceb79b")
        self.container.grid(row=0, column=0, sticky="nsew") 
        self.container.grid_propagate(False)
        
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
        pass    
            
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
            frame = Frame(self.container, bg="#ffe6c9", width=660, height=360)
            frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
            story_frame = Frame(frame, bg="#ffe6c9", width=620, height=200)
            story_frame.grid(row=1,column=0, sticky="nsew", pady=10, padx=10)

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
            text_label.grid(row=0, column=0, columnspan=2, pady=20)

            cont_button = Button(frame, text = "Continue", height = 3, width = 30, 
                     activebackground="#ceb79b", relief=RIDGE, font=self.BUTTON_FONT,
                     bg="#fff3e6", command=lambda: self.next_chapter(title_label, text_label))
            cont_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="s")

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

#file_path = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story.txt"

#sections = Story.chapters(file_path)
#titles = {}
#x = []
#i = 1
#num = 1
#challenge = ["wer", "weeww"]

#for title, content in sections.items():
    #if content != "":
        #titles[i] = title
        #sector = title.split(" - ")
        #x.append(sector[-1])
        #i += 1

#heading = titles[1]
#text = sections[heading]
#app = Story(file_path, heading, text, titles, sections, challenge, num)
#app.run()