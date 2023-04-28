from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Greeting():
		name: str
		email: str
		birthday: date
