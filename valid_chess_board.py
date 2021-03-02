whitePieces = ['wking','wqueen','wrook','wknight','wbishop','wpawn']
blackPieces = ['bking','bqueen','brook','bknight','bbishop','bpawn']
chessBoard = {'1a': '', '1b': '', '1c': '', '1d': '', '1e':'','1f':'','1g':'','1h':'', \
'2a': '', '2b': '', '2c': '', '2d': '', '2e':'','2f':'','2g':'','2h':'', \
'3a': '', '3b': '', '3c': '', '3d': '', '3e':'','3f':'','3g':'','3h':'', \
'4a': '', '4b': '', '4c': '', '4d': '', '4e':'','4f':'','4g':'','4h':'', \
'5a': '', '5b': '', '5c': '', '5d': '', '5e':'','5f':'','5g':'','5h':'', \
'6a': '', '6b': '', '6c': '', '6d': '', '6e':'','6f':'','6g':'','6h':'', \
'7a': '', '7b': '', '7c': '', '7d': '', '7e':'','7f':'','7g':'','7h':'', \
'8a': '', '8b': '', '8c': '', '8d': '', '8e':'','8f':'','8g':'','8h':''}
print('What piece would you like to move? Please use the format: bking or wqueen for example.')
while True:
    choice = input()
    if choice in whitePieces:
        print('Good choice')
        break
    elif choice in blackPieces:
        print('Good choice')
        break
    else:
        print('That is not a valid piece, please enter a valid piece in the format bknight / wpawn')
        continue
print('Where would you like to move your piece on the board? The Chess board ranges from 1a to 8h')
while True:
    X= input()
    if X in chessBoard:
        print('Great!')
        break
    else:
        print('Please enter a valid move like 3b or 4d')
        continue
print('your move is ' + choice + ' ' + X)
