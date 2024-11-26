import re
from app.models.base import BaseModel
# import bcrypt

class User(BaseModel):
    """A class to represent a user in the application"""
    __emails = set()  # Class-level set to track unique emails

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()  # Call to BaseModel's constructor
        self.first_name = self.validate_firstname(first_name)
        self.last_name = self.validate_lastname(last_name)
        self.email = self.validate_email(email)
        # self.password = password
        self.is_admin = is_admin
        self.places = []  #It saves the places that the user has created
        self.reviews = []  #It saves the reviews that the user has created


        if email not in User.__emails:
            User.__emails.add(email)
        else:
            raise ValueError("Email already registered")

        # if password:
        #     self.hash_password(password)

    @staticmethod
    def validate_firstname(first_name):
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and must be at most 50 characters long.")
        return first_name

    @staticmethod
    def validate_lastname(last_name):
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and must be at most 50 characters long.")
        return last_name

    @staticmethod
    def validate_email(email):
        if not email:
            raise ValueError("Email is required.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("error: Invalid email format")
        return email
    
    # def hash_password(self, password):
    #     """Hashes the password before storing it."""
    #     self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    # def verify_password(self, password):
    #     """Verifies if the provided password matches the hashed password."""
    #     return bcrypt.check_password_hash(self.password, password)

    def add_place(self, place):
        self.places.append(place)
        place.owner = self   # Set the place's owner to this user

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        return f"<User  {self.first_name} {self.last_name}>"
