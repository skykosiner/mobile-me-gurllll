from dataclasses import dataclass
from typing import List
import json

@dataclass
class Items:
    Category: str
    ItemCode: str
    Description: str
    Price: float

def GetItems() -> List[Items]:
    items: List[Items] = []

    f = open("items.json")
    data = json.load(f)

    for i in data['items']:
        item = Items(**i)
        items.append(item)

    f.close()

    return items
