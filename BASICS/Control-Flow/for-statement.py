'''
    Python's for statement iterates over the items of any sequence(list or str) in the order that they appear in the sequence.


'''

words = ["cat", "window", "defenestrate"]

for word in words:
    print(word, len(word))

# Code that modifies a collection while looping over that collection can be tricky to get right.
# More staight forward to loop over a copy of the collection or create a new collection.

# Sample collection
users = {"Hans": "active", "Elenore":"inactive", "景太郎":"inactive"}

print(users)
# Create a copy of the collection
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)


# Create new collection
records = {"Alex": "alive", "Ann": "deceased", "Ayub":"deceased"}

print(records)
print(records.items())

death_records = {}

for person, s in records.items():
    if s == 'deceased':
        death_records[person] = s

print(death_records)


alive_records = {}
for p, sta in records.items():
    if sta == "alive":
        alive_records[p] = sta
print(alive_records)

