from dataclasses import dataclass


@dataclass
class ItemDto:
    title: str = None
    description: str = None
    quantity: int = None
    status: str = None


@dataclass
class HistoryDto:
    comment: str = None
    status: str = None
    operation: str = None
    entity: str = None
    entity_id: int = None
