# return masked string except for last 4 digits
print ('Enter your code')
cc = input()
def maskify(cc):
    mask = ''
    for char in cc[:-4]:
        mask += '#'
    mask += cc[-4:]
    return mask 
print (maskify(cc))
