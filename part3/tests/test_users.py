import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_user_creation_valid():
    '''
    User creation test with valid data.
    '''
    data = {
        "first_name": "Lidia",
        "last_name": "Butterley",
        "email": "lbutterley0@bravesites.com"
    }
    response = requests.post(f"{BASE_URL}/users/", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["first_name"] == "Lidia"
    assert response_data["last_name"] == "Butterley"
    assert response_data["email"] == "lbutterley0@bravesites.com"


def test_user_creation_empty_fields():
    '''
    User creation test with empty fields.
    '''
    data = {
        "first_name": "",
        "last_name": "",
        "email": ""
    }
    response = requests.post(f"{BASE_URL}/users/", json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data

def test_user_creation_invalid_email():
    '''
    User creation test with invalid email.
    '''
    data = {
        "first_name": "Lidia",
        "last_name": "Butterley",
        "email": "lbutterley"
    }
    response = requests.post(f"{BASE_URL}/users/", json=data)
    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data
    assert "email" in response_data
