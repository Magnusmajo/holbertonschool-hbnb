from app.models.base import BaseModel
from app.models.user import User


class Place(BaseModel):
    """Represents a place with a title, description, price, location, and owner."""

    def __init__(self, title: str, description: str=None, price: float=0.0, latitude: float=0.0, longitude: float=0.0, owner_id: User=None):
        """
        Initializes a new Place instance.

        Args:
        Default Values: Set default values for description, price, latitude, longitude, and owner to ensure that they can be omitted when creating a Place instance.
            title (str): The title of the place.
            description (str): A description of the place.
            price (float): The price of the place.
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            owner (User): The owner of the place.

        Raises:
            ValueError: If any of the provided values are invalid.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        # self.reviews = []  # A list of reviews for the place.
        # self.amenities = []  # A list of amenities available at the place.

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
            raise ValueError("Error: Title is required and must be 100 characters or less.")
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
        if value < 0:
            raise ValueError("Error: Price must be a positive value.")
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
            raise ValueError("Error: Latitude must be within the range of -90.0 to 90.0.")
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
            raise ValueError("Error: Longitude must be within the range of -180.0 to 180.0.")
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
            value (User): The user instance to set as the owner.

        Raises:
            ValueError: If the provided value is not an instance of User.
        """
        if not isinstance(value, User):
            raise ValueError("Error: Owner must be a valid User instance.")
        self._owner = value

    def add_review(self, review):
        """Adds a review to the place."""
        self.reviews.append(review)
        review.place = self  # Ensure the review knows which place it belongs to

    def list_reviews(self):
        """Returns a list of reviews for the place."""
        return self.reviews

    def add_amenity(self, amenity):
        """Adds an amenity to the place."""
        self.amenities.append(amenity)
        amenity.places.append(self)  # Ensure the amenity knows which place it belongs to

    def list_amenities(self):
        """Returns a list of amenities available at the place."""
        return self.amenities

    def __repr__(self): return f"<Place {self.title}>"

    def to_dict(self):
        """Convert the Place instance to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.username if self.owner else None,
            'reviews': [review.to_dict() for review in self.reviews],
            'amenities': [amenity.to_dict() for amenity in self.amenities],
        }
