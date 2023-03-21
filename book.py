favouritebooks={"sam": {"book title" :"Le Petit Prince","pages": 100 }, "henri": {"book title":"Kagejitsu", "pages" : 200} ,"crystal": {"book title": "A TIME TO KILL", "pages": 300}}
for x in favouritebooks:
    print(f"{x.title()}'s favourite book is {str(favouritebooks[x]['book title']).title()} and has {str(favouritebooks[x]['pages']).title()} pages")