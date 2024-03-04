desserts = ["cake", "chocolate", "ice cream", "cake again", "aaaaaaa", "spongecake"]
supermarket = ["cheesecake", "chocolate", "ice cream", "brownies", "spongecake", "twinkies"]

for dessert in desserts:
    print(dessert)

# henriAge = 17
# henriWallet = 0
# henriLicence = "none"

# #true
# if henriAge < 20 and henriWallet <100 and henriLicence != "valid":
#     print("true")

# #false
# if henriAge > 10 and henriWallet == 0 and henriLicence != "none":
#     print("false")

# if henriAge > 15 and henriWallet >10:
#     print("you can go out")

# else:
#     print("stay home")


# purchase = 5
# if purchase >100:
#     print("free tshirt")

# elif purchase > 30:
#     print("free icecream")

# elif purchase > 10:
#     print("50p off")

# else:
#     print("nothing for you")



# match your desserts list to what the supermarket has
#     if the supermarket has it, print ("Yes, we're having ------DESSET NAME- for dinner")
# if the supermarket doesn't have it ("poor me, i will not have ----DESSERT NAME---- ")

for x in desserts:
    if x in supermarket:
        print("yes, we're having" ,x, "for dinner")
    else:
        print("poor me, i will not have" ,x)


test = []

if len(test) == 0:
    print("empty")

if test:
    print("aa")


