from enum import Enum, StrEnum, auto


class Color(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


print(Color.BLUE.value)
