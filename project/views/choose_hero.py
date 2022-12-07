from flask_restx import Namespace, Resource
from flask import request, render_template, redirect
from project.container import heroes
from project.logic.unit import PlayerUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_hero_ns = Namespace("choose-hero")


class ChooseHeroView(Resource):
    def get(self):
        unit_params = get_unit_params()
        unit_params["header"] = "Выберите героя"
        return render_template(unit_params)

    def post(self):
        player_data = request.form.to_dict()
        heroes["player"] = create_unit(player_data, PlayerUnit)
