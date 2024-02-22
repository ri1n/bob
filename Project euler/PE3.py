# # The prime factors of 13195 are 5, 7, 13 and 29.

# # # What is the largest prime factor of the number 600851475143 ?

# # num = 13195
# # large_pf = 0
num = 13195
large_pf = 0

# # for y in range(num, 2, -1):
    
    if num%y == 0: #divisible by largest number (y)

        for x in range(y, 2, -1): 
            while large_pf == 0: #to only get 1 value
                if y%x !=0: #checks if y is a prime number
                    print(y)
                    large_pf = y


# # print(large_pf)

# prime_nums = []
# non_prime = []


# def get_prime(target_num):
#     for i in range(2, target_num):
#         for x in range(2,i-1):
#             if i%x == 0:
#                 non_prime.append(i)
#             else:
#                 prime_nums.append(i)



# get_prime(315)
# print(prime_nums)


# def prime(number):
#     for i in range(2, number):
#         if number%x == 0:
#             continue

prime_num=[]
prime_factors = []


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_prime(target_num):
    for i in range(2, target_num,1):
        x = is_prime(i)
        if x:
            prime_num.append(i)


def get_prime_factors(target_num, prime_num):
    i = 0
    j = target_num
    while i < len(prime_num):
        if j % prime_num[i] == 0:
            prime_factors.append(prime_num[i])
            j=j/prime_num[i]
        if j % prime_num[i] != 0:
            i=i+1


get_prime(600851475143)

get_prime_factors(600851475143, prime_num)
print(prime_factors)
print(prime_factors[-1])