from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
# from app.persistence.repository import InMemoryRepository
from app.persistence.repository import SQLAlchemyRepository


#<--- Facade.py --->
class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        self.user_repo.update(user_id, data)

    def delete_user(self, user_id):
        self.user_repo.delete(user_id)