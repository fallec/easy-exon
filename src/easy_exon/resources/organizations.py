from typing import List

from ..models.organization import OrganizationModel, ProjectOrganizationLink

class OrganizationsResource:
    def __init__(self, client):
        self._client = client

    def list(self, organizations_id: list[str]) -> List[OrganizationModel]:
        data = self._client.post("/api/org-service/organizations/all", json=[o for o in organizations_id])
        return [OrganizationModel.model_validate(item) for item in data]

    def json(self, organization_id: str) -> dict:
        data = self._client.post("/api/org-service/organizations/all", json=[organization_id])
        return data

    def list_project(self, organization_id: str) -> List[ProjectOrganizationLink]:
        data = self._client.get(f"/api/project-service/organizations/members/{organization_id}")
        return [ProjectOrganizationLink.model_validate(item) for item in data]
