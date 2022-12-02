from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from classes import UnitClass
from logic.equipment import Armor, Weapon


class BaseUnit(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = ...
        self.armor = ...
        self._is_skill_used = False

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
        return damage

    def get_damage(self, damage: float) -> None:
        self.hp -= damage

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        if self._is_skill_used:
            return "Навык уже использован."
        return self.unit_class.skill.use(user=self, target=target)


class PlayerUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:
        if self.unit_class.stamina >= self.weapon.stamina_per_hit:
            self.stamina -= self.weapon.stamina_per_hit
            damage = self._count_damage(target)
            if damage > 0:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:
        if not self._is_skill_used and choice(range(5)) == 4:
            self._is_skill_used = True
            return self.use_skill(target)
        if self.unit_class.stamina >= self.weapon.stamina_per_hit:
            self.stamina -= self.weapon.stamina_per_hit
            damage = self._count_damage(target)
            if damage > 0:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
