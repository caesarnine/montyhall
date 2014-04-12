# let's import the libraries we need
import numpy as np
import random

# first, the function to simulate the door that the prize is behind
# each element is a different game, with the first representing the first game, the second the second, and so on

def simulate_prizedoor(nsim):
    answer=np.random.randint(0,3,nsim)
    return answer


# next, the function to simulate the users guesses
# each element is a different game, with the first representing the first game, the second the second, and so on

def simulate_guess(nsim):
    answer = np.random.randint(0,3,nsim)
    return answer
print simulate_guess(3)

# and then, a function to simulate the goat doors; which are doors that the prize is not behind
# each element is a different game, with the first representing the first game, the second the second, and so on

def goat_door(prizedoors, guesses):
    result = np.empty(0)
    for door in range(0,len(prizedoors)):
        answer = [0,1,2]
        answer.pop(answer.index(prizedoors[door]))
        if guesses[door] in answer:
            answer.pop(answer.index(guesses[door]))
        result = np.append(result,(random.choice(answer)))
    return result.astype(int)

print goat_door(np.array([0, 1, 2]), np.array([1,1,1]))

# continuing, a function to simulate if the participant changes his/her guess based on the opened goat door
# each element is a different game, with the first representing the first game, the second the second, and so on

def switch_guess(guesses, goatdoors):
    result = np.empty(0)
    for door in range(0,len(guesses)):
        answer = [0,1,2]
        answer.remove(guesses[door])
        answer.remove(goatdoors[door])
        result = np.append(result,answer)
    return result.astype(int)

# last, a function to calculate the winning percentage over multiple simulations.

def win_percentage(guesses, prizedoors):
    wins = float()
    for i in range(0,len(guesses)):
        if guesses[i] == prizedoors[i]:
            wins += 1
    return wins/len(guesses) * 100

# finally, let's pull it all together, and run 30,000 simulations to see whether it's better to switch doors or not.

guesses = simulate_guess(30000)
prizedoors = simulate_prizedoor(30000)
goatdoors = goat_door(prizedoors,guesses)


switchedguesses = switch_guess(guesses, goatdoors)

print "The win percentage is " + str(win_percentage(guesses,prizedoors)) + " if doors aren't switched."
print "The win percentage is " + str(win_percentage(switchedguesses,prizedoors)) + " if doors are switched."

