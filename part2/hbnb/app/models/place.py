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
            owner_id (User): The owner of the place.

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
        self.reviews = []  # A list of reviews for the place.
        self.amenities = []  # A list of amenities available at the place.

    @staticmethod
    def validate_title(title):
        """Validates the title of a place   """
        if not title or len(title) > 100:
            raise ValueError("Error: Title is required and must be at most 100 characters long.")
        return title

    @staticmethod
    def validate_price(price):
        """Validates the price of a place."""
        if price < 0:
            raise ValueError("Error: Price must be a non-negative value.")
        return price

    @staticmethod
    def validate_latitude(latitude):
        """Validates the latitude of a place."""
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Error: Latitude must be within the range of -90.0 to 90.0.")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        """Validates the longitude of a place."""
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Error: Longitude must be within the range of -180.0 to 180.0.")
        return longitude

    @staticmethod
    def validate_owner_id(owner_id):
        """Validates the owner of a place."""
        if not isinstance(owner_id, User):
            raise ValueError("Error: Owner must be a valid User instance.")
        return owner_id

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
        amenity.places.append(self)  # Ensure the place-owner of the amenity

    def list_amenities(self):
        """Returns a list of amenities available at the place."""
        return self.amenities

    def __repr__(self):
        return f"Place('{self.name}' owned by {self.owner.first_name} {self.owner.last_name})"