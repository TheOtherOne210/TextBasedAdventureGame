
def EndingScene():
    print("You are now safe")
    print("thanks for playing")
    quit()

def cabinscene():
    print("As you approach the cabin it seems as there are people inside")
    print("Do you go inside or do you want to go somewhere else")
    playerInput = input("Go inside or Find something else: ")
    if playerInput == "go inside":
        print("you go inside the cabin")
        print("you find your family")
        EndingScene()
    elif playerInput == "find something else":
        print("You go away from the cabin")
        print("as you progress you get eaten by wolves")
        cabinscene()
    else:
        print("choose an option")

def deadend():
    print("Do you want to go back or stay at this very obvious dead end")
    playerInput = input("Stay or go back: ").strip().lower()
    if playerInput == "stay":
        print("You stay and look at the deadend")
        print("Years past and you are now dead due to starvation and Dehydration")
        quit()
    elif playerInput == "go back":
        print("You do the obvious option and go back")
        introscene()
    else:
        print("Choose a valid option")
        deadend()

def introscene():
    playerName = input(">What is your name: ")
    print(f">Hello {playerName}")  

    print("The adventure starts with you in a mystical forrest")
    print("As you continue you enter towards a cross road with only two paths")
    print("You can only choose to go left or right")

    playerInput = input("left or right: ").strip().lower()
    if playerInput == "left":
        print("you chose left")
        print("As you follow the road it then leads you to a dead end")
        deadend()
    elif playerInput == "right":
        print("you chose right")
        print("You follow down this path towards to be what looks like a cabin")
        cabinscene()
    else:
        print("invalid option. Please try again")
        
introscene()
