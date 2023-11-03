# create a list by squaring each number
l = [10, 20, 30, 40]
res = []
for num in l:
    res.append(num ** 2)
print(res)

# comprehension
# res = [item_to_be_appended for loop]

res = [num** 2 for num in l]
print(res)

res = [num**2 for num in l]
print(res)

# list of length of names

names = ["steeve", "john", "bob"]

# for loop
res = []
for name in names:
    res.append(len(name))

print(res)

# comprehension
res = [len(name) for name in names]
print(res)