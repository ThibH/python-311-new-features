from typing import TypedDict, NotRequired, Required


class Movie(TypedDict):
    title: str
    year: int
    rating: NotRequired[int]


m1: Movie = {"title": "Blade Runner", "year": 2018}
