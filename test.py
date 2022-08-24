import random
import time

num = random.randrange(1,100)
print(num)
while True:
    time.sleep(1)
    start = int(input("Type a number from 1 to 100. "))
    if start > num:
       print("To high") 
    if start < num:
        print("To low")
    if start == num:
        print("You did it")
        break




