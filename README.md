# Guess The Number
Guess the Number is a simple game made using Python. Your Enemy, the CPU, trys to out smart you letting you learn its pattern while in the end mixing it up and letting you lose.
# How does it work
The Computer randomizes a area where the number will be randomized in.
```python
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
```

Then the Computer randomizes the final number
```python
c = randint(a,b)
```
Then we get the answer from the player
```python
print("Guess the number that I am thinking of. The Number is " + str(a) + "-" + str(b))

while AnswerFound == False:

    d = input("| ")
```

Finally we detect if the answer is correct or incorrect. If it is incorrect we try to find out if it is lower then the answer or higher.
```python

    if d == str(c):

        print("Correct!")
        AnswerFound = True

    else:

        try:

            if round( int(d) ) <= c:

                print("Too Low")

            if round( int(d) ) >= c:

                print("Too High")

            

        except Exception as err:

            print("Please Only Insert Numbers")
            print(str(err))
            exit()
           
```

# To Do

- Add a Points System
- Improve this README
