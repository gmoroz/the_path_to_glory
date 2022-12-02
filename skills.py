from dataclasses import dataclass
from abc import ABC, abstractmethod


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

    def use(self, user, target):
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


@dataclass
class ConcreteSkill(Skill):
    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."
