import random

random.randint(1,6)

def roll_dice(number):
    sum = 0
    i = 1
    while i < int(number+1):
        x = random.randint(1,6)
        print(f"Dice {i}: {x}")
        i+=1
        sum += x
    print(f"p1 sum: {sum}")

    return sum

def pc_dice(number):
    pc_sum = 0
    
    i = 1
    while i < int(number+1):
        y = random.randint(1,6)
        print(f"Dice {i}: {y}")
        i += 1
        pc_sum += y
    print(f"pc sum: {pc_sum}")

    return pc_sum

def judge(number):
    a = int(roll_dice(number))
    b = int(pc_dice(number))
        
    if a > b:                 
        print("player wins")                                
      
    elif a == b:
        print("draw")
    else:
        print("pc wins")
    

while True:
    
    number = int(input("how many dice? "))
    if number == 0:
        break
    
    judge(number)












#     Make 2 more functions:
# 1. pc_dice()
# 2. judge()

# After player enters his dice number, the computer will also roll the same number of dice.

# the judge function will see whose number is higher, and declare a winner.