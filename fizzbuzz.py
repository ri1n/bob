numbers = list(range(1,100))

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