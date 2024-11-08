from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Name must be provided and be less than 50 characters")
        self._name = value

    def __repr__(self):
        return f"<Amenity name={self.name}>"

    def save(self):
        super().save()  # Call the save method from BaseModel
        # chicos el codigo adicional para guardar las amenities en base de datos o en memoria debe ser implementado aqui.

        def __repr__(self):
            return f"<Amenity {self.name}>"