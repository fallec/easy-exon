from typing import List
from ...models.pir.work_sections import WorkSectionModel


class WorkSectionResource:
    def __init__(self, client):
        self._client = client

    def list(self, object_id) -> List[WorkSectionModel]:
        data = self._client.get(f"api/project-work-document-service/work-sections?projectId={object_id}")
        return [WorkSectionModel.model_validate(item) for item in data]
