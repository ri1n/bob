palindrome=[]
for x in range(100, 1000):
    for y in range(100, 1000):
        numbers =[]
        a = x*y

    for i in str(a):
        numbers.append(int(i))

    if len(numbers) == 5:
        if numbers[0] == numbers[-1] and numbers[1] == numbers[-2]:
            palindrome.append(numbers)
    # if len(numbers) == 5:
    #     if numbers[0] == numbers[4] and numbers[1] == numbers[3]:
    #         palindrome.append(numbers)
    # if len(numbers) == 6:
    #     if numbers[0] == numbers[5] and numbers[1] == numbers[4] and numbers[2] == numbers[3]:
    #         palindrome.append(numbers)
    # if len(numbers) == 7:
    #     if numbers[0] == numbers[6] and numbers[1] == numbers[5] and numbers[2] == numbers[4]:
    #         palindrome.append(numbers) 

print(palindrome)