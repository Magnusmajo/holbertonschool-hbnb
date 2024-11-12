import re
from app.models.base import BaseModel

class User(BaseModel):
    """A class to represent a user in the application"""
    __emails = set()  # Class-level set to track unique emails

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()  # Call to BaseModel's constructor
        self.first_name = self.validate_name(first_name, "First name")
        self.last_name = self.validate_name(last_name, "Last name")
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.places = []  #It saves the places that the user has created

    def validate_name(self, name, field_name):
        if not name or len(name) > 50:
            raise ValueError(f"{field_name} is required and must be at most 50 characters long.")
        return name

    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        if email in User._emails:
            raise ValueError("Email must be unique.")
        User.__emails.add(email)
        return email

    def __repr__(self):
        return f"<User  {self.first_name} {self.last_name}>"