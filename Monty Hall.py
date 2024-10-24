from random import randint # randint randomly generates a number between x -  y, and it will also be an integer
from random import seed #forces the random number generator to generate a new sequence of random numbers

wins = 0 #records the number of wins across the 10,000 trials
losses = 0 #record the number of losses across the 10,000 trials
TRIALS = 10000 #constant variable. The variable will not change, it is a fixed amount for the number of trials
closed_doors = 3 #the number of doors that are closed for one trial

#generating a new sequence of random numbers (seed)
seed()

#runs the code 10,000 times
for i in range(TRIALS):
    #hiding the prize behind one of three doors randomly
    prize_door =  randint(1,3)
    #which door the player chooses during the game
    player_choice = randint(1,3)

    #AT THIS POINT, the prize has been hidden behind one of the doors and the player has chose a door

    #Host is opening one of the other two doors which has a fake prize behind it
    while closed_doors > 2:
        # host is opening a door
        host_door = randint(1,3)
        # the door the host opens is not the player's door or the prize door
        if host_door == prize_door or host_door == player_choice:
            continue
        #AT THIS POINT, the number closed decrease by 1 because host has opened one door
        closed_doors -= 1

    #AT THIS POINT, the prize has been hidden, the player has chose a door, the host has opened a door.
    #host asks the player if they want to switch doors.
    # For the sake of our argument, we assume the player will always switch doors

    #Runs through all possible combinations where the player will choose the remaining door
    if player_choice == 1 and host_door == 3:
        player_choice = 2
    elif player_choice == 1 and host_door ==2:
        player_choice = 3
    elif player_choice == 2 and host_door ==3:
        player_choice = 1
    elif player_choice == 2 and host_door ==1:
        player_choice = 3
    elif player_choice == 3 and host_door == 2:
        player_choice = 1
    elif player_choice == 3 and host_door ==1:
        player_choice = 2
    if player_choice == prize_door:
        wins+=1
    else:
        losses+=1
    #Resets the number of closed doors each trial
    closed_doors = 3
#converts the amount of times that player has won to a percent
total_win_rate = round((wins/TRIALS)*100,1)
#Shows statistics(how many times player has won vs. times player has lost)
print("The player in " + str(TRIALS) + " trials won a new car " + str(wins) + " times")
print("The player lost " + str(losses) + " times. This resulted in a success rate of " + str(total_win_rate) +"%")

















