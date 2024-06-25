#!/usr/bin/python3

## The objective of lab is to write a simple guessing program utilizing conditionals. Our simple program will behave in the following manner:

##Ask the user to, Finish the movie title, "Monty Python's The Life of ..."
##Collects up to 3 responses from the user
##Responses to the user's input should include: "Correct!", "Sorry, try again!", and "Sorry, the answer was Brian."##


respons = " "
count = 0 

while count < 3 and respons != "Brian":
    count += 1
    respons = input("please enter your guess: ")
    if respons == "Brian":
        print("Correct!")
        break
    elif count == 3:
        print("sorry, the answer was Brian")
        break
    else:
        print('sorry, try again')



