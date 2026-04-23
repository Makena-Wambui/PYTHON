'''
    Fibonacci series:
        A sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, and so on.
'''

"""
    In this first line, we have multiple assignment.
    The variables a and b simultaneously get the values 0 and 1
"""
a, b = 0, 1


"""
    While loop executes as long as the condition remains true
    Condition: a is less than or equal to 10

    Body of the loop is indented
"""
while a <= 10:
    print(a, end=", ") 
    '''
        This function writes the value of the args it is given.

        You can pass the keyword argument end to print() to avoid the new line after the output or to end the output with a different string
    '''
    a, b = b, a + b
    
