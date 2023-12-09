from pprint import pp
from dataclasses import dataclass
from typing import List

FNAME = 'input'

data = []
with open(FNAME) as f:
    data = f.read().splitlines()

total = 0

for d in data:
    dsplit = d.split(":")
    game = dsplit[0]
    gamedata = dsplit[1]
    gameNumsRaw = gamedata.split("|")
    winningNumbers = gameNumsRaw[0]
    myNumbers = gameNumsRaw[1]
    winningNumbers = [int(x) for x in list(filter(len, winningNumbers.split(" ")))]
    myNumbers = [int(x) for x in list(filter(len, myNumbers.split(" ")))]
    overlapCount = len(set(winningNumbers).intersection(set(myNumbers)))
    score = 0
    if overlapCount > 0:
        score = 2**(overlapCount - 1)
    total = total + score

pp(total)


@dataclass
class GameInfo:
    winningNumbers: List[int]
    myNumbers: List[int]
    points: int

myHand = {}
state = []

for d in data:
    dsplit = d.split(":")
    game = dsplit[0]
    gamedata = dsplit[1]
    gameNumsRaw = gamedata.split("|")
    winningNumbers = gameNumsRaw[0]
    myNumbers = gameNumsRaw[1]
    winningNumbers = [int(x) for x in list(filter(len, winningNumbers.split(" ")))]
    myNumbers = [int(x) for x in list(filter(len, myNumbers.split(" ")))]
    overlapCount = len(set(winningNumbers).intersection(set(myNumbers)))

    state.append(GameInfo(winningNumbers, myNumbers, overlapCount))

pp(state)

for i in range(len(state)):
    # Add the card of that value to my hand
    nextC = state[i].points
    pp(("card", i + 1, "idx", i, "score", nextC))
    if not myHand.get(i + 1):
        myHand[i + 1] = 1
    else:
        myHand[i + 1] = myHand[i + 1] + 1

    pp(myHand)
    # Process this card value and add to hand
    for _ in range(myHand[i + 1]):
        for j in range(i + 1, i + nextC + 1):
            if not myHand.get(j + 1):
                myHand[j + 1] = 1
            else:
                myHand[j + 1] = myHand[j + 1] + 1
    pp(myHand)
    pp("<<<<<<<<<<<<")

pp("===========================")
pp(myHand)

sum = 0
for _, v in myHand.items():
    sum = sum + v

pp(sum)
