from logic.arena import Arena
from logic.unit import BaseUnit
from logic.equipment import Equipment
from project.logic.classes import get_unit_classes

heroes = {"player": BaseUnit, "enemy": BaseUnit}
arena = Arena()
equipment = Equipment()
unit_classes = get_unit_classes()
