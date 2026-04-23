# There are a number of compound data types in Python.

# They are used to group together values.

# The most versatile compound data  type is the list.

# It is written as a list of comma separated values (items) between square brackets. 

# Lists might contain items of different types.

# Usually lists have items of the same type, but this is not a requirement.

squares = [1,4, 9, 16, 25]

print(squares)


'''
All built in sequence types can be indexed and sliced including lists and strings.
'''
print(squares[0]) # Indexing returns the item at that position/index
print(squares[1])
print(squares[-1])
print(squares[-2])


print(squares[1:3]) # Slicing returns a new list

print(squares[-1:])
print(squares[-3:])

# Lists also support concatenation
print(squares + [36, 49, 64, 81, 100])


# Strings are immutable, lists are mutable meaning their content can be changed
cubes = [1, 8, 27, 65, 125] # change the cube of 4 to 64
cubes[3] = 64
print(cubes)

# You can also add new items to the end of a list using list.append()
cubes.append(216)
print(cubes)

cubes.append(7 ** 3)
print(cubes)


# print(8 ** 2)
# print(8 ** 3)


'''
    Simple assignment in Python never copies data.
    When you assign a list to a variable, the variable refers to the existing list.
    When you make changes to the list through one variable, will affect all variables that refer to the same list.
'''
rgb = ['red', 'green', 'blue']
# print(rgb)

# Assign another variable rgb
rgba = rgb
# print(rgba)

# Check if both variables reference the same object
print(id(rgb))
print(id(rgba))
print(rgb is rgba) # True because both variables reference the same list object in memory

# Try to make changes to the list through one variable.
rgba.append('alpha')
print(rgb)
print(rgb is rgba) # Still True because both variables reference the same list object in memory

rgb[0] = "cyan"
print(rgba) # Changes made through rgb are reflected in rgba because both variables reference the same list object in memory


# Slice operations return a new list containing the requested elements.
# The below slice returns a shallow copy of the list, which is a new list object that contains references to the same elements as the original list.
print(rgba)
corrected_rgba = rgba[:]
print(corrected_rgba)
corrected_rgba[0] = "Red"
print(corrected_rgba)
print(rgba)


# Built in function len() also applies to lists and returns the number of items in the list.
letters = ['a', 'b', 'c', 'd']
print(len(letters))


# Lists can be nested
# You can create lists containing other lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][2])
