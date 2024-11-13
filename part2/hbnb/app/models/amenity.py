from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []  # A list of places that have this amenity.

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Name must be provided and be less than 50 characters")
        self._name = value

    def save(self):
        super().save()  # Call the save method from BaseModel

    def add_place(self, place):
        """Adds a place to the list of places that have this amenity."""
        if place not in self.places:
            self.places.append(place)
            place.amenities.append(self)

        def list_places(self):
            """Returns a list of places that have this amenity."""
            return self.places

        def __repr__(self):
            return f"<Amenity {self.name}>"