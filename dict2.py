# favouritebooks={"sam": "Le Petit Prince" , "henri": "Kagejitsu","crystal": "A TIME TO KILL"}
# print(f"sam's favourite book is {favouritebooks['sam']}")

# for k,v in favouritebooks.items():
#     print(f"{k}'s favourite book is {v}")

# # dict in a list
# alien01 = {"colour":"porple", "speed":"slow", "points":1}
# alien_swarm = []
# for i in range(30):
#     alien_swarm.append(alien01)
# print(alien_swarm)

# list in a dict
# favouritebooks={"sam": ["Le Petit Prince", "Watchmen"] , "henri": ["Kagejitsu", " Naruto"],"crystal": ["A TIME TO KILL","THE HOUSE OF MIRTH"]}



# print(favouritebooks["crystal"][1].title())

# dict in a dict
favouritebooks={"sam": "Le Petit Prince" , "henri": {"Book title":"Kagejitsu", "pages" : 200} ,"crystal": "A TIME TO KILL"}
print(favouritebooks["henri"]["pages"])

