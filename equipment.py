from dataclasses import dataclass
import json
import marshmallow
import marshmallow_dataclass


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class EquipmentData:
    list_of_weapons: list[Weapon]
    list_of_armors: list[Armor]

    class Meta:
        unknown = marshmallow.EXCLUDE


class Equipment:
    def __init__(self) -> None:
        self.equipment = self._get_equipment_data()

    def __get_item(
        self, item_name: str, items: list[Armor | Weapon]
    ) -> Weapon | Armor | None:
        for item in items:
            if item_name == item.name:
                return item

    def __get_names(self, items: list[Weapon | Armor]) -> list[str]:
        return [item.name for item in items]

    def get_weapon(self, weapon_name: str) -> Weapon | None:
        return self.__get_item(weapon_name, self.equipment.list_of_weapons)

    def get_armor(self, armor_name: str) -> Armor | None:
        return self.__get_item(armor_name, self.equipment.list_of_armors)

    def get_weapons_names(self) -> list[str]:
        return self.__get_names(self.equipment.list_of_weapons)

    def get_armors_names(self) -> list[str]:
        return self.__get_names(self.equipment.list_of_armors)

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        with open("data/equipment.json") as file:
            data = json.load(file)
        equipment_schema = marshmallow_dataclass.class_schema(data)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
