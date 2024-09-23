import random

rand_num = random.randint(1, 100)



while True:
    guess = int(input("Enter your guess: "))
    if guess>rand_num:
        print("Try a smaller number: ")
        
    else:
        print("Correct!")      
        break


    
        
