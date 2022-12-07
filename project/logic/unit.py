from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint
from project.logic.classes import UnitClass
from project.logic.equipment import Armor, Weapon


@dataclass
class BaseUnit(ABC):
    name: str
    unit_class: UnitClass
    _is_skill_used: bool = False

    def __post_init__(self):
        self.hp = self.unit_class.max_health
        self.stamina = self.unit_class.max_stamina
        self.weapon = ...
        self.armor = ...

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

    def _count_damage(self, target: BaseUnit) -> int:
        damage = self.weapon.calc_damage()
        if target.stamina >= target.armor.stamina_per_turn:
            damage -= target.armor.defence * target.unit_class.armor
            target.stamina -= target.armor.stamina_per_turn
        return round(damage, 1)

    def get_damage(self, damage: float) -> None:
        self.hp = round(self.hp - damage, 1)

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        if self._is_skill_used:
            return "Навык уже использован."
        return self.unit_class.skill.use(user=self, target=target)


@dataclass
class PlayerUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:

        if self.stamina >= self.weapon.stamina_per_hit:
            self.stamina = round(self.stamina - self.weapon.stamina_per_hit, 1)
            damage = self._count_damage(target)

            if damage > 0:
                target.get_damage(damage)
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."

            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:

        if not self._is_skill_used and randint(0, 100) < 36:
            return self.use_skill(target)

        if self.stamina >= self.weapon.stamina_per_hit:
            self.stamina = round(self.stamina - self.weapon.stamina_per_hit, 1)
            damage = self._count_damage(target)

            if damage > 0:
                target.get_damage(damage)
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."

            return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."

        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
