#!/usr/bin/python3 


def find_the_redheads(family):
    redheads = dict(filter(check_redheads ,family.items()))
    redheads = list(redheads)
    return redheads

def check_redheads(member):
    _name, hair_color = member
    return hair_color == "red"

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))