# list = []
# tuple = ()
# dict = {} key:value

alien01 = {"colour":"porple", "speed":"slow", "points":1}
print(alien01["colour"])
alien01["colour"] = "blue"
print(alien01["colour"])

print(f"you killed the {alien01['colour']} alien, you got {alien01['points']} points")


alien01["x_position"] = 0
alien01["y_position"]= 100

print(alien01)

del alien01["colour"]

print(alien01)