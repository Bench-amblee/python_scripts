import random
NumberOfStreaks = 0
print('Type "flip" to flip 100 coins 10000 times. The program will count how many times there are 6 instances of tails or heads in a row')
input()
for ExperimentNumber in range(10000): #test 10000 times
    #flip 100 coins
    Trials = 101
    Results = []
    while Trials > 0:
        Trials = Trials - 1
        Coin = random.randint(0,1)
        if Coin == 0:
            Results.append('H' )
        if Coin == 1:
            Results.append('T' )

    for i in range(len(Results)):
        if i == 0:
            streak = 0
        elif Results[i] == Results[i-1]:
                streak += 1
        else:
            streak = 0
        if streak == 6:
            NumberOfStreaks += 1

print('Total number of 6 streaks: ' + (str(int(NumberOfStreaks))))
print('Probability of Heads/Tails 6 in a row: %s%%' % (NumberOfStreaks / (100)))
