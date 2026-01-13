from .timestamp_mixin import TimestampMixin


class BaseEntity(TimestampMixin):
    id: int
