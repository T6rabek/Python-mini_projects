import random



balance = 100

def spin_row():
    global balance

    while balance > 0:
        print(f"Your balance is ${balance}!")

        bet = input("Enter the amount of bet: $")
        if not bet.isdigit():
            print("Bet needs to be a positive #")
            continue
        bet = int(bet)
        if bet <= 0:
            print("Bet must be greater than zero!")
            continue

        elif bet > balance:
            print("Insufficient funds! ")
        else:
            balance -= bet
            break

    symbols = ['🍒','🍋','🔔', '🍏', '🍉']
    spinning = random.choices(symbols, k=3)
    print(" | ".join(spinning))

    if spinning[0] == spinning[1] == spinning[2]:
        print("You win completely!")
        winnings = bet * 10
    elif spinning[0] == spinning[1] or spinning[0] == spinning[2] or spinning[1] == spinning[2]:
        print('You win!')
        winnings = bet * 3
    else:
        print("You lose!")
        winnings = 0
    balance +=winnings
    return winnings












def choices():
    while True:
        global balance
        print("Options:\n1.Balance\n2.Play\n3.Benefit\n4.Quit")
        option = input("Choose one option: ")
        if option == "1":
            print(f"Your balance is ${balance}")
        elif option == "2":
            spin_row()
        elif option == "3":
            benefit()
        elif option == "4":
            break

        else:
            print("Choose one of the choices!")
        print("Thank you for playing!")


def benefit():
    global balance
    ben = balance - 100
    if balance > 100:
        print(f"Your benefit is: ${ben}")
    elif balance<100:
        print(f"Your loss is ${ben}")
    else:
        print("You do not have whether benefit or loss!")





def main():

    print("*******************************")
    print("Welcome to slot machine python!")
    print("Symbols: 🍒🍋🍉🔔🍏")
    print("*******************************")

    choices()









if __name__ == "__main__":
    main()

