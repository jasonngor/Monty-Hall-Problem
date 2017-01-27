import random

globalCount = 0
prizeCount = 0

# This script statistically tests the Monty Hall problem by setting up a
# scenario where a contestant picks door 1, and always switches
# to door 2 or 3

# loops through 100,000 times to get a good estimate
while globalCount <= 100000:
    # sets up 3 doors
    dList = [False, False, False]

    # picks a random door to hide the prize in
    prize = random.randint(0,2)
    dList[prize] = True

    # if prize is behind the first door, open either the second or third door
    # In this scenario, switching would be disadvantageous
    if dList[1:] == [False, False]:
        randNdx = random.randint(1,2)
        dList.pop(randNdx)

    # else, open the false door from the second or third door
    # In these two scenarios (either door 2 or 3 is true), switching would
    # be advantageous
    else:
        falseNdx = dList[1:].index(False)
        dList.pop(falseNdx)

    # if the prize is not behind the first door, count as a win
    if dList[0] == False:
        prizeCount += 1

    globalCount += 1

# should print a value close to 66.7%, showing that the contestant wins
# 66.7% of the time if he chooses to switch doors
print(prizeCount/globalCount * 100)
