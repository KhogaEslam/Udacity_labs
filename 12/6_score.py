
level = 0
score = 65
if score < 30:
    level = 1
elif score < 50:
    level = 2
elif score < 70:
    level = 3
    #Don't forget the escape character in this print statement.
    print("You\'ve reached level 3")
elif score < 90:
    level = 4
else:
    level = 5
    print("Level 5, way to go")
print(score)
print(level)