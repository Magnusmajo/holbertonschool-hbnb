import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture(scope="module")
def create_user():
    """
    Fixture to create user and get id.
    """
    data = {
        "first_name": "Anna",
        "last_name": "Robinson",
        "email": "anna@bravesites.com"
    }
    response = requests.post(f"{BASE_URL}/users/", json=data)
    return response.json()["id"]

@pytest.fixture(scope="module")
def create_amenity():
    """
    Fixture to create amenity and get id.
    """
    data = {
        "name": "wifi"
    }
    response = requests.post(f"{BASE_URL}/amenities/", json=data)
    return response.json()["id"]

def test_place_creation_valid(create_user, create_amenity):
    """
    Place creation test with valid data.
    """
    data = {
        "title": "Hermosa Casa",
        "description": "Lugar tranquilo con una gran vista",
        "price": 150.00,
        "latitude": 45.0,
        "longitude": -70.0,
        "owner_id": create_user,  # Replace with valid owner_id
        "amenities": [create_amenity]  # Replace with valid amenity id
    }
    response = requests.post(f"{BASE_URL}/places/", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == "Hermosa Casa"
    assert response_data["price"] == 150.00
    assert -90 <= response_data["latitude"] <= 90
    assert -180 <= response_data["longitude"] <= 180

def test_place_creation_invalid(create_user, create_amenity):
    """
    Place creation test with invalid data.
    """
    data = {
        "title": "",
        "description": "Lugar tranquilo con una gran vista",
        "price": -150.00,
        "latitude": 95.0,
        "longitude": -200.0,
        "owner_id": create_user,  # Replace with valid owner_id
        "amenities": [create_amenity]  # Replace with valid amenity id
    }
    response = requests.post(f"{BASE_URL}/places/", json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data
