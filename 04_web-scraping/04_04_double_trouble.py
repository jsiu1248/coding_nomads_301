# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

# find all ghosts and ghost pokemon

import requests
from requests.models import Response 
ghost_url = "https://ghibliapi.herokuapp.com/people"
ghost_response = requests.get(ghost_url)
ghost_data=ghost_response.json()
ghost_data_clean={}
ghost_data_list=[]

for i in ghost_data:
  ghost_data_clean["name"]=i["name"]
  ghost_data_list.append(ghost_data_clean.copy()) # need the list because keys can't be duplicated
#print(ghost_data_list)  #also it needs to be copied so that it references and appends the copy every time
#print(len(ghost_data_list))


pokemon_data_clean={}
pokemon_data_list=[]
for j in range(1,len(ghost_data_list)+1):
    url= f"https://pokeapi.co/api/v2/pokemon/{j}"
    pokemon_response = requests.get(url)
    pokemon_data=pokemon_response.json()
    #print(pokemon_data)
    pokemon_data_clean["name"]= pokemon_data["forms"][0]["name"]
    pokemon_data_list.append(pokemon_data_clean.copy()) # need the list because keys can't be duplicated

#print(pokemon_data_list)

merged_list=[]
merged_dict={}





for k in range(len(ghost_data_list)):
  merged_dict["trainer_name"]=ghost_data_list[k]["name"]
  #merged_list.append(merged_dict.copy())
  merged_dict["pokemon_name"]=pokemon_data_list[k]["name"]
  merged_list.append(merged_dict.copy())

print(merged_list)


#merged_list=list(zip(ghost_data_list, pokemon_data_list))

#print(merged_list)
#repeating right and and add better comments

