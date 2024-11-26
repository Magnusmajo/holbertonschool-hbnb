from app.services.repositories.user_repository import UserRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
