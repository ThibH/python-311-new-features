from typing import Self


class CustomPath:
    def __init__(self, path: str):
        self.path = path

    def concat(self, other: str) -> Self:
        return CustomPath(f'{self.path}/{other}')

    def __str__(self):
        return self.path


p = CustomPath("/Users")
print(p.concat("thibh"))


class MyInt(int):
    @classmethod
    def fromhex(cls, s: str) -> Self:
        return cls(int(s, 16))


i = MyInt.fromhex("FF")
print(i)
