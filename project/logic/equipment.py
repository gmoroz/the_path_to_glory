import marshmallow
import marshmallow_dataclass
import json
from dataclasses import dataclass, field
from random import uniform


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    def calc_damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]

    class Meta:
        unknown = marshmallow.EXCLUDE


class Equipment:
    def __init__(self) -> None:
        self.equipment = self._get_equipment_data()

    def _get_item(
        self, item_name: str, items: list[Armor | Weapon]
    ) -> Weapon | Armor | None:
        for item in items:
            if item_name == item.name:
                return item

    def _get_names(self, items: list[Weapon | Armor]) -> list[str]:
        return [item.name for item in items]

    def get_weapon(self, weapon_name: str) -> Weapon | None:
        return self._get_item(weapon_name, self.equipment.weapons)

    def get_armor(self, armor_name: str) -> Armor | None:
        return self._get_item(armor_name, self.equipment.armors)

    def get_weapons_names(self) -> list[str]:
        return self._get_names(self.equipment.weapons)

    def get_armors_names(self) -> list[str]:
        return self._get_names(self.equipment.armors)

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        with open("project/data/equipment.json") as file:
            data = json.load(file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        return equipment_schema().load(data)
