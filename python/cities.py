cities = {"london" : {"country": "england", "population": "9m", "fact" :"wo'or bo'o"}, "new york": {"country": "USA", "population": "8.5m", "fact": "new version of york"}, "paris": {"country": "france","population": "2.1m", "fact": "jayz"}}
for x in cities:
    print(x.title(),str(cities[x]).title())