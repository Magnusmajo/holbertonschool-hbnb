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

@pytest.fixture(scope="module")
def create_place(create_user, create_amenity):
    """
    Fixture to create place and get id.
    """
    data = {
        "title": "Casa de Prueba",
        "description": "Lugar para prueba de reviews",
        "price": 100.00,
        "latitude": 40.0,
        "longitude": -70.0,
        "owner_id": create_user,
        "amenities": [create_amenity]
    }
    response = requests.post(f"{BASE_URL}/places/", json=data)
    return response.json()["id"]

def test_review_creation_valid(create_place, create_user):
    """
    Create a valid review.
    """
    data = {
        "text": "Lugar excelente, me gustó mucho.",
        "rating": 5,
        "place_id": create_place,
        "user_id": create_user
    }
    response = requests.post(f"{BASE_URL}/reviews/", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["text"] == "Lugar excelente, me gustó mucho."

def test_review_creation_empty_text(create_place, create_user):
    """
    Create a review with empty text.
    """
    data = {
        "text": "",
        "rating": 5,
        "place_id": create_place,
        "user_id": create_user
    }
    response = requests.post(f"{BASE_URL}/reviews/", json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data

def test_review_creation_invalid_user_id(create_place):
    """
    Create a invalid review with invalid user_id.
    """
    data = {
        "text": "Review con usuario inválido.",
        "rating": 5,
        "place_id": create_place,
        "user_id": "invald_id"
    }
    response = requests.post(f"{BASE_URL}/reviews/", json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data

def test_review_creation_invalid_place_id(create_user):
    """
    Create a invalid review with invalid place_id.
    """
    data = {
        "text": "Review con lugar inválido.",
        "rating": 5,
        "place_id": "invalid_id",
        "user_id": create_user
    }
    response = requests.post(f"{BASE_URL}/reviews/", json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data
