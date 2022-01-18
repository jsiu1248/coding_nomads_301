# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.


import pytest

url = "https://en.wikipedia.org/wiki/Web_scraping"

import requests 
from bs4 import BeautifulSoup 
#import unittest
class Wiki():
    def __init__(self):
        pass
    def pull_data(self):
        self.page= requests.get(url) 
        self.soup = BeautifulSoup(self.page.text, "html.parser") 
        #print(soup.prettify())
        self.soup_text=self.soup.prettify()
        #with open('html.txt', 'w', encoding="utf8") as f: # trying to write everything to a find to see how it looks



            #f.write(soup_text)
            

        self.all_links = self.soup.find(id="bodyContent").find_all("a") # tag # returning a resultset hover over
        #print(all_links)

        self.link_list=[]
        for link in self.all_links:
            if link['href'].find("/wiki/")!=-1: # if it doesn't find it then it would be a -1 # kind of like its own class
                    self.link_list.append(f"https://en.wikipedia.org{link['href']}") # they don't look like dictionaries. why can I subset it this way
        print(self.link_list)
# w=Wiki()
# w.pull_data()
# class test_clean(unittest.TestCase):
    # def __init__(self):
    #     pass
def test_clean_is_not_none():
    w=Wiki()
    w.pull_data()
    # fixtures - ways of setting up the environment
    #configs for flask, test the object
    for i in w.link_list:
        pytest.assertIsNotNone(i) #see that we changed the column at least know that there is a change
def test_values():
    w=Wiki()
    w.pull_data()
    for i in w.link_list:
        pytest.assertIn("https:", i) #testing 0 not in s_1_clean

#try visiting links
def test_html_working():
    w=Wiki()
    w.pull_data()
    for i in w.link_list:
        response=requests.get(i)
        # print(response.status_code)
        if response.status_code=="404":
            print(i)
        pytest.assertEqual(response.status_code,"404")

# if __name__ == "__main__":
pytest.main()