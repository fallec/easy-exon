from typing import List

from ..models.user import UserModel

class UsersResource:
    def __init__(self, client):
        self._client = client

    def get(self, users_id: List[str]) -> List[UserModel]:
        data = self._client.post(f"/api/users-service/users/get-users", json=[u for u in users_id])
        return [UserModel.model_validate(item) for item in data]
    
    def list(self) -> List[UserModel]:
        data = self._client.get(f"/api/users-service/users/registry")
        return [UserModel.model_validate(item) for item in data]

    def put(self, new_user: dict) -> UserModel:
        data = self._client.put(f"/api/users-service/users", json=new_user)
        return UserModel.model_validate(data)

    def me(self) -> UserModel:
        data = self._client.get(f"/api/users-service/users/current")
        return UserModel.model_validate(data)
