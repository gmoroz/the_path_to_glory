from __future__ import annotations
from typing import TYPE_CHECKING
from project.container import equipment, unit_classes

if TYPE_CHECKING:
    from project.logic.unit import BaseUnit


def create_unit(unit_data: dict[str], UnitClass: BaseUnit) -> BaseUnit:
    name = unit_data.get("name")
    type_of_unit = unit_data.get("unit_class")
    weapon = equipment.get_weapon(unit_data.get("weapon"))
    armor = equipment.get_weapon(unit_data.get("armor"))

    unit: BaseUnit = UnitClass(name=name, unit_class=unit_classes.get(type_of_unit))
    unit.equip_armor(armor)
    unit.equip_weapon(weapon)

    return unit


def get_unit_params() -> dict[str, list[str]]:
    return {
        "classes": unit_classes.keys(),
        "weapons": equipment.get_weapons_names(),
        "armors": equipment.get_armors_names(),
    }
