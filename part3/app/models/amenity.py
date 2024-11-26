from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name)


    @staticmethod
    def validate_name(name):
        if not name or len(name) > 100:
            raise ValueError("Error: Name is required and must be at most 100 characters long.")
        return name

    def __repr__(self):
        return f"Amenity('{self.name}')"