import requests
import pytest

BASE_URL = "https://api.pokemonbattle.ru/v2/trainers"
TRAINER_ID = "19973"
HEADERS = {
    "Content-Type": "application/json",
    "trainer_token": "1c6c4bae034caea02f93da8564539f99"
}

def test_get_trainers_status_code():
    response = requests.get(BASE_URL, params={"trainer_id": TRAINER_ID}, headers=HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_get_trainer_name_in_response():
    response = requests.get(BASE_URL, params={"trainer_id": TRAINER_ID}, headers=HEADERS)
    assert response.status_code == 200, "Failed to fetch trainer data"
    
    response_data = response.json()
    trainer_name = "Хаски"
    
    print("\nResponse data:", response_data)

    trainer_list = response_data.get("data", [])
    print("\nTrainer list:", trainer_list) 
    
    found = any(trainer.get("trainer_name") == trainer_name for trainer in trainer_list)
    
    assert found, (
        f"Trainer name '{trainer_name}' not found in response. "
        f"Available trainers: {[trainer.get('trainer_name') for trainer in trainer_list]}"
    )