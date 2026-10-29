#!/usr/bin/python3 


def find_the_redheads(family):
    list(filter(check_redheads ,family.items()))
    

def check_redheads(member):
    print(member)
    name, hair_color = member
    return hair_color == "red"

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

find_the_redheads(dupont_family)