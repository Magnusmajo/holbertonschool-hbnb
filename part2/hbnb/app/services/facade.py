from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        """
        Create a new user with the provided user data.

        Args:
            user_data (dict): A dictionary containing user attributes.
            ** Unpacking arguments to pass the dictionary as keyword arguments.

        Returns:
            User: The new created user object.
        """
        self.user_repo = InMemoryRepository()
        user = User(**user_data)
        self.user_repo.save(user)
        return user

    # Placeholder method for fetching a user by ID
    def get_user(self, user_id):
        """
        Retrieve a user by user ID.
        """
        return self.user_repo.get(user_id)

    # Placeholder method for fetching a user by email
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Placeholder method for creating a place
    def create_place(self, place_data):
        """
        Creates a new place and saves it to the repository.
        Same way than create_user.
        Raise:
            ValueError: If the owner_id is not a valid user.
        """
        owner = self.get_user(place_data['owner_id'])
        if owner:
            place = Place(**place_data)
            self.place_repo.save(place)
            return place
        else:
            raise ValueError("Owner not found")

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        """
        Retrieve a place by its ID.
        Same way than get_user.
        """
        return self.place_repo.get(Place, place_id)

    # Placeholder method for creating a review
    def create_review(self, review_data):
        """
        Creates a review for a given user and place.

        Args:
            review_data (dict): A dictionary containing review details including 'user_id' and place_id'.
        Raises:
            ValueError: If the user or place is not found.
        """
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])
        if user and place:
            review_data['user'] = user
            review_data['place'] = place
            review = Review(**review_data)
            self.review_repo.save(review)
            return review
        else:
            raise ValueError("User or place not found")

    def get_review(self, review_id):
        """
        Retrieve a review by its ID.
        Same way than get_user.
        """
        return self.review_repo.get(Review, review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        pass

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        pass

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        pass

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass

    # Placeholder method for creating an amenity
    def create_amenity(self, amenity_data):
        """
        Create a new amenity and save it to the repository.

        Args:
            amenity_data (dict): A dictionary containing the data for the new amenity.

        Returns:
            Amenity: The newly created amenity object.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.save(amenity)
        return amenity

    # Placeholder method for fetching an amenity by ID
    def get_amenity(self, amenity_id):
        """
        Retrieve an amenity by its ID.

        Same way than get_user.
        """
        return self.amenity_repo.get(Amenity, amenity_id)

    # Example method for validating data
    def validate_data(self, data, schema):
        # Placeholder for validation logic
        pass

    # Example method for converting object to dict
    def object_to_dict(self, obj):
        # Placeholder for object conversion logic
        return obj.__dict__
