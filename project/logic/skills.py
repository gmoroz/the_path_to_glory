from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from project.logic.unit import BaseUnit


@dataclass
class Skill(ABC):
    name: str
    stamina: float
    damage: float

    @abstractmethod
    def skill_effect(self):
        pass

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina >= self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            user._is_skill_used = True
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


@dataclass
class ConcreteSkill(Skill):
    def skill_effect(self) -> str:
        self.user.stamina = round(self.user.stamina - self.stamina, 1)
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."
