from typing import List

from ...models.sk.document import ActDocumentModel

class DocumentsResource:
    def __init__(self, client):
        self._client = client

    def list(self, object_id) -> List[ActDocumentModel]:
        data = self._client.get(f"/api/sk-service/v2/documents?projectId={object_id}&userId=1ab20141-b424-4099-8409-f69ef8d9d492")
        return [ActDocumentModel.model_validate(item) for item in data]
