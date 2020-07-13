from random import randint

# Guess the Number
#
# Author: Okistuff
# Date of Creation: June 24, 2020

foundArea = False
AnswerFound = False
points = 0

save = open("saves/save.gtn", "w+")

# Reading the Save File

print(save.readline(6))


# Getting the area of randomization



while foundArea == False:


    a = randint(0, 150)
    b = randint(0, 150)

    

    if a >= b or b <= a:

        pass

    if (a + 2) >= b or (b - 10) >= a:

        # Makes sure that its fair for the player

        pass 

    else:

        foundArea = True

# Getting the number inside the area

c = randint(a,b)

# Asking for User Input

print("Guess the number that I am thinking of. The Number is " + str(a) + "-" + str(b))

while AnswerFound == False:

    d = input("| ")

    if d == str(c):

        print("Correct!")
        AnswerFound = True

        points += 1

        print("You Earned A Point! Want to Play Again?")

    else:

        points -= 1

        try:

            if round( int(d) ) <= c:

                print("Too Low")

            if round( int(d) ) >= c:

                print("Too High")

            

        except Exception:

            print("Please Only Insert Numbers")
    
        print("You Lost 1 Point")

        

