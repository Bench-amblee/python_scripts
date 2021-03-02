grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']] 
#longer method
a = -1
while a < 9:
    a = a + 1
    print (grid [a] [0], end =" ")
    if a == 8:
        break
print ('')
b = -1
while b < 9:
    b = b + 1
    print (grid [b] [1], end =" ")
    if b == 8:
        break
print ('')
c = -1
while c < 9:
    c = c + 1
    print (grid [c] [2], end =" ")
    if c == 8:
        break
print ('')
d = -1
while c < 9:
    d = d + 1
    print (grid [d] [3], end =" ")
    if d == 8:
        break
print ('')
e = -1
while e < 9:
    e = e + 1
    print (grid [e] [4], end =" ")
    if e == 8:
        break
print ('')
f = -1
while f < 9:
    f = f + 1
    print (grid [f] [5], end =" ")
    if f == 8:
        break
print ('')
#shorter method

print('\n'.join(map(''.join, zip(*grid))))
