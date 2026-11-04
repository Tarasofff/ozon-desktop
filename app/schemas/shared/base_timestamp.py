from datetime import datetime
from schemas.shared import BaseSchema


class BaseTimestampedRead(BaseSchema):
    created_at: datetime
    updated_at: datetime
