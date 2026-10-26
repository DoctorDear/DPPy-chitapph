#!/usr/bin/env python3

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))

result = firstNum * secondNum
print(str(firstNum) + " x " + str(secondNum) + " = " + str(result))

if result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")