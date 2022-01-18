# Build a very basic Pokémon class that allows you to simulate battles
# in a fire-water-grass game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on fire-water-grass that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


#feed the pokemon and then regain

import requests
import random
import time
import os
import json

#extract the data
"""
# this data has to be written to a file and then save until later

file  = open("pokemon.txt", "w+")

pokemon_data={}
pokemon_data_list=[]
for i in range(1,8):
    url= f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    data=response.json()
    if data["types"][0]["type"]["name"] in ["grass","fire","water"]:
        pokemon_data["name"]= data["forms"][0]["name"]
        pokemon_data["id"]= data["id"]
        pokemon_data["types"]= data["types"][0]["type"]["name"]
        pokemon_data['max_hp']=data["stats"][0]["base_stat"]
        pokemon_data_list.append(pokemon_data.copy())
print(pokemon_data_list)

file.write(f"{pokemon_data_list}")
"""

#load the data

file_path=os.path.dirname(__file__)
#print(file_path)
file_path_pokemon=os.path.join(file_path)
#C:\Users\jsiu\Documents\codingnomads\python-301-main_jsiu\python-301-main\projects
paths=os.path.join(file_path_pokemon,'pokemon.json')
#file_read=open(paths, 'r')

pokemon_file=open(paths)
pokemon_data_load = json.load(pokemon_file)
print(pokemon_data_load)
# jsons have to be in double quotes

pokemon_list=[]
pokemon_dict={}
pokemon_list_2=[]

for pokemon in pokemon_data_load:
    pokemon_list.append(pokemon["name"])
    #pokemon_dict[pokemon["name"]]=pokemon["types"]
    #pokemon_list_2.append([pokemon["name"], pokemon["types"],pokemon["max_hp"]])
    # pokemon_dict["name"]=pokemon["name"]
    # pokemon_dict["types"]=pokemon["types"]
    # pokemon_dict["max_hp"]=pokemon["max_hp"]
    pokemon_dict[pokemon["name"]]=[pokemon["types"],pokemon["max_hp"]]
print(pokemon_list)
print(pokemon_dict)
print(pokemon_list_2)

#select random pokemon
human_pokemon=random.choice(pokemon_list)
computer_pokemon=random.choice(pokemon_list) # number of pokemon choices?

#user_pokemon=random.choice(pokemon_list)

# print(user_pokemon)

class Pokemon:
    def __init__(self, user_pokemon):
        self.name=user_pokemon
        self.types=pokemon_dict[self.name][0]
        self.hp=pokemon_dict[self.name][1]

    #should their health be outside of the battle and feed method them?
    #pokemon hp class?
    #hm I guess each pokemon has its own hp


    #human_hp=max_hp #pokemon
    #computer_hp=max_hp # computer pokemon

#redudant # use attributes # get pokemon objects and not tuple objects
    def get_info(self):
        if self.name in pokemon_dict: #{bulb:grass} how to turn into {name:bulb, }
            self.types=pokemon_dict[self.name][0]
            self.max_hp=pokemon_dict[self.name][1]
            return  self.types, self.name, self.max_hp

    # def get_info(self):
    #     if user_pokemon in pokemon_dict: #{bulb:grass} how to turn into {name:bulb, }
    #         self.type=pokemon_dict[user_pokemon][0]
    #         self.max_hp=pokemon_dict[user_pokemon][1]
    #         return  self.type, user_pokemon, self.max_hp


    @staticmethod
    def battle(human, computer):
        human_hp=human[2]
        computer_hp=computer[2]
        #instance of a class and list then have states
        #as long as you pass it in order
        if human[0]=="fire" and computer[0]=="water":
            print(f"{human[1]} is {human[0]} loses to {computer[1]} is {computer[0]}. Computer wins! ")
            human_hp=human_hp-10
            print(human_hp)
            return human_hp
            if human_hp==0:
                print("Human lost the battle")


            #need counter for human health and computer health
            #Round 1 
            #take human max_hp and minus 10 
            #computer is max_hp
            # Round 2
            # take computer max_hp and minus 10
            # Round 3
            # take human that has minus 10 and minus 10 again 
        if human[0] == "water" and computer[0] == "fire":
            print(f"{human[1]} is {human[0]} beats {computer[1]} is {computer[0]}. Human wins! ")
            computer_hp=computer_hp-10
            print(computer_hp)
            return computer_hp

            if computer_hp==0:
                print("Computer lost the battle")
        if human[0] == "water" and computer[0] == "grass":
            print(f"{human[1]} is {human[0]} loses to {computer[1]} is {computer[0]}. Computer wins! ")
            human_hp=human_hp-10
            print(human_hp)
            return human_hp
            if human_hp==0:
                print("Human lost the battle")

        if human[0] == "grass" and computer[0] == "water":
            print(f"{human[1]} is {human[0]} beats {computer[1]} is {computer[0]}. Human wins! ")
            computer_hp=computer_hp-10
            print(computer_hp)
            return computer_hp
            if computer_hp==0:
                print("Computer lost the battle")

        if human[0] == "fire" and computer[0] == "grass":
            print(f"{human[1]} is  {human[0]} beats {computer[1]} is {computer[0]}. Human wins! ")
            computer_hp=computer_hp-10
            print(computer_hp)
            return computer_hp
            if computer_hp==0:
                print("Computer lost the battle")

        if human[0] == "grass" and computer[0] == "fire":
            print(f"{human[1]} is {human[0]} loses to {computer[1]} is {computer[0]}. Computer wins! ")
            human_hp=human_hp-10
            print(human_hp)
            return human_hp
            if human_hp==0:
                print("Human lost the battle")

        if human[0] == "water" and computer[0] == "water":
            print(f"{human[1]} is {human[0]} and {computer[1]} is {computer[0]} are the same. It is a draw! ")
        if human[0] == "fire" and computer[0] == "fire":
            print(f"{human[1]} is {human[0]} and {computer[1]} is {computer[0]} are the same. It is a draw! ")
        if human[0] == "grass" and computer[0] == "grass":
            print(f"{human[1]} is {human[0]} and {computer[1]} is {computer[0]} are the same. It is a draw! ")

computer_info=Pokemon(computer_pokemon).get_info()
human_info=Pokemon(human_pokemon).get_info()
#print(computer_info.get_info())
#print(human_info.get_info())

print(computer_info)
print(human_info)

Pokemon.battle( human_info, computer_info)
#human_info=Pokemon.get_info(user_pokemon)
    #print(computer_type)
    #print(human_type)

#print(Pokemon.battle(human_info, computer_info))
