""" 1. Bank account balance

2. Deposit
3. Withdrawal
4. Exit
"""

def show_balance():

    return f"Your balance is {balance}"



def deposit():
    amount = float(input("Enter the amount of deposit you want to put into: "))
    if amount < 0:
        print("The amount must not be less than 0!")

    else:
        return amount



def withdraw():
    withdrawal = float(input("Enter the amount of money you want to get back: "))
    if withdrawal > balance:
        print("Insufficient funds!")
        return 0
    else:

        return withdrawal

balance = 0
is_running = True

while is_running:
    print("-----Choices-----")
    print("1. Bank account balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter the choice: ")
    match choice:
        case "1":
            print(show_balance())



        case "2":

            balance = balance + deposit()
        case "3":
            balance -= withdraw()
        case "4":
            is_running = False
        case _:
            print("The choice is not valid!")

print("Thank you for choosing us! Have a nice day!")




