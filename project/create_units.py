from project.container import equipment, unit_classes, user_service
from project.constants import GLADIATOR_NAMES
from project.logic.arena import Arena
from project.logic.unit import BaseUnit, EnemyUnit, PlayerUnit
from random import choice


def get_unit(unit_data, Unit: BaseUnit, is_enemy=False) -> BaseUnit:
    name = (
        choice(GLADIATOR_NAMES)
        if is_enemy
        else user_service.get_user_by_token().username
    )
    type_of_unit = unit_data.get("unit_class").get("name")
    weapon = equipment.get_weapon(unit_data.get("weapon").get("name"))
    armor = equipment.get_armor(unit_data.get("armor").get("name"))
    unit_class = unit_classes.get(type_of_unit)
    hp = round(unit_data.get("hp"), 1)
    stamina = round(int(unit_data.get("stamina")), 1)

    return Unit(
        name=name,
        unit_class=unit_class,
        armor=armor,
        weapon=weapon,
        hp=hp,
        stamina=stamina,
    )


def get_arena(arena_dict: dict) -> Arena:
    arena_dict["player"] = get_unit(arena_dict.get("player"), PlayerUnit)
    arena_dict["enemy"] = get_unit(arena_dict.get("enemy"), EnemyUnit)
    return Arena(**arena_dict)
