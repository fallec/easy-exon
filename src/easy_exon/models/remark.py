from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict

from .universal import UserPreview, PirCipher, FileAttachment


# ────────────────────────────── Основная модель замечания ──────────────────────────────


class RemarkModel(BaseModel):
    """
    Замечание строительного контроля / технадзора.

    `id` — единственное обязательное поле, все прочие считаются опциональными.
    """

    # базовая конфигурация (Pydantic v2)
    model_config = ConfigDict(
        extra="allow",              # пропускать неописанные поля
        str_strip_whitespace=True,  # авто-trim строк
        from_attributes=True,
    )

    # ─── Идентификаторы ───
    id: int
    projectId: Optional[str] = None

    # ─── Датовые метки ───
    creationDate: Optional[str] = None
    removalTerm: Optional[str] = None
    removalDate: Optional[str] = None
    removeResponsibleDate: Optional[str] = None

    # ─── Участники ───
    authorUserId: Optional[str] = None
    responsibleUserId: Optional[str] = None
    creatorUserId: Optional[str] = None
    notifyUserIds: List[str] = Field(default_factory=list)

    authorUser: Optional[UserPreview] = None
    responsibleUser: Optional[UserPreview] = None
    creatorUser: Optional[UserPreview] = None
    notifyUsers: List[UserPreview] = Field(default_factory=list)

    # ─── Основные реквизиты ───
    number: Optional[str] = None
    buildingObject: Optional[str] = None
    location: Optional[str] = None
    workType: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None                    # OPEN / REMOVED / CLOSED …
    priorityType: Optional[str] = None              # REGULAR / HIGH …

    # ─── Причины и нормативы ───
    causes: List[str] = Field(default_factory=list)

    # ─── Документы ───
    pirCiphers: List[PirCipher] = Field(default_factory=list)
    descriptionAttachments: List[FileAttachment] = Field(default_factory=list)
    responsibleForCorrectingAttachments: List[FileAttachment] = Field(default_factory=list)

    # ─── Журналы, инспекции ───
    generalJournalIds: List[str] = Field(default_factory=list)
    inspectionIds: List[int] = Field(default_factory=list)
    inspectionNumbers: List[str] = Field(default_factory=list)
    inspectionCount: Optional[str] = None

    # ─── Флаги / индикаторы ───
    isSigned: Optional[bool] = None
    isSend: Optional[bool] = None
    createdFromBus: Optional[bool] = None
    attentionIndicator: Optional[str] = None
    hasComments: Optional[bool] = None

    # ─── Прочее ───
    structureElement: Optional[str] = None
    requestRemovalRemark: Optional[str] = None
    refuseReason: Optional[str] = None
