from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator


# ──────────────────────── Атрибуты пользователя ────────────────────────


class UserAttributes(BaseModel):
    """Гибкая модель «ключ-значение» с типами для самых частых полей."""

    # «паспорт» пользователя
    middle_name: Optional[str] = None
    position: Optional[str] = None
    department: Optional[str] = None
    phone_number: Optional[str] = None
    inn: Optional[str] = None
    snils: Optional[str] = None

    # интерфейс / внешний вид
    image_id: Optional[str] = None
    image_color: Optional[str] = None

    # внутренние флаги учётной записи
    banking_activity: Optional[bool] = None
    is_activated: Optional[bool] = None
    is_2fa_enabled: Optional[bool] = None
    is_delegated: Optional[bool] = None
    is_external_user: Optional[bool] = None
    privacy_license_is_accepted: Optional[bool] = None
    user_agreement_is_accepted: Optional[bool] = None

    # связи с организацией
    current_organisation_id: Optional[str] = None

    # даты
    last_login_date: Optional[str] = None

    model_config = ConfigDict(extra="allow")   # сохраняем любые неожиданные поля


# ──────────────────────── Основная модель пользователя ────────────────────────


class UserModel(BaseModel):
    """
    Пользователь EXON/KeyCloak.

    * `id` — UUID (обязателен).
    * Все остальные поля опциональны.
    """

    id: str
    login: Optional[str] = None
    emailAddress: Optional[str] = None

    firstName: Optional[str] = None
    lastName: Optional[str] = None
    registrationDate: Optional[str] = None

    roles: List[str] = Field(default_factory=list)
    attributes: UserAttributes = Field(default_factory=UserAttributes)

    enabled: Optional[bool] = None
    emailVerified: Optional[bool] = None
    isFake: Optional[bool] = None

    model_config = ConfigDict(extra="allow", str_strip_whitespace=True, from_attributes=True)
