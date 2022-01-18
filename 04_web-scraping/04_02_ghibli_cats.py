# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

BASE_URL = "https://ghibliapi.herokuapp.com/people"

#find information about all of the cats 

import requests 
from bs4 import BeautifulSoup 
response = requests.get(BASE_URL) 
#soup = BeautifulSoup(page.text) 
#soup_list=[soup.prettify()]
data=response.json()
data_dict={}
list=[]
print("Studio Ghibli Cats:")
"""
for i in data:
     for key,value in i.items():
         if value=="https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3":
            if key=="name":
                dict["name"]=value
            if key=="gender":
                dict["gender"]=value
            if key=="eye_color":
                dict["eye_color"]=value
            if key=="hair_color":
                dict["hair_color"]=value
                print(str(dict.copy()).strip("{}"))
"""
for i in data:
    if i["species"]=="https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3":
            data_dict["name"]=i["name"]
            data_dict["gender"]=i["gender"]
            data_dict["eye_color"]=i["eye_color"]
            data_dict["hair_color"]=i["hair_color"]
            print(data_dict)




#translate code into python basicallyy
#under people
#if species is https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3 then enter url and parse?