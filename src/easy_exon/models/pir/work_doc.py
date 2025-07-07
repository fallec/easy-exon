from datetime import datetime, date
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class DocContentModel(BaseModel):
    # --- идентификация / версия ---
    id: str
    sectionId: Optional[str] = None
    changeSetId: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[str] = None
    cipher: Optional[str] = None               # ← оставили один раз
    change: Optional[int] = None
    version: Optional[int] = None

    # --- файлы и названия ---
    documentFileId: Optional[str] = None  
    name: Optional[str] = None  
    sectionName: Optional[str] = None
    labelName: Optional[str] = None

    # --- календарные поля ---
    vprPlanningDate: Optional[date] = None
    vprExactDate: Optional[date] = None
    expectedApprovalDate: Optional[date] = None
    approvalDate: Optional[date] = None
    transferToClientDate: Optional[date] = None
    sendToWorkContractorDate: Optional[date] = None
    transferForReworkDate: Optional[date] = None

    # --- экспертиза ---
    expertiseConclusionNumber: Optional[str] = None
    expertiseDate: Optional[date] = None
    expertOpinionId: Optional[str] = None

    # --- метаданные проекта ---
    projectId: str
    qrFileId: Optional[str] = None
    extension: Optional[str] = None
    xsdDocumentType: Optional[str] = None

    # --- числовые / флаговые ---
    delay: Optional[int] = None
    remarkCount: Optional[int] = 0
    designerRemarks: Optional[int] = None  # ⬅️ добавили default=None

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
    note: Optional[str] = ''
    exploItStatus: Optional[str] = None     # ⬅️ default=None

    authorMemberId: Optional[str] = None
    authorMemberName: Optional[str] = None
    exploItStatus: Optional[str] = None

    # --- настройки Pydantic v2 ---
    model_config = ConfigDict(
        orm_mode=True,
        extra="ignore",          # игнорируем неожиданные ключи
        populate_by_name=True,   # можно подавать snake_case, если нужно
    )

class DocModel(BaseModel):
    content: List[DocContentModel]
    pageNum: int
    pageCount: int
    pageSize: int
    totalSize: int
