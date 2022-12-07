from flask_restx import Namespace, Resource
from flask import request, render_template
from project.container import heroes
from project.logic.unit import EnemyUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_enemy_ns = Namespace("choose-enemy")


@choose_enemy_ns.route("/")
class ChooseHeroView(Resource):
    def get(self):
        unit_params = get_unit_params()
        unit_params["header"] = "Выберите врага"
        return render_template("hero_choosing.html", result=unit_params)

    def post(self):
        enemy_data = request.form.to_dict()
        heroes["enemy"] = create_unit(enemy_data, EnemyUnit)
