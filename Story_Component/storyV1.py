'''Version One of the story code
29.7.2025
Pika Ranzinger
V1: Complete all code required for the story to work'''

import json 

class Story:
        
    def story_present(self):
        pass

with open("story.json") as book:
    chapters = json.load(book)
    
for chapter,paragraph in chapters.items():
    print("")
    print(chapter)
    print("")
    for key, value in paragraph.items():
        print("")
        print(key)
        print("")
        for i in value:
            print(i)