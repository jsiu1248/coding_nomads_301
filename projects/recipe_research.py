# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

#Ingredients class
# look for recipes made from ingredients
#url search

# https://platform.codingnomads.co/learn/mod/page/view.php?id=6622#


# Implement the Ingredient() class, where each ingredient has at least a .name and an .amount attribute.
# Add an instance method called .get_info() that takes the .name attribute of an Ingredient() and creates a Wikipedia URL.
# The .get_info() method should then automatically open the corresponding Wikipedia page in your web browser:
#https://en.wikipedia.org/wiki/Carrot
#https://docs.python.org/3/library/webbrowser.html

from posixpath import join
import requests
from bs4 import BeautifulSoup 
import webbrowser



class Ingredients():
    def __init__(self):
        self.ingredient=input("What ingredients do you want in your recipe?")
    
    def get_info(self):
        wiki="https://en.wikipedia.org/wiki/"
        website_link=join(wiki, self.ingredient)
        webbrowser.open_new_tab(website_link)


Ingredients().get_info()