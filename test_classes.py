from __future__ import annotations
from typing import TYPE_CHECKING
from logic.classes import get_unit_classes

if TYPE_CHECKING:
    from logic.classes import UnitClass


unit_classes = get_unit_classes()
warrior: UnitClass = unit_classes["Воин"]
mage: UnitClass = unit_classes["Маг"]
thief: UnitClass = unit_classes["Вор"]
assert warrior.skill.name == "Свирепый пинок"
