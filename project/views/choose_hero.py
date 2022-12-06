from flask_restx import Namespace, Resource
from flask import request, render_template
from project.container import arena, equipment, heroes

from logic.unit import PlayerUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_hero_ns = Namespace("choose-hero")


class ChooseHeroView(Resource):
    def get(self):
        unit_params = get_unit_params()
        return render_template(
            {
                "header": "Выберите героя",
                "classes": [unit_class.name for unit_class in get_unit_classes()],
                "weapons": equipment.get_weapons_names(),
                "armors": equipment.get_armors_names(),
            }
        )

    def post(self):
        player_data = request.form.to_dict()
        heroes["player"] = create_unit(player_data, PlayerUnit)
