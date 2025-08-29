class Story:
    '''the reading and separation of the story by sections '''
    
    def __init__():
        pass
    
    def chapters():
        #separating story by sections 
        sections = {}
        current_chapter = None
        current_title = None 
        current_content = []
        
        with open("story.txt", "r", encoding='utf-8') as book:
            for line in book:
                #split the lines 
                line = line.strip()
                
                if line.lower().startswith("chapter"):
                    #find and save chapter titles 
                    current_chapter = line 
                    
                elif line.startswith("~") and line.endswith("~"):
                    #find and save the section title
                    if current_chapter is not None:
                        #check if current chapter has a saved name 
                        current_title = line 
                        full_title = f"{current_chapter} - {current_title}"
                    else:
                        #if no current chapter saved just have section title
                        full_title = current_title
                    
                    #adding everything to dictionary
                    sections[full_title] = "\n".join(current_content).strip()
                    
                    #reseting it
                    current_title = line.strip("~")
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

###Main Program        

#get sections
story = Story.chapters()

#continue num
cont = "1"

for title, content in story.items():
    if len(content) == 0:
        pass
    else:
        if cont == "1":
            print(f""" 
            === {title} ===
            
            {content}
            
            """)
            cont = "0"
        cont = input("Press 1 to continue: ")
