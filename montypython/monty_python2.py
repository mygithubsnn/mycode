#!/usr/bin/python3

"""" while and if loop n"""


respons = " "
count = 0 

while count < 3 and respons != "brian":
    count += 1
    respons = input("please enter your guess: ")
    if respons.lower() == "brian":
        print("Correct!")
        break
    elif count == 3:
        print("sorry, the answer was Brian")
        break
    else:
        print('sorry, try again')



