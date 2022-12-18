from __future__ import annotations
from random import choice
from typing import TYPE_CHECKING
from project.container import equipment, unit_classes, user_service
from project.constants import GLADIATOR_NAMES

if TYPE_CHECKING:
    from project.logic.unit import BaseUnit


def create_unit(unit_data: dict[str], UnitClass: BaseUnit) -> BaseUnit:
    name = unit_data.get("name")
    type_of_unit = unit_data.get("unit_class")
    weapon = equipment.get_weapon(unit_data.get("weapon"))
    armor = equipment.get_armor(unit_data.get("armor"))
    unit_class = unit_classes.get(type_of_unit)
    hp = unit_class.max_health
    stamina = unit_class.max_stamina
    unit: BaseUnit = UnitClass(
        name=name,
        unit_class=unit_class,
        armor=armor,
        weapon=weapon,
        hp=hp,
        stamina=stamina,
    )

    return unit


def get_unit_params(is_enemy=False) -> dict[str, list[str]]:
    return {
        "classes": unit_classes.keys(),
        "weapons": equipment.get_weapons_names(),
        "armors": equipment.get_armors_names(),
        "name": (
            choice(GLADIATOR_NAMES)
            if is_enemy
            else user_service.get_user_by_token().username
        ),
    }
