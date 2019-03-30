import random
randNum = random.randint(1, 100)
numInput = int(input("Please enter a number between 1 and 100: \n"))
while numInput != randNum:
    if (numInput > 100 or numInput < 1):
        print("Over range! Please input again: ")
        numInput = int(input())
    elif numInput > randNum:
        print("Too large! Please input another: ")
        numInput = int(input())
    else:
        print("Too small! Please input another: ")
        numInput = int(input())
print("Congratulations! Your are awesome!")
