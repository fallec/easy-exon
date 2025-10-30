from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class WorkSectionModel(BaseModel):
    id: str

    name: Optional[str] = None
    projectId: Optional[str] = None
    parentId: Optional[str] = None
    hasAccess: Optional[bool] = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        populate_by_name=True,
    )
