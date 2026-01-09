from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Timestamp(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
