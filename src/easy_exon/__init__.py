import requests

from .client import BaseClient
from .exceptions import TokenError
from .resources.objects import ObjectsResource
from .resources.isr.csgs import CsgsResource
from .resources.pir.work_docs import DocsResource
from .resources.isr.works import WorksResource
from .resources.sk.inspections import InspectionsResource
from .resources.sk.remarks import RemarksResource
from .resources.organizations import OrganizationsResource
from .resources.users import UsersResource
from .resources.itd.acts import ActsResource


BASE_URL = "https://exon.exonproject.ru/"


class MyApiClient(BaseClient):
    def __init__(self, base_url: str = BASE_URL, token: str = None):
        super().__init__(base_url, token)
        self.objects = ObjectsResource(self)
        self.csgs = CsgsResource(self)
        self.works = WorksResource(self)
        self.inspections = InspectionsResource(self)
        self.remarks = RemarksResource(self)
        self.organizations = OrganizationsResource(self)
        self.users = UsersResource(self)
        self.acts = ActsResource(self)
        self.docs = DocsResource(self)


def get_token(username: str, password: str) -> str:
    resp = requests.post(
        f"https://exon.exonproject.ru/auth/realms/SpringBoot/protocol/openid-connect/token",
        data = {
            "grant_type": "password",
            "client_id":  "ExonReactApp",
            "username":   username,
            "password":   password,
            "scope":      "openid",
        },
        timeout = 10,
    )

    if not resp.ok:
        raise TokenError(resp.status_code, resp.text)
    return resp.json()["access_token"]
