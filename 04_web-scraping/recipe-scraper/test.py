import requests
from bs4 import BeautifulSoup
import pprint
import json
import time
# Extract the title of each recipe and save it as a variable
BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)

soup = BeautifulSoup(page.text)
links = soup.find_all('a')
titles = []
for link in links:
    titles.append(link.text)
# pprint.pprint(titles)

# Extract the text body of each recipe and save it as a variable
pages = [link['href'] for link in links]
recipes = []
for p in pages:
    p1 = requests.get(f'https://codingnomads.github.io/recipes/{p}')
    recipe = BeautifulSoup(p1.text)
    info = recipe.find('div', class_='is-normal')
    # info = recipe.find('div', class_='md')
    recipes.append(info.text)
print(recipes)

# Create the search function
def search_recipes(recipes, ingredients):
    for recipe in recipes:
        if all(ingredient in recipe for ingredient in ingredients):
            print(recipe)

# Do the searching
list_of_ingredients = []
ingredient = input('What ingredient do you have? type "stop" to stop... ')
list_of_ingredients.append(ingredient)
while ingredient != 'stop'.lower():
    ingredient = input('What else? type "stop" to stop... ')
    if ingredient == 'stop'.lower():
        print('searching for recipes...')
        time.sleep(2)
        search_recipes(recipes, list_of_ingredients)
    list_of_ingredients.append(ingredient)