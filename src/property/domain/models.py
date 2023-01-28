from dataclasses import dataclass


@dataclass
class Property:
    address: str
    city: str
    price: int
    description: str
    status: str
