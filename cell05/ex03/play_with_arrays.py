#!/usr/bin/env python3

originalArr = [2, 8, 9, 48, 8, 22, -12, 2]
newArr = []
for x in originalArr:
    if x > 5:
        newArr.append(x + 2)

newSet = set(newArr)

print(originalArr)
print(newSet)
