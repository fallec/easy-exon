import requests

from .client import BaseClient
from .exceptions import TokenError

from .resources.users import UsersResource
from .resources.organizations import OrganizationsResource
from .resources.objects import ObjectsResource

#act
from .resources.act.estimates import EstimatesResource
from .resources.act.certificates import CertificatesResource

#isr
from .resources.isr.csgs import CsgsResource
from .resources.isr.works import WorksResource

#itd
from .resources.itd.acts import ActsResource
from .resources.itd.general_journals import GeneralJournalsResource
from .resources.itd.materials import MaterialsResource
from .resources.itd.ojrs import OjrsResource
from .resources.itd.orders import OrdersResource
from .resources.itd.schemas import SchemasResource
from .resources.itd.tasks import TasksResource

#otitb
from .resources.otitb.acts import CheckingActsResource
from .resources.otitb.documents import CheckingDocumentsResource
from .resources.otitb.journals import JournalElementsResource

#pir
from .resources.pir.expertises import ExpertiseResource
from .resources.pir.project_work_docs import ProjectDocsResource
from .resources.pir.VPR_docs import VPRDocsResource
from .resources.pir.work_docs import WorkDocsResource

#sk
from .resources.sk.documents import DocumentsResource
from .resources.sk.inspections import InspectionsResource
from .resources.sk.journals import JournalsResource
from .resources.sk.registries import RegistriesResource
from .resources.sk.remarks import RemarksResource


BASE_URL = "https://exon.exonproject.ru/"


class MyApiClient(BaseClient):
    def __init__(self, base_url: str = BASE_URL, token: str = None):
        super().__init__(base_url, token)
        self.users = UsersResource(self)
        self.organizations = OrganizationsResource(self)
        self.objects = ObjectsResource(self)

        #act
        self.act_estimates = EstimatesResource(self)
        self.act_certificates = CertificatesResource(self)

        #isr
        self.isr_csgs = CsgsResource(self)
        self.isr_works = WorksResource(self)

        #itd
        self.itd_acts = ActsResource(self)
        self.itd_general_journals = GeneralJournalsResource(self)
        self.itd_materials = MaterialsResource(self)
        self.itd_ojrs = OjrsResource(self)
        self.itd_orders = OrdersResource(self)
        self.itd_schemas = SchemasResource(self)
        self.itd_tasks = TasksResource(self)

        #otitb
        self.otitb_acts = CheckingActsResource(self)
        self.otitb_documents = CheckingDocumentsResource(self)
        self.otitb_journals = JournalElementsResource(self)

        #pir
        self.pir_expertise = ExpertiseResource(self)
        self.pir_project_docs = ProjectDocsResource(self)
        self.pir_vpr_docs = VPRDocsResource(self)
        self.pir_work_docs = WorkDocsResource(self)

        #sk
        self.sk_documents = DocumentsResource(self)
        self.sk_inspections = InspectionsResource(self)
        self.sk_journals = JournalsResource(self)
        self.sk_registries = RegistriesResource(self)
        self.sk_remarks = RemarksResource(self)


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
