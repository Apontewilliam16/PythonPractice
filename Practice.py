import random
#Number Guessing Project 
guessesTaken = 0 
number = random.randint(1,10)

while guessesTaken < 5:
    response = int(input("Pick a Number 1 to 10? \t"))

    guessesTaken = guessesTaken +1

    if number > response :
        print("Its greater than", response)
    if number < response :
        print("Its less than", response)

    if number == response :
        break

if response == number:
    guessesTaken = str(guessesTaken)
    print("Nice Work You Guess the Number in " + guessesTaken + "guesses!")

if response != number:
    number = str(number)
    print('Nope. The number I was thinking of was' + number)
       
