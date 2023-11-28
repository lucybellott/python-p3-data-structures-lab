spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_values = [food['name'] for food in spicy_foods]
    return spicy_values

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food['heat_level']
        avg = total / len(spicy_foods)
    return avg

    #or eturn sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append({'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10,})
    return spicy_foods

