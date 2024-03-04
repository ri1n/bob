

# def greeter_function(name)
#     print(f"hello you are {name}")

# while True:
#     name = input("A:")
#     greeter_function(name)
import random

random.randint(1,6)


def roll_dice(number):
    sum=0
    
    i = 1
    while i < int(number+1):
        x = random.randint(1,6)
        print(f"Dice {i}: {x}")
        i+=1
        sum += x

    print(f"sum of dice: {sum}")

while True:
    
    number = int(input("how many dice? "))
    if number == 0:
        break
    roll_dice(number)
