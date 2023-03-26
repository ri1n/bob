num = 100
large_pf = 0


for x in range(1, num): 
    if num%x == 0: #divisible by largest number (y)
        print(x)

        for y in range(2, x):
            if x%y ==0:
                print("y")
            elif x%y!=0:
                print(x)
