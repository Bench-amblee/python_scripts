import sys
spam = ['apples', 'bananas', 'tofu', 'cats']
i = len(spam)
if len(spam) == 0:
    sys.exit
else:
    while i > 0:
        i = i-1
        print(spam[-i-1] + ',', end =" ")
        if i == 1:
            break
    print('and ' + spam[len(spam)-1])
