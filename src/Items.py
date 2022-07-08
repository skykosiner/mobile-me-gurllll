from dataclasses import dataclass
from typing import List

@dataclass
class Items:
    Category: str
    ItemCode: str
    Description: str
    Price: float

    @staticmethod
    def GetIems() -> List[Items]:
