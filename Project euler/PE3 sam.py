prime_Nums = []
Prime_Factors = []


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_Prime(target_Number):
    for i in range(2, target_Number, 1):
        x = is_prime(i)
        if x == True:
            prime_Nums.append(i)

def get_PrimeFactors(target_Number, prime_Nums):    
    i = 0
    j = target_Number
    while i < len(prime_Nums):
        if j % prime_Nums[i] == 0:
            Prime_Factors.append(prime_Nums[i])
            j = j / prime_Nums[i]
        if j % prime_Nums[i] != 0:
            i = i+1
        
        

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]

get_Prime(600851475143)
# print(prime_Nums)

get_PrimeFactors(600851475143, prime_Nums)
print(Prime_Factors)