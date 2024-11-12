from app.models.base import BaseModel
from app.models.user import User


class Place(BaseModel):
    """Represents a place with a title, description, price, location, and owner."""

    def __init__(self, title=str, description=None, price=float, latitude=float, longitude=float, owner=User):
        """
        Initializes a new Place instance.

        Args:
            title (str): The title of the place.
            description (str): A description of the place.
            price (float): The price of the place.
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            owner (User ): The owner of the place.

        Raises:
            ValueError: If any of the provided values are invalid.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

    def __repr__(self):
        """Returns a string representation of the Place instance."""
        return f"<Place {self.title}>"

    @property
    def title(self):
        """Gets the title of the place."""
        return self._title

    @title.setter
    def title(self, value):
        """
        Sets the title of the place.

        Args:
            value (str): The new title for the place.

        Raises:
            ValueError: If the title is empty or exceeds 100 characters.
        """
        if not value or len(value) > 100:
            raise ValueError("Title is required and must be 100 characters or less.")
        self._title = value

    @property
    def price(self):
        """Gets the price of the place."""
        return self._price

    @price.setter
    def price(self, value):
        """
        Sets the price of the place.

        Args:
            value (float): The new price for the place.

        Raises:
            ValueError: If the price is not a positive value.
        """
        if value <= 0:
            raise ValueError("Price must be a positive value.")
        self._price = value

    @property
    def latitude(self):
        """Gets the latitude of the place."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """
        Sets the latitude of the place.

        Args:
            value (float): The new latitude for the place.

        Raises:
            ValueError: If the latitude is not within the range of -90.0 to 90.0.
        """
        if not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be within the range of -90.0 to 90.0.")
        self._latitude = value

    @property
    def longitude(self):
        """Gets the longitude of the place."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """
        Sets the longitude of the place.

        Args:
            value (float): The new longitude for the place.

        Raises:
            ValueError: If the longitude is not within the range of -180.0 to 180.0.
        """
        if not (-180.0 <= value <= 180.0):
            raise ValueError("Longitude must be within the range of -180.0 to 180.0.")
        self._longitude = value

    @property
    def owner(self):
        """Gets the owner of the place."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Sets the owner of the place.

        Args:
            value (User ): The user instance to set as the owner.

        Raises:
            ValueError: If the provided value is not an instance of User.
        """
        if not isinstance(value, User):
            raise ValueError("Owner must be a valid User instance.")
        self._owner = value