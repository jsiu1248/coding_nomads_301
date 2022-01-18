# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

url = "https://en.wikipedia.org/wiki/Web_scraping"

import requests 
from bs4 import BeautifulSoup 
page= requests.get(url) 
soup = BeautifulSoup(page.text, "html.parser") 
#print(soup.prettify())
soup_text=soup.prettify()
#with open('html.txt', 'w', encoding="utf8") as f: # trying to write everything to a find to see how it looks



    #f.write(soup_text)
    

all_links = soup.find(id="bodyContent").find_all("a") # tag # returning a resultset hover over
#print(all_links)

for link in all_links:
    if link['href'].find("/wiki/")!=-1: # if it doesn't find it then it would be a -1 # kind of like its own class
            print(f"https://en.wikipedia.org{link['href']}") # they don't look like dictionaries. why can I subset it this way
            #print(type(link)) # class 'bs4.element.Tag'


# extract all of the links
#filter the navigation links
#follow the links to another article
#extract text from article and save to text file
# regex and find all of the numbers
#Category, (identifier), Help:, Wikipedia:, 