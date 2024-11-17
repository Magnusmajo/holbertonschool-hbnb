import re
from app.models.base import BaseModel
import bcrypt

class User(BaseModel):
    """A class to represent a user in the application"""
    __emails = set()  # Class-level set to track unique emails

    def __init__(self, first_name, last_name, email, is_admin=False, password=None):
        super().__init__()  # Call to BaseModel's constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        self.places = []  #It saves the places that the user has created

        if password:
            self.hash_password(password)

    @staticmethod
    def validate_firstname(self, first_name):
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and must be at most 50 characters long.")
        return first_name

    @staticmethod
    def validate_lastname(self, last_name):
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and must be at most 50 characters long.")
        return last_name

    @staticmethod
    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format: Invalid email format")
        return email
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def add_place(self, place):
        self.places.append(place)
        place.owner = self   # Set the place's owner to this user

    def __repr__(self):
        return f"<User  {self.first_name} {self.last_name}>"
