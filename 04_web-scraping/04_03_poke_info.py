# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5




import requests 
from bs4 import BeautifulSoup 
 
file = open("pokemon.html","w")
#soup_list=[soup.prettify()]
pokemon_data={}
for i in range(1,8):
    url= f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    data=response.json()
    #print(pokemon_data)
    pokemon_data["name"]= data["forms"][0]["name"]
    pokemon_data["id"]= data["id"]
    pokemon_data["types"]= data["types"][0]["type"]["name"]
    print(pokemon_data)
    pokemon_data_string=str(pokemon_data) # have to rename it for some reason
    print(pokemon_data_string)
    file.write(f"{pokemon_data_string} \n")


file.close()