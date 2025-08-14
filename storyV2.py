'''this is the entire code for the story text file, in which it splits it 
by chapter and section, allowing challenges to be easily integreated into the 
story
13/8/2025
Pika Ranzinger 
Version One: All basic code for it to run 
Version Two: creating it's GUI'''

from tkinter import *
import tkinter.font as tkfont

class Story:
    '''the reading and separation of the story by sections '''
    
    def __init__(self, file_path, title, content, title_lists, sections):
        #identifying main variables 
        self.file_path = file_path
        self.title_lists = title_lists
        self.num = 2
        self.sections = sections 
        
        #window
        self.root = Tk()
        self.root.title("Storyline")
        self.root.configure(bg="#ffe6c9")        
        
        #fonts
        self.title_font = tkfont.Font(family="Lucida Handwriting", size=12)
        self.label_font = tkfont.Font(family="Century Gothic", size=10)
        self.button_font = tkfont.Font(family="Tahoma", size=12, weight="bold")                
        
        #sizing 
        self.root.resizable(0,0)
        self.root.geometry("700x550")        
        
        #container for frame
        self.container = Frame(self.root, width=700, height=550,
                               highlightthickness=5, bg="#ffe6c9",
                               highlightbackground="#ceb79b", 
                               highlightcolor="#ceb79b")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_propagate(False)
        
        #column and row configurations 
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)        
        
        #dictionary for frames
        self.frames = {}
        self.frames["StoryFrame"] = self.create_story_frame(title, content)
        
        # show the intial frame 
        self.show_frame("StoryFrame")
    
    def show_frame(self, name):
        '''display the required name from the dictionary'''
        frame = self.frames[name]
        frame.tkraise() # move frame to the top
        
    def run(self):
        '''run the GUI'''
        self.root.mainloop()
        
    def create_story_frame(self, chapter, section):
        '''creating the GUI for the chapters'''
        #frame
        frame = Frame(self.container, height=660, width=360, pady=20,padx=20, 
                      bg="#ffe6c9")
        frame.grid(row=0, column=0, sticky="nsew")
        
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)        
        frame.grid_propagate(False)
        
        #chapter title 
        title_label = Label(frame, text=f"{chapter}", font=self.title_font
                            ,bg="#ffe6c9")
        title_label.grid(row=0, column=0, columnspan=2, sticky="n")
        
        #section label 
        section_label = Label(frame, text=section, font=self.label_font, bg="#ffe6c9")
        section_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        #continue button
        cont_button = Button(frame, text = "Continue", height=3, width=30, font = self.button_font, 
                             relief=RIDGE, bg="#fff3e6", activebackground="#ceb79b",
                             command=lambda: self.next_chapter(title_label, section_label))
        cont_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        return frame
    
    def next_chapter(self, title, text):
        if self.num == len(self.title_lists) + 1:
            self.root.destroy()
        else:
            header = self.title_lists[self.num]
            message = self.sections[header]
            title.config(text= header)
            text.config(text=message)
            self.num += 1
    
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
    
file_path = r"N:\13PRG\st21121-Pika\Assessments\91906PikaRanzinger\Story_Component\story.txt"

sections = Story.chapters(file_path)
titles = {}
i = 1

for title, content in sections.items():
    if content != "":
        titles[i] = title
        i += 1

heading = titles[1]
text = sections[heading]
app = Story(file_path, heading, text, titles, sections)
app.run()