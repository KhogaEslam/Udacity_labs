
# Description followed by input
# if choice 1:
#    Description followed by input
#    if choice 2:
#       Description followed by input
#       if choice 3:
#          Description
#       else not choice 3:
#          Description
#    if not choice 2:
#       Description followed by input
#       if choice 4:
#          Description
#       else not choice 4:
#          Description
# if not choice 1:
#    Description followed by input
#    if choice 5:
#       Description followed by input
#       if choice 6:
#          Description
#       else not choice 6:
#          Description
#    if not choice 5:
#       Description followed by input
#       if choice 7:
#          Description
#       else not choice 7:
#          Description

print("You find yourself standing in an open field, filled with grass and",
      "yellow wildflowers.")
print("In front of you is a house.")
print("To your right is a dark cave.")

choice = input("What would you like to do? Type a to enter the house, type b to enter the cave: ")
# choice 1
if choice.lower() == "a":
    print("You've entered the house.")
    print("It looks like a tornado hit the inside of the house. Everything is a mess, and it looks like someone was looking for something in a hurry.")
    print("You see a scrap of paper on the floor at the same time you see movement out the window.")
    choice = input("What would you like to do? Type a to pickup the scrap of paper, type b to investigate the movement: ")
    #choice 2
    if choice.lower() == "a":
        print("It looks like a note.")
        print("You start to read it and see that it is an invitation to a famous school for witchcraft and wizardry!")
        choice = input("What would you like to do? Type a to try and return the invitation to the rightful owner, type b to keep it for yourself: ")
        #choice 3
        if choice.lower() == "a":
            print("You recognize the name, so you leave the house in search of the intended recipient.")
        else:
            print("You start off towards the train station, hoping you're not too late.")
    else: 
        print("You see some tracks in the mud outside the window.")
        print("You decide to follow them to see where they lead and see a large furry animal up ahead.")
        choice = input("What would you like to do? Type a to continue following the trail, type b to turn around: ")
        #choice 4
        if choice.lower() == "a":
            print("You continue following the creature at what you hope is a safe distance.")
            print("Unfortunately, it catches your scent and turns around, running at you too quickly for you to move.")
        else:
            print("You turn around and find that you are now hopelessly lost.")
# not choice 1
else:
    print("You slowly enter the cave. There is barely enough light from the opening to see.")
    print("You encounter a pit of snakes with a vine")
    #choice 5
    choice = input("What would you like to do? Type a to turn around, type b to swing over the pit: ")
    if choice.lower() == "a":
        print("You turn around and leave the cave, but find you are out of water. You decide to return home.")
    else: 
        print("You grab the vine and successfully swing over the pit.")
        print("There is a torch on the other side that you are able to light. Following the cave you see two tunnels.")
        choice = input("What would you like to do? Type a to take the tunnel to the left, type b to take the tunnel to the right: ")
        print("You start down the tunnel, but find that the floor suddenly gives way. You slide in the dark for some time before being shot out of the tunnel and into a lake.") 
print("You wake with a start, unsure of what just happened.")