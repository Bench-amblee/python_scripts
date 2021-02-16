# this is a guess the number game.
import random
SecretNumber = random.randint(1,20)
print ('GUESSING GAME')
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('take a guess.')
    guess = int(input())

    if guess < SecretNumber:
        print('Your guess is too low')
    elif guess > SecretNumber:
        print('Your guess is too high.')
    else:
        break
if guess == SecretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(SecretNumber))
# Guessing game over
