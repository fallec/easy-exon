from typing import List, Optional

from pydantic import BaseModel, Field

from .universal import UserPreview, PirCipher, FileAttachment


# ────────────────────────── Вспомогательные модели ──────────────────────────


class RemarkLink(BaseModel):
    """Краткая ссылка на замечание, вошедшее в инспекцию."""
    id: str                                  # в API бывает числом или строкой
    isDeletable: Optional[bool] = None
    deletionRefuseReason: Optional[str] = None


# ────────────────────────── Основная модель ──────────────────────────


class InspectionModel(BaseModel):
    """
    Инспекция / акт строительного контроля.

    * `id` — обязательный целочисленный идентификатор.
    * Все остальные поля опциональны и допускают «лишние» ключи (`extra="allow"`).
    """

    # ─── Обязательные ───
    id: int

    # ─── Базовые реквизиты ───
    projectId: Optional[str] = None
    number: Optional[str] = None
    buildingObject: Optional[str] = None
    location: Optional[str] = None
    workType: Optional[str] = None           # для одного типа работ
    workTypes: List[str] = Field(default_factory=list)  # для множественных типов
    description: Optional[str] = None
    status: Optional[str] = None             # OPEN / HAVE_REMARKS / CLOSED …
    result: Optional[str] = None             # итог/заключение инспекции

    # ─── Даты (Unix-ms → datetime) ───
    creationDate: Optional[int] = None
    startDate: Optional[int] = None
    endDate: Optional[int] = None
    removalTerm: Optional[str] = None
    removalDate: Optional[str] = None
    removeResponsibleDate: Optional[str] = None

    # ─── Пользователи ───
    authorUserId: Optional[str] = None
    responsibleUserId: Optional[str] = None
    responsibleBuilderUserId: Optional[str] = None
    creatorUserId: Optional[str] = None

    notifyUserIds: List[str] = Field(default_factory=list)
    participantUserIds: List[str] = Field(default_factory=list)

    authorUser: Optional[UserPreview] = None
    responsibleUser: Optional[UserPreview] = None
    responsibleBuilder: Optional[UserPreview] = None
    creatorUser: Optional[UserPreview] = None
    notifyUsers: List[UserPreview] = Field(default_factory=list)
    participantUsers: List[UserPreview] = Field(default_factory=list)

    # ─── Логические флаги ───
    priorityType: Optional[str] = None
    attentionIndicator: Optional[str] = None
    hasComments: Optional[bool] = None
    isSigned: Optional[bool] = None
    isSend: Optional[bool] = None
    createdFromBus: Optional[bool] = None

    # ─── Документы и ссылки ───
    pirCiphers: List[PirCipher] = Field(default_factory=list)
    descriptionAttachments: List[FileAttachment] = Field(default_factory=list)
    responsibleForCorrectingAttachments: List[FileAttachment] = Field(default_factory=list)

    # ─── Журналы / инспекции / замечания ───
    generalJournalIds: List[str] = Field(default_factory=list)
    inspectionIds: List[int] = Field(default_factory=list)
    inspectionNumbers: List[str] = Field(default_factory=list)
    inspectionCount: Optional[str] = None

    remarks: List[RemarkLink] = Field(default_factory=list)
    remarkNumbers: List[str] = Field(default_factory=list)
    remarkCount: Optional[str] = None

    # ─── Причины, нормативы, структура ───
    causes: List[str] = Field(default_factory=list)
    structureElement: Optional[str] = None
    requestRemovalRemark: Optional[str] = None
    refuseReason: Optional[str] = None

    class Config:
        extra = "allow"
        str_strip_whitespace = True
        from_attributes = True
