from __future__ import annotations
from abc import ABC
from classes import UnitClass
from equipment import Armor, Weapon


class BaseUnit(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = ...
        self.armor = ...
        self._is_skill_used = ...

    def health_points(self):
        return f"Очки здоровья: {self.hp}/{self.unit_class.max_health}"

    def stamina_points(self):
        return f"Очки выносливости: {self.stamina}/{self.unit_class.max_stamina}"

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit):
        pass
