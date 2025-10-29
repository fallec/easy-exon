from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict, AliasChoices, RootModel


class OrgUserLink(BaseModel):
    """
    Связь пользователя с организацией.
    """
    userId: str
    department: Optional[str] = None
    position: Optional[str] = None


class AddressData(BaseModel):
    """
    Структурированный адрес организации.
    """
    source: Optional[str] = None
    postalCode: Optional[str] = None
    regionKladrId: Optional[str] = None
    region: Optional[str] = None
    area: Optional[str] = None
    cityType: Optional[str] = None
    city: Optional[str] = None
    settlementType: Optional[str] = None
    settlement: Optional[str] = None
    cityArea: Optional[str] = None
    cityDistrict: Optional[str] = None
    street: Optional[str] = None
    house: Optional[str] = None
    blockType: Optional[str] = None
    block: Optional[str] = None
    floor: Optional[str] = None
    flatType: Optional[str] = None
    flat: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class SROCertificate(BaseModel):
    """
    Сведения о членстве в СРО.
    """
    organizationId: Optional[str] = None
    inn: Optional[str] = None
    organizationName: Optional[str] = None
    ogrn: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class Contract(BaseModel):
    """
    Договор, связанный с организацией в проекте.
    """
    id: str
    fileId: Optional[str] = None
    name: Optional[str] = None
    number: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    customerId: Optional[str] = None
    executorIds: List[str] = Field(default_factory=list)
    cost: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class SROOrganization(BaseModel):
    """
    Организация в разрезе данных СРО.
    """
    id: Optional[str] = None
    name: Optional[str] = None
    shortName: Optional[str] = None
    inn: Optional[str] = None
    ogrn: Optional[str] = None
    ogrnDate: Optional[str] = None
    kpp: Optional[str] = None
    status: Optional[str] = None
    pictureId: Optional[str] = Field(default=None, validation_alias=AliasChoices("pictureId", "avatarId"))
    ceo: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None
    addressData: Optional[AddressData] = None
    type: Optional[str] = None
    branchType: Optional[str] = None
    isGis: Optional[bool] = None
    updatedAt: Optional[str] = None
    dadataHid: Optional[str] = None
    codeCountry: Optional[str] = Field(default=None, validation_alias=AliasChoices("codeCountry", "countryCode"))
    version: Optional[int] = None

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class OrganizationSnapshot(BaseModel):
    """
    Снимок данных организации во времени.
    """
    id: str
    name: str
    shortName: Optional[str] = None
    inn: Optional[str] = None
    ogrn: Optional[str] = None
    ogrnDate: Optional[str] = None
    kpp: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None
    pictureId: Optional[str] = Field(default=None, validation_alias=AliasChoices("pictureId", "avatarId"))
    ceo: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None

    users: Optional[List[OrgUserLink]] = None
    addressData: Optional[AddressData] = None
    sroOrganizations: Optional[List[SROOrganization]] = None
    organisationChanges: Optional[dict] = None

    type: Optional[str] = None
    branchType: Optional[str] = None
    isGis: Optional[bool] = None
    isUpdated: Optional[bool] = None
    updatedAt: Optional[str] = None
    dadataHid: Optional[str] = None
    codeCountry: Optional[str] = Field(default=None, validation_alias=AliasChoices("codeCountry", "countryCode"))

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class OrganizationModel(BaseModel):
    """
    Организация с актуальными данными и историей.
    """
    id: str
    name: str
    shortName: Optional[str] = None

    inn: Optional[str] = None
    ogrn: Optional[str] = None
    ogrnDate: Optional[str] = None
    kpp: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None
    pictureId: Optional[str] = Field(default=None, validation_alias=AliasChoices("pictureId", "avatarId"))
    ceo: Optional[str] = None

    address: Optional[str] = None
    postalCode: Optional[str] = None
    addressData: Optional[AddressData] = None

    users: List[OrgUserLink] = Field(default_factory=list)
    sroOrganizations: List[SROOrganization] = Field(default_factory=list)
    organisationChanges: Optional[dict] = None

    history: List[OrganizationSnapshot] = Field(default_factory=list)

    type: Optional[str] = None
    branchType: Optional[str] = None
    isGis: Optional[bool] = None
    isUpdated: Optional[bool] = None
    updatedAt: Optional[str] = None
    dadataHid: Optional[str] = None
    codeCountry: Optional[str] = Field(default=None, validation_alias=AliasChoices("codeCountry", "countryCode"))

    model_config = ConfigDict(
        extra="allow",
        str_strip_whitespace=True,
        from_attributes=True,
        populate_by_name=True,
    )


class ProjectOrganizationLink(BaseModel):
    """
    Связь проекта с организацией и связанными сущностями.
    """
    id: str
    organizationId: str
    projectId: str
    organization: OrganizationModel
    organizationRole: Optional[str] = None
    userIds: List[str] = Field(default_factory=list)
    users: List[dict] = Field(default_factory=list)
    memberUsers: List[dict] = Field(default_factory=list)
    contracts: List[Contract] = Field(default_factory=list)
    sroCertificates: List[SROCertificate] = Field(default_factory=list)
    hashTags: List[str] = Field(default_factory=list)
    isDeveloper: Optional[bool] = None

    model_config = ConfigDict(extra="allow", populate_by_name=True)
