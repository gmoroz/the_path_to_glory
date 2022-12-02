from __future__ import annotations
from abc import ABC, abstractmethod
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

    @property
    def health_points(self) -> str:
        return f"Очки здоровья: {self.hp}/{self.unit_class.max_health}"

    @property
    def stamina_points(self) -> str:
        return f"Очки выносливости: {self.stamina}/{self.unit_class.max_stamina}"

    def equip_weapon(self, weapon: Weapon) -> str:
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit):
        damage = self.weapon.calc_damage()
        if target.stamina >= target.armor.stamina_per_turn:
            damage -= target.armor.defence * target.unit_class.armor

    def get_damage(self, damage: float) -> None:
        self.hp -= damage

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        pass
