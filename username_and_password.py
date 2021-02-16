# Asks for name and password, both inputs need to be correct
while True:
    print('User Name?')
    name = input()
    if name != 'Ben':
        continue
    print('Hello, Ben. What is the password (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
# repeats Yes Sir 7 times after access is granted
for i in range(10):
    print('WELCOME (' + str(i+1) + ')')
# lists 5 random numbers between 1 and 10
import random
for i in range(5):
    print(random.randint(1,10))
