from random import randint

pickNumber = int(input("How many quick picks? "))
pickList = [0,0,0,0,0,0]
for i in range(pickNumber):
    for x in range(6):
        pickRandom = randint(1,45)
        while pickRandom not in pickList:
            pickList[x] = pickRandom
            pickRandom = randint(1,45)
    pickList.sort()
    print(pickList)

