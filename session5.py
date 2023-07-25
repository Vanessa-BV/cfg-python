#with open('session5todo.txt', 'r') as todo_file:
#    contents = todo_file.read()
#print(contents)

#with open('session5todo.txt','w+') as todo_file:
#    todo = 'Baking Cooking Cleaning Working\nRunning \nBoxing'
#    todo_file.write(todo)
#
#import csv
#field_names = ['name', 'age']
#data = [
#    {'name': 'Jill', 'age': 32},
#    {'name': 'Sara', 'age': 28},
#]

#with open('trees.csv', 'w+') as csv_file:
#    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

#    spreadsheet.writeheader()
#    spreadsheet.writerows(data)

#with open('trees.csv', 'r') as csv_file:
#    spreadsheet = csv.DictReader(csv_file)
#    for row in spreadsheet:
#        print(dict(row))


import requests
pokemon_number = input("What is the Pokemon's ID?")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])


import requests
pokemon_number = input("What is the Pokemons' ID?")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

moves = pokemon['moves']

for move in moves:
    print(move['move']['name'])