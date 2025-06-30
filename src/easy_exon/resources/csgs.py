from typing import List

from ..models.csg import CsgModel

class CsgsResource:
    def __init__(self, client):
        self._client = client

    def list(self, object_id) -> List[CsgModel]:
        data = self._client.get(f"/api/isr-new-service/graphs/{object_id}/all")
        return [CsgModel.model_validate(item) for item in data]
