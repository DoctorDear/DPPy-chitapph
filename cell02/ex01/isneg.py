#!/usr/bin/env python3

numInput = int(input())
if numInput < 0:
    print("This number is negative.")
elif numInput == 0:
    print("This number is both positive and negative.")
else:
    print("This number is positive.")