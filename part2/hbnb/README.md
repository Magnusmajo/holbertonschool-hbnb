# holbertonschool-hbnb

![Captura de pantalla 2024-11-13 105055](https://github.com/user-attachments/assets/90fe9f96-596a-4d7a-a60d-852a7a6c3b54)

HBnB project for Holberton School

## Project Setup Overview

This project is structured to separate different concerns into distinct directories and files. Below is a brief description of each directory and file:

### Directories and Files

- **app/**: Contains the main application code.
    - **\_\_init\_\_.py**: Initializes the app module.
    - **api/**: Contains the API-related code.
        - **\_\_init\_\_.py**: Initializes the API module.
        - **v1/**: Contains version 1 of the API.
            - **\_\_init\_\_.py**: Initializes the v1 module.
            - **users.py**: Manages user-related API endpoints.
            - **places.py**: Manages place-related API endpoints.
            - **reviews.py**: Manages review-related API endpoints.
            - **amenities.py**: Manages amenity-related API endpoints.
    - **models/**: Contains the data models.
        - **\_\_init\_\_.py**: Initializes the models module.
        - **user.py**: Defines the User model.
        - **place.py**: Defines the Place model.
        - **review.py**: Defines the Review model.
        - **amenity.py**: Defines the Amenity model.
    - **services/**: Contains service layer code.
        - **\_\_init\_\_.py**: Initializes the services module.
        - **facade.py**: Provides a facade for the services.
    - **persistence/**: Contains persistence layer code.
        - **\_\_init\_\_.py**: Initializes the persistence module.
        - **repository.py**: Manages data storage and retrieval.

- **run.py**: The entry point for running the application.
- **config.py**: Contains configuration settings for the application.
- **requirements.txt**: Lists the dependencies required to run the application.
- **README.md**: Provides an overview and documentation for the project.

### Installation Instructions

To install the project, follow these steps:

1. Clone the repository:
     ```sh
     git clone https://github.com/magnusmajo/holbertonschool-hbnb.git
     ```

2. Navigate to the project directory:
     ```sh
     cd holbertonschool-hbnb
     ```

3. Create a virtual environment:
     ```sh
     python3 -m venv env
     ```

4. Activate the virtual environment:
     - On Windows:
         ```sh
         env\Scripts\activate
         ```
     - On macOS/Linux:
         ```sh
         source env/bin/activate
         ```

5. Install the dependencies:
     ```sh
     pip install -r requirements.txt
     ```

6. Run the application:
     ```sh
     python run.py
     ```

This setup will get the application up and running on your local machine.

## Core Business Logic Classes Implementation
The Business Logic layer is responsible for the core functionalities of the application.
It manages the data and the rules that govern the application's behavior. In this layer,
we define various entities that represent the key components of the application.

- **models/base_model.py**: Defines the base class for all models in the application.

#### BaseModel

- Initializes a unique ID using UUID and timestamps for creation and updates.
- Contains a save method to update the updated_at timestamp.
- Includes an update method that allows updating multiple attributes based on a dictionary input.

#### User

- Inherits from BaseModel and adds user-specific attributes.
- Contains the constructor method to define the attributes for the user representation.
- Includes a validator method for the first_name, last_name (validate_name).
- Includes a validator method for the email (validate_email).

#### Example Usage

Below is an example of how to create a new user and handle potential validation errors:

```python
from app.models.user import User

try:
    user1 = User(first_name="", last_name="Myers", email="trap.ups@example.com")
    print(user1)
except ValueError as e:
    print(f"first_name is required and must be at most 50 characters long.: {e}")

try:
    user2 = User(first_name="Anuel", last_name="AA", email="trap.shi@example.com")  # This will raise an error
except ValueError as e:
    print(f"Error creating user: {e}")

try:
    user3 = User(first_name="Sixtinine", last_name="", email="sixtinine.anotherothershi@example.com")
    print(user3)
except ValueError as e:
    print(f"last_name is required and must be at most 50 characters long.: {e}")
    ```

#### Place

- Inherits from BaseModel and adds place-specific attributes.
- Contains the constructor method to define the attributes for the place representation.
- Includes a validator method for the title (Required, maximum length of 100 characters).
- Includes a validator method for the price (Must be a positive value).
- Includes a validator method for the latitude (Must be within the range of -90.0 to 90.0).
- Includes a validator method for the longitude (Must be within the range of -180.0 to 180.0).
- Includes a validator method for the owner (Must be an instance of User, who owns the place).

#### Example Usage

Below is an example of how to create a new place and handle potential validation errors:

```python
from app.models.place import Place
from app.models.user import User

# Create a user instance to be the owner of the place
owner = User(first_name="John", last_name="Doe", email="john.doe@example.com")

try:
    place1 = Place(title="Beautiful Beach House", price=250.0, latitude=34.0522, longitude=-118.2437, owner=owner)
    print(place1)
except ValueError as e:
    print(f"Error creating place: {e}")

try:
    place2 = Place(title="", price=150.0, latitude=34.0522, longitude=-118.2437, owner=owner)  # This will raise an error
except ValueError as e:
    print(f"Error creating place: {e}")

try:
    place3 = Place(title="Mountain Cabin", price=-50.0, latitude=34.0522, longitude=-118.2437, owner=owner)  # This will raise an error
except ValueError as e:
    print(f"Error creating place: {e}")

try:
    place4 = Place(title="City Apartment", price=200.0, latitude=100.0, longitude=-118.2437, owner=owner)  # This will raise an error
except ValueError as e:
    print(f"Error creating place: {e}")
```

#### Review
- Inherits from BaseModel taking the id, created_at and updated_at
- Contains the constructor method to define the attributes for the review representation.
- includes the validation for the required text
- includes the validation for the rating (Must be a positive integer between 0 and 5.)
Includes the User and Place instances to ensure the relationship between them

#### Example Usage

Below is an example of how to create a new review and handle potential validation errors:

```python
from app.models.review import Review
from app.models.user import User
from app.models.place import Place

# Create a user instance to be the author of the review
author = User(first_name="Jane", last_name="Doe", email="jane.doe@example.com")

# Create a place instance to be reviewed
place = Place(title="Cozy Cottage", price=120.0, latitude=45.1234, longitude=-93.1234, owner=author)

try:
    review1 = Review(text="Great place to stay!", rating=5, user=author, place=place)
    print(review1)
except ValueError as e:
    print(f"Error creating review: {e}")

try:
    review2 = Review(text="", rating=4, user=author, place=place)  # This will raise an error
except ValueError as e:
    print(f"Error creating review: {e}")

try:
    review3 = Review(text="Not bad", rating=6, user=author, place=place)  # This will raise an error
except ValueError as e:
    print(f"Error creating review: {e}")

try:
    review4 = Review(text="Could be better", rating=3, user=None, place=place)  # This will raise an error
except ValueError as e:
    print(f"Error creating review: {e}")
```

#### Amenity:

- Inherits from BaseModel.
- Initializes with a name attribute, which is validated to ensure it is not empty and is less than 50 characters.
- Overrides the __repr__ method to return a string representation specific to the Amenity class.
- Contains a save method that updates the updated_at timestamp, although it seems to contain a placeholder comment for saving the amenity.

#### Example Usage

Below is an example of how to create a new amenity and handle potential validation errors:

```python
from app.models.amenity import Amenity

try:
    amenity1 = Amenity(name="Free WiFi")
    print(amenity1)
except ValueError as e:
    print(f"Error creating amenity: {e}")

try:
    amenity2 = Amenity(name="")  # This will raise an error
except ValueError as e:
    print(f"Error creating amenity: {e}")

try:
    amenity3 = Amenity(name="Swimming Pool")
    print(amenity3)
except ValueError as e:
    print(f"Error creating amenity: {e}")
```

---

This is a Holberton School Project  

**Authors**:
- Alexis Rodriguez Rodriguez  
- Bryan Aleman  
- Matthew Hernandez  
**Location**: Montevideo, Uruguay  
**Date**: 2024

© 2024-- All rights reserved --
