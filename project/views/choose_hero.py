from flask_restx import Namespace, Resource
from flask import request, render_template
from project.container import arena, equipment
from logic.classes import get_unit_classes

choose_hero_ns = Namespace("choose-hero")


class ChooseHeroView(Resource):
    def get(self):
        result = {
            "header": "Выберите героя",
            "classes": [unit_class.name for unit_class in get_unit_classes()],
            "weapons": equipment.get_weapons_names(),
            "armors": equipment.get_armors_names(),
        }
        return render_template(result)

    def post(self):
        pass
