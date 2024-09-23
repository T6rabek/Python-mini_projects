import random

options = ('Rock', 'Paper', 'Scissors')
while True:
    player = input('Enter one of the choices: ').capitalize()
    computer = random.choice(options)
    
    if player not in options:
        print('Choices must be either one: Rock, paper, scissors')
        player = input('Try again: ')
    
    print(f"You chose {player}")
    print(f"Computer chose {computer}")
    
    
    
    
    
    if player == computer:
        print('TIE!')
        
    elif player == 'Rock' and computer == 'Scissors':
        print('You win!')
    
    elif player == 'Scissors' and computer == 'Paper':
        print("You win!")
        
    elif player == 'Paper' and computer == 'Rock':
        print("You win!")
        
    else:
        print("You lose!")
        
    guess = input('Do u wanna continue? (y/n): ').lower()
    if guess=='y':
        continue
    else:
        print('Thanks for playing!')
        break
    
    


