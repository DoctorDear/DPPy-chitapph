#!/usr/bin/python3

def add_one(x):
    x += 1
    return x

def main():
    my_var = 42 #pass by value, the value of my_var is copied to x in add_one
    print(my_var)
    add_one(my_var)
    print(my_var)
    my_var = add_one(my_var) #reassigning the return value of add_one to my_var
    print(my_var)
main()
    
