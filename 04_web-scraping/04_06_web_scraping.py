# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

#view-source:https://lyricstranslate.com/en/hacken-lee-%E4%B8%80%E7%94%9F%E4%B8%8D%E5%8F%98-yat-sang-bat-bin-lyrics.html
#https://mojim.com/cny100040x90x1.
#https://www.smule.com/song/%E6%9D%8E%E5%85%8B%E5%8B%A4-hacken-lee-c3po-%E6%9D%8E%E5%85%8B%E5%8B%A4-hacken-lee-karaoke-lyrics/551319248_2742820/arrangement
 
#https://mojim.com/cnh100040.htm 
# all the song
from posixpath import join
import requests
from bs4 import BeautifulSoup 
import json
import os
import re

# figure out how to get links with chinese characters
#just one page
"""
url = "https://mojim.com/cny100040x90x1"
page= requests.get(url) 
soup = BeautifulSoup(page.text, "html.parser") 
soup_text=soup.prettify()
#print(soup_text)
#all_text = soup.find("div",{"class":"1frabae"})
all_text = soup.find("div",id="fsZ")
print(all_text.text)
"""

#trying to get all of the songs
url = "https://mojim.com/cnh100040.htm"
mojo="mojim.com"
link_list=[]
page= requests.get(url) 
soup = BeautifulSoup(page.text, "html.parser") 
soup_text=soup.prettify()
#print(soup_text)
all_text = soup.find_all("span",class_="hc3")
for i in all_text:
        all_text_v2=i.find("a")
        if all_text_v2 is not None:
            link_list.append(all_text_v2.get('href')) #<class 'bs4.element.Tag'>
            #print(all_text_v2)

for j in link_list:
    url= f"http://mojim.com{j}"
    page= requests.get(url) 
    soup = BeautifulSoup(page.text, "html.parser") 
    soup_text=soup.prettify()
    #print(soup_text)
    #all_text = soup.find("div",{"class":"1frabae"})
    all_text = soup.find("div",id="fsZ")
    print(all_text.text)


#print(link_list)

#[<span class="hc3">歌曲列表</span>,span class="hc3">1.<a href="/cny100040x103x1.htm" title="为食熊猫 歌词">为食熊猫</a></span>, <span
#<a href="/cny100040x26x1.htm" title="夏日之神话 歌词">夏日之神话</a>

#TODO 
#maybe save data later