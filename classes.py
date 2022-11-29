from dataclasses import dataclass


@dataclass
class ConcreteSkill:
    name: str
    stamina_consumption: float
    damage: float


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: ConcreteSkill
