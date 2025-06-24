myList = ["bsjdnfsnf", 12, 13 -126.125, 0, True, "mdbfm"]

print(len(myList)) 

myList.append("yulia") 

myList.insert(0, "apple")

myList.pop()

print(myList)

for t in myList:
    if t == 12:
        print(t)

numbers = []
for i in range(1, 12):
    if i % 4 == 0:
        numbers.append(i)

print(numbers)

numbers = [i for i in range(1, 12) if i % 2 == 0]
print(numbers)

for index, item in enumerate(myList, start=52):
    print(f"{index} - {item}")
