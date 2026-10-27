#!/usr/bin/env python3
# ageInput = int(input("Please tell me your age: "))
# print(f"You are currently {ageInput} years old.")
# print(f"In 10 years, you'll be {ageInput + 10}.")
# print(f"In 20 years, you'll be {ageInput + 20}.")
# print(f"In 30 years, you'll be {ageInput + 30}.")

def show_future_age(age):
    print(f"You are currently {age} years old.")
    for years in range(10, 31, 10): # range(start, stop, step)
        print(f"In {years} years, you'll be {age + years}.")
        
ageInput = int(input("Please tell me your age: "))
show_future_age(ageInput)