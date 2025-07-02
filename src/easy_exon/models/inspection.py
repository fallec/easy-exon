from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


# ────────────────────────── Вспомогательные модели ──────────────────────────


class UserPreview(BaseModel):
    """Краткая информация о пользователе (автор, ответственный, получатель)."""

    id: str
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str] = None
    organizationId: Optional[str] = None
    organizationName: Optional[str] = None
    position: Optional[str] = None
    viewedAt: Optional[datetime] = None

    class Config:
        extra = "allow"


class PirCipher(BaseModel):
    """Шифр ПИР / СП с метаданными."""

    cipher: str
    cipherType: Optional[str] = None
    sectionName: Optional[str] = None
    name: Optional[str] = None
    fileId: Optional[str] = None
    change: Optional[int] = None
    status: Optional[str] = None
    initiatorOrganizationId: Optional[str] = None
    initiatorUserId: Optional[str] = None
    documentId: Optional[str] = None

    class Config:
        extra = "allow"


class FileAttachment(BaseModel):
    """Файл-вложение (описание, корректировка, комментарий и др.)."""

    type: str
    name: str
    link: str
    qrFileId: Optional[str] = None
    version: Optional[str] = None
    change: Optional[str] = None
    signed: Optional[bool] = None


# ────────────────────────── Основная модель ──────────────────────────


class InspectionModel(BaseModel):
    """
    Замечание / уведомление тех. надзора.

    * `id` — обязательный целочисленный идентификатор.
    * Все остальные поля опциональны.
    """

    # ─── Обязательные ───
    id: int

    # ─── Базовые реквизиты ───
    projectId: Optional[str] = None
    number: Optional[str] = None
    buildingObject: Optional[str] = None
    location: Optional[str] = None
    workType: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

    # ─── Даты (Unix-мс → datetime) ───
    creationDate: Optional[datetime] = None
    removalTerm: Optional[datetime] = None
    removalDate: Optional[datetime] = None
    removeResponsibleDate: Optional[datetime] = None

    @field_validator(
        'creationDate',
        'removalTerm',
        'removalDate',
        'removeResponsibleDate',
        mode='before',               # вызываем ДО базовой валидации
    )
    @classmethod
    def _ts_to_dt(cls, v):
        """Преобразуем миллисекунды UNIX-времени ⇒ datetime (UTC)."""
        if isinstance(v, int):
            return datetime.utcfromtimestamp(v / 1000)
        return v

    # ─── Пользователи ───
    authorUserId: Optional[str] = None
    responsibleUserId: Optional[str] = None
    creatorUserId: Optional[str] = None
    notifyUserIds: List[str] = Field(default_factory=list)

    authorUser: Optional[UserPreview] = None
    responsibleUser: Optional[UserPreview] = None
    creatorUser: Optional[UserPreview] = None
    notifyUsers: List[UserPreview] = Field(default_factory=list)

    # ─── Доп. поля логики ───
    priorityType: Optional[str] = None
    attentionIndicator: Optional[str] = None
    hasComments: Optional[bool] = None
    isSigned: Optional[bool] = None
    isSend: Optional[bool] = None
    createdFromBus: Optional[bool] = None
    inspectionIds: List[int] = Field(default_factory=list)
    inspectionNumbers: List[str] = Field(default_factory=list)
    inspectionCount: Optional[str] = None
    structureElement: Optional[str] = None
    causes: List[str] = Field(default_factory=list)
    refuseReason: Optional[str] = None
    requestRemovalRemark: Optional[str] = None

    # ─── Коллекции вложенных объектов ───
    pirCiphers: List[PirCipher] = Field(default_factory=list)
    descriptionAttachments: List[FileAttachment] = Field(default_factory=list)
    generalJournalIds: List[str] = Field(default_factory=list)
    responsibleForCorrectingAttachments: List[FileAttachment] = Field(default_factory=list)

    class Config:
        extra = "allow"
        anystr_strip_whitespace = True
        orm_mode = True
