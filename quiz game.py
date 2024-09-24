total = 0
foods = []
prices = []

while True:
    food = input("Enter a food you wanna buy (q to quit): ") 
    
    if food.lower() != "q":
        foods.append(food)
        price = float(input("Enter the price of a food: $"))
        prices.append(price)
        
    else:
        break
    
print("-----Your cart------")
    
for x in foods:
    print(x)
    
for i in prices:
    total = total + i

print(total)