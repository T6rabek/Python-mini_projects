questions = ('What is the name of our galaxy?', 
             'Which creature can live in both water and desert?', 
             'How many fingers do humans have?', 
             'What was the first program in python?')
options = (('A. Milky way', 'B. Milk way', 'C. Hello world!'),
           ('A. Frog', 'B. Whale', 'C. Hello world'),
           ('A. 10', 'B. 20', 'C. Hello world!'),
           ('A. Calculator', 'B. Computer', 'C. Hello world!'))
answers = ('A', 'A', 'B', 'C')

guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------")
    print(question)
    
   
    for option in options[question_num]:
        
        print(option)
        
    
    
    guess = input("Enter the answer: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        
    question_num+=1
        
print(f"You found {score} correct answers!")
percent = score*100/len(questions)
print(f"Your percentage is {percent}%")