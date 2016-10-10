import random

guessesTaken = 0

print("Hello ! What is your name ?")
myName = input()

number = random.randint(1,20)
print("Well!" + myName + " I am thinking of a number between 1 to 20.")
print("You have only 5 chances. Let's try how much potential you have.")

while guessesTaken < 5:
    print("Take a guess")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print("Your guess is lower than my number")

    if guess > number:
        print("Your guess is higher than my number")

    if guess == number:
        break
        
if guess == number:
    guessesTaken = str(guessesTaken) 
    print("Well done! " + myName + " You guessed my number in " + guessesTaken + " chances.")

if guess != number:
    number = str(number)
    print("Sorry " + myName + "! I was thinking of " + number + ". No worry, You can try again.")



