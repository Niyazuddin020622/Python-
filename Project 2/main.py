import random

n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    n = int(input("Guess the Number:  "))
    if(a > n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please:")
        guesses +=1

print(f"You have guessed the number correctly in {guesses} attempt")


