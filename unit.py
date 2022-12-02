from abc import ABC
from dataclasses import dataclass

from classes import UnitClass


@dataclass
class BaseUnit(ABC):
    name: str
    unit_class: UnitClass
    hp: float = unit_class.max_health
    stamina: float = unit_class.max_stamina
    