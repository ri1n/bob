# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome_test(numbers):
    palindrome = []
    
    if len(numbers) == 6:
        if numbers[0] == numbers[-1] and numbers[1] == numbers[-2] and numbers[2] == numbers[-3]:
            palindrome.append(numbers)


    if palindrome != []:
        print(palindrome)
    return palindrome


multiple = [1]
def multiplier():
    for x in range(100, 1000):
        for y in range(100, 1000):
            numbers =[]
            a = x*y

            for i in str(a):
                numbers.append(int(i))

            palindrome_test(numbers)

            

    
    #return palindrome_test


def sorter():
    



multiplier()

numbers = multiplier()




    
    



            

        

