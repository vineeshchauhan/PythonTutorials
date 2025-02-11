names = ['John', 'Bob', ' Mosh', 'Sarah', "Mary"]

print(names)

print(names[-1])

print(names[2:4])

print(names[:])


names = [3,4,5,2,7,54,23,45,656,67,78,3,23,2,1]
largest = names[0]
for num in names:
    if num > largest:
        largest = num
print(largest)

names.insert(2,155)
print(names)

print(5 in names)


print(names.sort())

print(names)

for item in names:
    if item in names:
        names.remove(item)

print(names)