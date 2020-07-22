import random
chosenNum = random.randint(0,10)
userNum = int(input(“Guess number from 0 to 10: “))

while userNum != chosenNum:
	userNum = int(input(“Try again: “))

print(“You got it. The number was”, chosenNum) 
