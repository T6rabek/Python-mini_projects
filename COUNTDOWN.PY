import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(my_time)):
    hours = int(x/3600)
    minutes = int((x/60)%60)
    seconds = x%60
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
   
print("TIME'S UP!")