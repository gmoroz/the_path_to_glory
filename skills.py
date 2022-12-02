from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


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

    def use(self, user: BaseUnit, target: BaseUnit):
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


@dataclass
class ConcreteSkill(Skill):
    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.user.)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."
