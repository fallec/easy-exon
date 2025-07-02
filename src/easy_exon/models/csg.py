from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class CsgModel(BaseModel):

    id: str
    name: Optional[str] = None
    rootWorkId: Optional[str] = None
    organizationId: Optional[str] = None
    organizationShortName: Optional[str] = None
    projectId: Optional[str] = None

    isVisible: Optional[bool] = None
    isMain: Optional[bool] = None
    is4dGraph: Optional[bool] = None
    isLaborCosts: Optional[bool] = None

    createdAt: Optional[date] = None
    createdBy: Optional[str] = None

    rootEditors: List[str] = Field(default_factory=list)
    daysToYellow: Optional[int] = None
    daysToRed: Optional[int] = None
    visibleListOrgId: List[str] = Field(default_factory=list)

    class Config:
        extra = "allow"
        anystr_strip_whitespace = True
        orm_mode = True
