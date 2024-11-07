# holbertonschool-hbnb

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

---

This is a Holberton School Project  
**Author**: Alexis Rodriguez Rodriguez  
**Location**: Montevideo, Uruguay  
**Date**: 2024

© 2024 Alexis-Holberton School -- All rights reserved --