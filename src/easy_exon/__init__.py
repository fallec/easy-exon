import requests

from .client import BaseClient
from .exceptions import TokenError

from .resources.users import UsersResource
from .resources.organizations import OrganizationsResource
from .resources.objects import ObjectsResource

#sk
from .resources.sk.documents import DocumentsResource
from .resources.sk.inspections import InspectionsResource
from .resources.sk.journals import JournalsResource
from .resources.sk.registries import RegistriesResource
from .resources.sk.remarks import RemarksResource

#isr
from .resources.isr.csgs import CsgsResource
from .resources.isr.works import WorksResource

#itd
from .resources.itd.acts import ActsResource
from .resources.itd.materials import MaterialsResource
from .resources.itd.ojrs import OjrsResource
from .resources.itd.orders import OrdersResource
from .resources.itd.schemas import SchemasResource
from .resources.itd.tasks import TasksResource

#pir
from .resources.pir.work_docs import DocsResource


BASE_URL = "https://exon.exonproject.ru/"


class MyApiClient(BaseClient):
    def __init__(self, base_url: str = BASE_URL, token: str = None):
        super().__init__(base_url, token)
        self.users = UsersResource(self)
        self.organizations = OrganizationsResource(self)
        self.objects = ObjectsResource(self)

        #sk
        self.documents = DocumentsResource(self)
        self.inspections = InspectionsResource(self)
        self.journals = JournalsResource(self)
        self.registries = RegistriesResource(self)
        self.remarks = RemarksResource(self)

        #isr
        self.csgs = CsgsResource(self)
        self.works = WorksResource(self)

        #itd
        self.acts = ActsResource(self)
        self.materials = MaterialsResource(self)
        self.ojrs = OjrsResource(self)
        self.orders = OrdersResource(self)
        self.schemas = SchemasResource(self)
        self.tasks = TasksResource(self)

        #pir
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
