import json
import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass
from logic.skills import ConcreteSkill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: ConcreteSkill

    class Meta:
        unknown = marshmallow.EXCLUDE


def get_unit_classes() -> dict[UnitClass]:
    with open("data/units.json") as file:
        unit_classes = {}
        data = json.load(file)
        unit_schema = marshmallow_dataclass.class_schema(UnitClass)
        for ent in data:
            unit_class = unit_schema().load(ent)
            unit_classes[unit_class.name] = unit_class
        return unit_classes
