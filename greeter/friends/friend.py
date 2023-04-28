from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Friend:
    name: str
    email: str
    birthday: date
