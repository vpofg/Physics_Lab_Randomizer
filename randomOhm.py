import random 



def ohmRand():
    ohmVal = input("Enter the ohm value: ")
    toleranceRes = input("Enter the tolerance value in percent: ")
    valGen = input("Enter the number of values to generate: ")
    toleranceRange = (float(toleranceRes) / 100) * float(ohmVal)
    lowerBound = float(ohmVal) - float(toleranceRange)
    upperBound = float(ohmVal) + float(toleranceRange)
    for i in range (0, int(valGen)):
        randNum = random.uniform(lowerBound, upperBound)
        print(randNum)


ohmRand()


def printName():
    name = input("Enter your name: ")
    print("Hello " + name + "!")

printName()