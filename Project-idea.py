import requests

def recipe_search(ingredient, mealType, Health):
    app_id = '499e33b4'
    app_key = '645541f04fffb0d263c3c9d9fbca2b06'
    if Health == 'none':
        url = 'https://api.edamam.com/search?q={}&mealType={}&app_id={}&app_key={}'.format(ingredient, mealType, app_id,app_key)
    else:
        url = 'https://api.edamam.com/search?q={}&mealType={}&health={}&app_id={}&app_key={}'.format(ingredient, mealType, Health, app_id,app_key)
    result = requests.get(url)
    data = result.json()
    return data['hits']

def run():
    #Ask user to enter an ingredient
    ingredient = input('Enter an ingredient: ')

    #Ask user for mealtype (breakfast, lunch, dinner)
    mealType = input('Would you like breakfast, brunch, lunch, dinner, snack, teatime? ')

    #Ask user if they have any dietary requirements
    Health = input("Do you have dietary requirements? E.g. none, vegan, vegetarian, dairy-free, kosher, gluten-free, paleo, low-sugar, soy-free: ")

    no_health = recipe_search(ingredient, mealType, 'none')
    health_result = recipe_search(ingredient, mealType, Health)

#filter dietary requirements:
    if Health == 'none':
        results = no_health
    else:
        results = health_result

    with open('recipes.txt', 'w', encoding='utf-8') as file:
        for result in results:
            recipe = result['recipe']
            file.write(recipe['label'] + '\n')
            file.write(recipe['url'] + '\n')
            file.write('Ingredients:\n')
            for ingredient in recipe['ingredientLines']:
                file.write('- ' + ingredient+ '\n')
            file.write('\n')


run()