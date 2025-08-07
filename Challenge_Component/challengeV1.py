'''This is have all the challenges that I will have during the game 
30/7/2025
Pika Ranzinger 
Version one: Write all the code'''
import time 
import random
import json 

class Challenge:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def ch1_1_challenge(self):
        #first challenge of chapter 1, it's a cryptogram
        
        #answer and score  
        sentence = "The universe is a dark forest"
        attempt = 0
        
        #challenge
        print(""" 
                __ __ E     __ __ I  __ E  __ __ E     I  __    __    
                26 16 19    7  23 21 13 19 15 20 19    21 20    1
                __ __ __ __    __ __ __ E  __ __ 
                6  1  15 22    2  25 15 19 20 26""")
        answer = input("Enter answer: ")
        
        #checking
        while answer.lower() != sentence.lower():
            #the user must answer correctly before moving on
            attempt += 1
            print("Wrong answer")
            answer = input("Enter answer: ")
        print("Correct!")
            
        return attempt
    
    def ch1_2_challenge(self):
        #second challenge of chapter 1, a number memory game 
        
        attempt = 0 
        numbers = []
        answers = []
        
        for i in range(5):
            #prints one num then waits 2 secs then another (loop of 5)
            num = random.randint(0,9)
            numbers.append(num)
            print(num)
            time.sleep(2)
        
        #user answer
        answer = input("Enter code: ")
        answer.split()
        for items in answer:
            items = int(items)
            answers.append(items)
        
        while answers != numbers:
            #checks if user answer is the same as answer
            #doesn't allow passage until user gets it right 
            attempt += 1 
            print("Wrong")
            answer = input("Enter code: ")
            answer.split()
            answers = []
            for items in answer:
                items = int(items)
                answers.append(items)
        print("Correct")
        
        return attempt
    
    def ch2_challenge(self, turn):
        '''challenge for chapter 2'''
        attempt = 0 
        
        if turn == 1:
            #riddle one
            print("""
                    “Start with silence in a heavy bowl,
                    Stir with shadows from a sleepless soul.
                    Sprinkle years lost to shame and pride—
                    Then bake until the truth can’t hide.
                    Tell me, wanderer, what is it I make?”
                   """)
            #answer 
            answer1 = "regret"
            
            #user answer
            user_answer1 = input("Answer: ")
            
            while answer1.lower() != user_answer1.lower():
                #doesn't allow passage until user answer is correct
                attempt += 1
                print("Wrong answer")
                user_answer1 = input("Answer: ")
            print("Correct")
            
        if turn == 2:
            #riddle 2 
            print(""""
            “I tick but make no sound,
            I’m neither lost nor found.
            I measure time through lack,
            Yet wear no numbered plaque.
            What am I?”
            """)
            
            #answer
            answer2 = "an absence"
            
            #user answer 
            user_answer2 = input("Answer: ")
            
            while answer2.lower() != user_answer2.lower():
                #doesn't allow passage until user answer is correct
                attempt += 1
                print("Wrong answer")
                user_answer2 = input("Answer: ")
            print("Correct") 
            
        if turn == 3:
            print("""
            “I fall, yet never sink.
            I lift, yet carry weight.
            I shine, yet never blind.
            I wound, though soft and light.
            I am part of pain and beauty both.
            What am I?” 
            """)
            
            #answer
            answer3 = "a word"
            
            #user answer
            user_answer3 = input("Answer: ")
            
            while answer3.lower() != user_answer3.lower():
                #doesn't allow passage until user answer is correct
                attempt += 1
                print("Wrong answer")
                user_answer3 = input("Answer: ")
            print("Correct")  
            
        return attempt
    
    def ch3_challenge(self):
        '''challenge for chapter 3'''
        attempt = 0
        paths = [3, 4, 6]
        choices = []
        
        while choices != paths:
            #doesn't let user pass until correct paths in order are taken
            #resets choices every round
            choices = []
            #first set
            print("""
                    1. A knight missing its heart, silent and unmoving.
                    2. A scholar chained to burning books, eyes closed in contemplation.
                    3. A child with eyes that blinked stars, holding a feather soaked in ink.
    
                    Each offered a price:
                    “Take my path and lose your pride.”
                    “Take mine and lose your name.”
                    “Take mine and face the truth that breaks.”
                       """)            
            choice1 = int(input("Choice: "))
            
            if choice1 != 3:
                #wrong choice
                print("""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)
                attempt += 1
                
            elif choice1 == 3:
                #correct choice continues on
                choices.append(choice1)
                print(""" 
                Lysander arrives at another set of doors, this one has five doors.
                They look at the moving pictures featured on the doors and recognise them 
                as the five stages of grief:
                1. Denial - depicting as a man aggressively shaking his head refusing to even look at Lysander
                2. Anger - depicting as a woman screaming towards Lysander
                3. Bargaining - depicting a person on their knees with their hands clasped praying for something 
                4. Depression - depicting a man with his back against a wall hunching over a picture frame
                5. Acceptance - depicting a woman standing at a gravestone, she smiling sadly
                """)
                
                choice2 = int(input("Choice: "))
                
                if choice2 != 4:
                    #wrong choice
                    print("""
                Lysander is lead to a narrow corridor, filled with continous twists and turns
                until they finally see a light at the end of the tunnel. They exit 
                this hours long maze they've trekked through to see they have 
                arrived at the same three statues.
                """)
                    attempt += 1 
                    
                elif choice2 == 4:
                    #correct choice and continues on
                    choices.append(choice2)
                    print("""
                        Lysander arrives in a circular room. The room had 7 doors when
                        you excluded the door Lysander had just entered from. Each door each had
                        just one word written on it.
                                1. Pride
                                2. Greed
                                3. Wrath
                                4. Envy
                                5. Lust
                                6. Gluttony
                                7. Sloth
                                       """) 
                    
                    choice3 = int(input("Choice: "))
                    
                    if choice3 != 6:
                        #wrong choice
                        print("""
                    Lysander is lead to a narrow corridor, filled with continous twists and turns
                    until they finally see a light at the end of the tunnel. They exit 
                    this hours long maze they've trekked through to see they have 
                    arrived at the same three statues.
                    """)
                        attempt += 1 
                    
                    elif choice3 == 6:
                        #correct choice and continues on 
                        choices.append(choice3)
                        
        return attempt
    
    def ch5_challenge(self):
        '''challenge 1 for chapter 6'''
        attempt = 0 
        options = ["rock", "paper", "scissors", "lizard", "spock"]
        win = 0 
        
        while win != 1:
            #doesn't allow passage until user wins 
            print("""
            What will you pick:
            1. rock
            2. paper
            3. scissors
            4. lizard
            5. spock
            """)
            
            #user picks theirs
            user_choice = int(input("Choice: "))
            
            #configures options for both
            user = options[user_choice-1]
            bot = options[random.randint(0,4)]
            
            #if statements for what beats what 
            if bot == "rock" and (user == "scissors" or user == "lizard"):
                attempt += 1 
                print("Bot wins")
            elif bot == "paper" and (user == "rock" or user == "spock"):
                attempt += 1 
                print("Bot wins")
            elif bot == "scissors" and (user == "paper" or user == "lizard"):
                attempt += 1 
                print("Bot wins")
            elif bot == "lizard" and (user == "paper" or user == "spock"):
                attempt += 1
                print("Bot wins")
            elif bot == "spock" and (user == "rock" or user == "scissors"):
                attempt += 1
                print("Bot wins")
            else: 
                print("You win!")
                win += 1
            
        return attempt
    
    def ch6_1_challenge(self):
        attempt = 0 
        bot_num = random.randint(1,100)
        user_num = 0 
        
        while user_num != bot_num:
            user_num = int(input("Enter number: "))
            if user_num > bot_num:
                print("Lower")
                attempt += 1
            elif user_num < bot_num:
                print("Higher")
                attempt += 1
        
        return attempt
    
    def ch6_2_challenge(self):
        '''challenge 2 for chapter 6'''
        attempt = 0 
        win = 0
        math_q = []
        math_a = []    
        
        with open(self.file_path) as file:
            #opens the file
            questions = json.load(file)
            for chapter, challenge in questions.items():
                #finds the correct set for this challenge
                if chapter == "ch6.2":
                    maths = challenge
        
        for questions, answers in maths.items():
            #separates answers and questions
            math_q.append(questions)
            math_a.append(answers)
            
        while win != 1:
            #doesn't allow a pass until below set time
            #sets time
            start_time = time.time()
            
            for i in range(10):
                #prints 10 random questions
                num = random.randint(0, 19)
                user_a = 0
                answer = math_a[num]
                question = math_q[num]
                
                while user_a != answer:
                    #doesn't allow to continue on next until user gets it correct
                    user_a = int(input(f" {question} = "))
                    if user_a != answer:
                        #if answer is wrong
                        print("Wrong answer")
                        attempt += 1
                #else it would be correct
                print("Correct!")
                
            #users end time 
            end_time = time.time()
            
            #calculates total time
            total_time = end_time - start_time
            print(total_time) #prints users total time
            
            if total_time > 60:
                #if greater 1 min it's too slow
                print("Too Slow!")
            else:
                #else allowed to pass
                print("Super Fast!")
                win += 1
                
        return attempt
    
    def ch7_challenge(self):
        '''challenge for chapter 7'''
        attempt = 0
        win = 0
        
        #read the json file 
        with open(file_path) as f:
            file = json.load(f)
            
            for key, value in file.items():
                if key == "ch7":
                    quiz = value
                    
        while win != 1:
            total = 0
            #looping the questions
            for key, value in quiz.items():
                q = value["question"]
                c = value["choices"]
                a = value["answer"]
                
                #shuffle choices
                random.shuffle(c)
                
                #print question 
                print(q)
                
                #looping for choices
                for i in range(len(c)):
                    print(f"{i+1}. {c[i]}")
                
                #user input
                print("")
                user = input("Answer: ")
                
                #checking if answer is correct
                if user.lower() == a.lower() or (user.isdigit() == True and c[int(user)-1] == a):
                    total += 1
                    print("Correct!")
                else:
                    attempt += 1
                    print("Incorrect :(")
                print("")
            
            #checks user got full score 
            if total == 15:
                win = 1
            else:
                print("You didn't get enough to pass")
    
        return attempt 
    
    def ch8_challenge(self):
        '''challenge for chapter 8'''
        attempt = 0
        
        #read the json file 
        with open(file_path) as f:
            file = json.load(f)
            
            for key, value in file.items():
                if key == "ch8":
                    quiz = value
                    
        #looping the questions
        for key, value in quiz.items():
            q_attempt = 0
            win = 0
            q = value["question"]
            c = value["choices"]
            a = value["answer"]
                    
            #shuffle choices
            random.shuffle(c)
            
            while win != 1:
                if q_attempt >= 5:
                    #looping for choices
                    for i in range(len(c)):
                        print(f"{i+1}. {c[i]}")
                        
                #print question 
                print(q)
                        
                #user input
                print("")
                user = input("Answer: ")
                        
                #checking if answer is correct
                if user.lower() == a.lower() or (user.isdigit() == True and c[int(user)-1] == a):
                    win += 1
                    print("Correct!")
                else:
                    attempt += 1
                    q_attempt += 1
                    print("Incorrect :(")
                print("")
                
        
        return attempt         
