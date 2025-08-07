'''this is the entire code for the story text file, in which it splits it 
by chapter and section, allowing challenges to be easily integreated into the 
story
3/8/2025
Pika Ranzinger 
Version One: All basic code for it to run '''

class Story:
    '''the reading and separation of the story by sections '''
    
    def __init__(file_path):
        self.file_path = file_path
    
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