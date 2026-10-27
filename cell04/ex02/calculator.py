#!/usr/bin/env python3

firstNum = int(input("Give me the first number: "))
secondNum = int(input("Give me the second number: "))
print("Thank you!")
# print(f"{firstNum} + {secondNum} = {int(firstNum + secondNum)}")
# print(f"{firstNum} - {secondNum} = {int(firstNum - secondNum)}")
# print(f"{firstNum} / {secondNum} = {int(firstNum / secondNum)}")
# print(f"{firstNum} * {secondNum} = {int(firstNum * secondNum)}")

result = [
    ("+", firstNum + secondNum), #tuple of operator and result
    ("-", firstNum - secondNum),
    ("/", int(firstNum / secondNum)),
    ("*", firstNum * secondNum) 
]
print(result[3])
for operator, value in result:
    print(operator)
    print(value)
    print(f"{firstNum} {operator} {secondNum} = {value}")