# Rock Paper Scissors
import random, sys
print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties' %(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        PlayerMove = input()
        if PlayerMove == 'q':
            sys.exit()
        if PlayerMove == 'r' or PlayerMove == 'p' or PlayerMove == 's':
            break
        print('Type one of r, p, s or q')

    # Display what the player chose
    if PlayerMove == 'r':
        print('ROCK versus...')
    elif PlayerMove == 'p':
        print('PAPER versus...')
    elif PlayerMove == 's':
        print('SCISSORS versus...')

    #Display what the computer chose
    RandomNumber = random.randint(1,3)
    if RandomNumber == 1:
        ComputerMove = 'r'
        print('ROCK')
    elif RandomNumber == 2:
        ComputerMove = 'p'
        print('PAPER')
    elif RandomNumber == 3:
        ComputerMove = 's'
        print('SCISSORS')

    #Record win loss tie results
    if PlayerMove == ComputerMove:
        print('Tie')
        ties = ties + 1
    elif PlayerMove == 'r' and ComputerMove == 's':
        print('You win!')
        wins = wins + 1
    elif PlayerMove == 'p' and ComputerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif PlayerMove == 's' and ComputerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif PlayerMove == 'r' and ComputerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif PlayerMove == 'p' and ComputerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif PlayerMove == 's' and ComputerMove == 'r':
        print('You lose!')
        losses = losses + 1
