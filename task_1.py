import requests

host = 'https://akabab.github.io/superhero-api/api'
url = '/all.json'

response = requests.get(host + url)
hero_dict = response.json()
list_hero_name = ["Hulk", "Captain America", "Thanos"]
int_dict = {}

for elem in hero_dict:
    if elem["name"] in list_hero_name:
        int_dict[elem["name"]] = elem["powerstats"]["intelligence"]
print(max(int_dict))
