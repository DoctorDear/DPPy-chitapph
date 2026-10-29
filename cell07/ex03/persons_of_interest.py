#!/usr/bin/python3 

def famous_births(scientists):
    sorted_scientists = sorted(scientists.values(), key=get_birth_year)

    for scientist in sorted_scientists:
        print(f"{scientist['name']} is a great scientist born in {scientist['date_of_birth']}.")


def get_birth_year(scientist):
    return int(scientist["date_of_birth"])

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)