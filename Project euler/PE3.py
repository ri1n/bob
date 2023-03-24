# The prime factors of 13195 are 5, 7, 13 and 29.

# # What is the largest prime factor of the number 600851475143 ?

num = 600851475143
num = int(num)
large_pf = 0

for y in range(2, num, -1):
    print(y)
    if num%y == 0: #divisible by largest number (y)

        for x in range(2, y, -1): 
            while large_pf == 0: #to only get 1 value
                if y%x !=0: #checks if y is a prime number
                    print(y)
                    large_pf = y


print(large_pf)            