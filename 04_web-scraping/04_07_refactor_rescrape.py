# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.




# CLI input of names of ingredients
# fetch the recipe that includes ingredients

from posixpath import join
import requests
from bs4 import BeautifulSoup 
import json
import os
import re
"""
def write_data():
    url = "https://codingnomads.github.io/recipes"
    page= requests.get(url) 
    soup = BeautifulSoup(page.text, "html.parser") 
    soup_text=soup.prettify()
    #print(soup_text)

    all_links = soup.find_all("a")

    link_list=[]
    for link in all_links:
        #if link['href'].find("/wiki/")!=-1: # if it doesn't find it then it would be a -1 # kind of like its own class
        link_list.append(link['href'])
    #print(link_list) # they don't look like dictionaries. why can I subset it this way


    #access the links through loop
    #how to scrap ingredients
    #do I need to take extract and filter out?
    # file  = open("recipe.txt", "w+", encoding="utf-8")

    data_list=[]
    for i in link_list:
        url= f"https://codingnomads.github.io/recipes/{i}"
        link_page= requests.get(url) 
        link_soup = BeautifulSoup(link_page.text, "html.parser") 
        #print(link_soup)
        data_list.append(link_soup)

    recipe_list=[]
    recipe_list_v2=[]
    recipe_list_final=[]

    for i in data_list: # goes through every recipe
        recipe = i.find("div", class_="md")
        recipe_list_final.append(recipe.text)

        # most of the code below tries to filter things down to the ingredients but there was a lot more cleaning needed also 
        # searching a multi level string is quicker than a nested list of strings. 

        # recipe_clean=recipe.find('ul')#.find_all("li")
        # if recipe_clean is not None:
        #     recipe_clean_v2=recipe_clean.find_all("li")
        #     for j in recipe_clean_v2: #goes through each ingredient
        #         if j.string is not None:
        #             recipe_list.append(j.text) #appends all of the ingredients in one recipe #["beef, "egg","hash brown"]
        #         recipe_list_v2.append(recipe_list)
        #         #recipe_list=[]

        # for ingredient in recipe_list_v2:
        #     if ingredient == []:
        #         recipe_list_v2.remove(ingredient)
    #     recipe_list=[]
    # recipe_list_final = []
    # [recipe_list_final.append(x) for x in recipe_list_v2 if x not in recipe_list_final]

    #print(recipe_list_final)
    with open('recipe_data.json', 'w') as fout:
        json.dump(recipe_list_final, fout)
"""

def load_file():
    file_path=os.path.dirname(__file__)
    print(file_path)
    file_path_recipe=os.path.join(file_path)
    #c:\Users\jsiu\Documents\codingnomads\python-301-main_jsiu\python-301-main\04_web-scraping\recipe-scraper
    print(file_path_recipe)

    paths=os.path.join(file_path_recipe, 'recipe_data.json')
    print(paths)
    #dir_path = os.path.dirname(os.path.realpath(__file__)) # gets me the same path as paths, but I'm having permission error
    #print(dir_path)
    with open (paths, 'r') as fin:
        data = json.load(fin)
    # #print(data)
    # # Create the search function
    # ingredient=input("What would you like to cook with?")
    # for i in data:
    #     if ingredient in i:
    #         print(i)


#write_data()
load_file()