theBoard = {'top-left': ' ', 'top-middle': ' ', 'top-right': ' ', 'mid-left': ' ', 'mid-middle': ' ', 'mid-right': ' ', 'low-left': ' ', 'low-middle': ' ', 'low-right': ' '}

def printboard(board): #grid design
    print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
    print('-+-+-')
    print(board['mid-left'] + '|' + board['mid-middle'] + '|' + board['mid-right'])
    print('-+-+-')
    print(board['low-left'] + '|' + board['low-middle'] + '|' + board['low-right'])
turn = 'X' #player 1
for i in range(9):
    printboard(theBoard)
    print('Turn for ' + turn + ' Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn =='X':
        turn = '0' #player 2
    else:
        turn = 'X'
printboard(theBoard)
input()
