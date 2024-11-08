from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def __repr__(self):
        return f"<Review by {self.user.first_name} for {self.place.title}>"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

        @property
        def text(self):
            return self._text

        @text.setter
        def text(self, value):
            if not value:
                raise ValueError("Review text is required")
            self._text = value

        @property
        def rating(self):
            return self._rating

        @rating.setter
        def rating(self, value):
            if not (1 <= value <= 5):
                raise ValueError("Rating must be between 1 and 5")
            self._rating = value

        @property
        def place(self):
            return self._place

        @place.setter
        def place(self, value):
            if not isinstance(value, Place):
                raise ValueError("Invalid place")
            self._place = value

        @property
        def user(self):
            return self._user

        @user.setter
        def user(self, value):
            if not isinstance(value, User):
                raise ValueError("Invalid user")
            self._user = value

        @property
        def created_at(self):
            return self._created_at

        @created_at.setter
        def created_at(self, value):
            self._created_at = value

        @property
        def updated_at(self):
            return self._updated_at

        @updated_at.setter
        def updated_at(self, value):
            self._updated_at = value