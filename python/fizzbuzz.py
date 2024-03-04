x = int(input("first number:"))
y = int(input("final number:"))
y = y+1


numbers = list(range(x,y))

for num in numbers:
    if num%15==0:
        print(num)
        print("Fizzbuzz")
    elif num%5==0:
        print(num)
        print("Fizz")
    elif num%3==0:
        print(num)
        print("Buzz")