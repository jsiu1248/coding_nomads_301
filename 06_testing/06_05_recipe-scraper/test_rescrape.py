# Write a unittest test suite to test the rescrape module

import unittest
import rescrape
import requests
from bs4 import BeautifulSoup 



x=rescrape.get_author("https://codingnomads.github.io/recipes/")
print(type(x))
"""
class test_rescrape(unittest.TestCase):
    def test_clean_html_content(self):
        self.assertIsNotNone(rescrape.get_html_content)
    #def test_clean_int(self):
    def test_get_author(self):
        self.assertIsNotNone(rescrape.get_author)
    def test_get_recipe(self):
        self.assertIsNotNone(rescrape.get_recipe)
    def test_get_recipe_links(self):
        self.assertIsNotNone(rescrape.get_recipe_links)
        assert isinstance(rescrape.get_recipe_links, str)



if __name__ == '__main__':
    unittest.main()


"""


