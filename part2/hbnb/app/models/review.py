from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    """
    Review class represents a review made by a user for a place.
    Attributes:
        text (str): The content of the review.
        rating (int): The rating given to the place in the review, must be between 1 and 5.
        place (Place): The place being reviewed.
        user (User): The user who made the review.
        created_at (datetime): The datetime when the review was created.
        updated_at (datetime): The datetime when the review was last updated.
    """
    def __init__(self, text=str, rating=int, place=Place, user=User):
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = place
        self.user = user

    @staticmethod
    def validate_text(text):
        if not text:
            raise ValueError("Review text is required.")
        return text

    @staticmethod
    def validate_rating(rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def __repr__(self):
        return f"<Review by {self.user.email} for {self.place.title}>"
