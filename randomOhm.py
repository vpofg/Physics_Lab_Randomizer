import random 
from random import randrange



def ohmRand():
    ohmVal = float(input("Enter the ohm value: "))
    toleranceRes = float(input("Enter the tolerance value in percent: "))
    toleranceRange = (float(toleranceRes) / 100) * float(ohmVal)
    lowerBound = ohmVal - toleranceRange
    upperBound = ohmVal + toleranceRange
    for i in range (0, 5):
        randNum = randrange(lowerBound, upperBound)
        print(randNum)


ohmRand()