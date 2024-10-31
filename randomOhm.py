import random 



def ohmRand():
    ohmVal = input("Enter the ohm value: ")
    toleranceRes = input("Enter the tolerance value in percent: ")
    toleranceRange = (float(toleranceRes) / 100) * float(ohmVal)
    lowerBound = float(ohmVal) - float(toleranceRange)
    upperBound = float(ohmVal) + float(toleranceRange)
    for i in range (0, 5):
        randNum = random.uniform(lowerBound, upperBound)
        print(randNum)


ohmRand()