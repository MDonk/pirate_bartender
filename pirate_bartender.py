import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def style():
    preferences = {}
    for key, value in questions.items():
        answer = input(value)
        preferences[key] = (answer == "y" or answer == "yes")
    return preferences

def drink(preferences):
    drink_it = []
    for key, value in preferences.items():
        if value is True:
            drink_it.append(random.choice(ingredients[key]))
    print(drink_it)
    return drink_it

if __name__ == '__main__':
    style()
    drink(preferences)