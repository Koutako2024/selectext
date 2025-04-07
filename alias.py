from enum import Enum, auto


class AliasType(Enum):
    FILENAME = auto()
    OTHER_TEXT = auto()


class Alias:
    def __init__(self, type: AliasType, content: str) -> None:
        self.type: AliasType = type
        self.content: str = content
