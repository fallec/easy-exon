from datetime import datetime, date
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class ProjectDocContentModel(BaseModel):
    # --- идентификация ---
    id: str
    sectionId: Optional[str] = None
    changeSetId: Optional[str] = None
    createdAt: datetime
    status: Optional[str] = None          # Enum можно добавить позже
    cipher: Optional[str] = None
    change: Optional[int] = None
    version: Optional[int] = None

    # --- файлы и названия ---
    documentFileId: Optional[str] = None
    name: Optional[str] = None
    sectionName: Optional[str] = None
    labelName: Optional[str] = None     # в выборке нет, но бывает в других проектах

    # --- календарные поля ПД ---
    approvalDate: Optional[date] = None
    expectedApprovalDate: Optional[date] = None
    transferToClientDate: Optional[date] = None
    sendToWorkContractorDate: Optional[date] = None

    # --- экспертиза ---
    expertiseConclusionNumber: Optional[str] = None
    expertiseDate: Optional[date] = None
    expertOpinionId: Optional[str] = None

    # --- метаданные проекта/файла ---
    projectId: Optional[str] = None
    qrFileId: Optional[str] = None
    xsdDocumentType: Optional[str] = None
    extension: Optional[str] = None

    # --- счётчики и флаги ---
    remarkCount: Optional[int] = 0
    hasRequestChangeIndicator: bool = False
    needActionIndicator: bool = False
    needQrCodeIndicator: bool = False
    noteActionIndicator: bool = False
    toDelegateIndicator: bool = False

    # --- ответственность ---
    responsibleEmployeeUserId: Optional[str] = None
    organizationId: Optional[str] = None
    initiatorUserId: Optional[str] = None
    initiatorOrganizationId: Optional[str] = None
    authorMemberId: Optional[str] = None
    authorMemberName: Optional[str] = None

    # --- прочее ---
    note: Optional[str] = ""
    exploItStatus: Optional[str] = None

    model_config = ConfigDict(
        orm_mode=True,
        extra="ignore",          # игнорируем неожиданные ключи
        populate_by_name=True,   # можно подавать snake_case, если нужно
    )


class ProjectDocModel(BaseModel):
    content: List[ProjectDocContentModel]
    pageNum: Optional[int] = None
    pageCount: Optional[int] = None
    pageSize: Optional[int] = None
    totalSize: Optional[int] = None
