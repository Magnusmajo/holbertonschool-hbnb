from app.models.base import BaseModel
from datetime import datetime

class User(BaseModel):
    """A class to represent a user in the application"""
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.id = self.generate_id()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"