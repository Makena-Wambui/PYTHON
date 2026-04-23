x = int(input("Please enter an integer: "))

'''
    There can be zero or more elif parts
    The else pat is optional. 
'''


if x < 0:
    x = 0
    print(x)
    print('Negative changed to 0.')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
