import random

number = random.randrange(1,10,2)

print (number)
while True :
    try:
        #input to validate
        response = int(input("Pick a Number 1 - 10? \t"))
    except ValueError:
        print("Please enter a number!")
        #better try again... Return to the start of the loop

        continue
    else:
        #we're ready to exit the loop.
        break

if number == response :
    print (" You got it")

elif number > response :
    print("Its greater than", response)

elif number < response :
     print("Its less than", response)

