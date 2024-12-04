import requests

HEADERS = {
    "Content-Type": "application/json",
    "trainer_token": "1c6c4bae034caea02f93da8564539f99"
}

BASE_URL_CREATE = "https://api.pokemonbattle.ru/v2/pokemons"
create_pokemon_payload = {
    "name": "generate",
    "photo_id": "-1"
}

response_create = requests.post(BASE_URL_CREATE, headers=HEADERS, json=create_pokemon_payload)

print("Создание покемона:")
print(response_create.json())

# Обернул pokemon_id в переменную, взяв id из ответа json 
pokemon_id = response_create.json()['id']
print(f"Создан покемон с ID: {pokemon_id}")


BASE_URL_UPDATE = "https://api.pokemonbattle.ru/v2/pokemons"
update_pokemon_payload = {
    "pokemon_id": str(pokemon_id),
    "name": "pytest",
    "photo_id": "-1"
}

response_update = requests.put(BASE_URL_UPDATE, headers=HEADERS, json=update_pokemon_payload)
print("\nСмена имени покемона:")
print(response_update.json())


BASE_URL_CATCH = "https://api.pokemonbattle.ru/v2/trainers/add_pokeball"
catch_pokemon_payload = {
    "pokemon_id": str(pokemon_id)
}

response_catch = requests.post(BASE_URL_CATCH, headers=HEADERS, json=catch_pokemon_payload)
print("\nПоймать покемона в покебол:")
print(response_catch.json())

# Допом прописал нокаут покемона, чтобы не было проблем с количеством живых, количеством в покеболе
BASE_URL_KNOCKOUT = "https://api.pokemonbattle.ru/v2/pokemons/knockout"
knockout_pokemon_payload = {
    "pokemon_id": str(pokemon_id)
}

response_knockout = requests.post(BASE_URL_KNOCKOUT, headers=HEADERS, json=knockout_pokemon_payload)
print("\nОтправить покемона в нокаут:")
print(response_knockout.json())