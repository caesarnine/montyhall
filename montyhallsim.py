# let's import the libraries we need
import numpy as np
import random

# first, the function to simulate the door that the prize is behind
# each element is a different game, with the first representing the first game, the second the second, and so on

def simulate_prizedoor(nsim):
    # randomly choose one of the three doors
    answer = np.random.randint(0,3,nsim)
    return answer


# next, the function to simulate the users guesses
# each element is a different game, with the first representing the first game, the second the second, and so on

def simulate_guess(nsim):
    # randomly choose one of the three doors
    answer = np.random.randint(0,3,nsim)
    return answer
print simulate_guess(3)

# and then, a function to simulate the goat doors; which are doors that the prize is not behind
# each element is a different game, with the first representing the first game, the second the second, and so on

def goat_door(prizedoors, guesses):
    # initialize an empty array that we will append to
    result = np.empty(0)
    # go through each game (each element) one by one
    for door in range(0,len(prizedoors)):
        # the list of all doors
        answer = [0,1,2]
        # remove the prize door from the list, since it can't be chosen as a goatdoor
        answer.pop(answer.index(prizedoors[door]))
        # if the guess was different, remove that guess as well, since that can't be a goatdoor either
        if guesses[door] in answer:
            answer.pop(answer.index(guesses[door]))
        # last, append to the previously initialized array, if there's more than one choice left, randomly
        # choose from the two remaining choices (in the case if the door chosen was the prizedoor)
        result = np.append(result,(random.choice(answer)))
    return result.astype(int)

# continuing, a function to simulate if the participant changes his/her guess based on the opened goat door
# each element is a different game, with the first representing the first game, the second the second, and so on

def switch_guess(guesses, goatdoors):
    # initialize an empty array that we will append to
    result = np.empty(0)
    # go through each game (each element) one by on
    for door in range(0,len(guesses)):
        # the list of all doors
        answer = [0,1,2]
        # remove the door that was guessed
        answer.remove(guesses[door])
        # remove the door that was opened as a goatdoor
        answer.remove(goatdoors[door])
        # append the remaining result, the door that the player would choose if they switched, to the previously
        # initialized array
        result = np.append(result,answer)
    return result.astype(int)

# last, a function to calculate the winning percentage over multiple simulations.

def win_percentage(guesses, prizedoors):
    # initialize a float to keep track of the number of wins
    wins = float()
    # go through each game to calculate which ones one and which ones didn't
    for i in range(0,len(guesses)):
        # if the guess was the prizedoor in the end, then count that as a win
        if guesses[i] == prizedoors[i]:
            wins += 1
    # return the percentage of wins
    return wins/len(guesses) * 100

# finally, let's pull it all together, and run 30,000 simulations to see whether it's better to switch doors or not.

# simulate 30,000 guesses
guesses = simulate_guess(30000)
# simulate 30,000 prizedoors
prizedoors = simulate_prizedoor(30000)
# simulate 30,000 goatdoor openings
goatdoors = goat_door(prizedoors,guesses)
# simulate for each 30,000 games if the player had switched his guess
switchedguesses = switch_guess(guesses, goatdoors)

# print the win percentage if the player did not switch guesses
print "The win percentage is " + str(win_percentage(guesses,prizedoors)) + " if doors aren't switched."
# print the win percentage if the player did switch guesses
print "The win percentage is " + str(win_percentage(switchedguesses,prizedoors)) + " if doors are switched."

