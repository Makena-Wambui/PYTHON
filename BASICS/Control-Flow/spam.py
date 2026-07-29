spam = 0  # we set the variable spam to 0

if (
    spam == 10
):  # check if spam is equal to 10 -> False so everything inside this if block is skiped
    print("eggs")
    if spam > 5:
        print("bacon")
    else:
        print("ham")
    print("spam")
print("spam")  # This line always runs no matter what because it is outside the if block
