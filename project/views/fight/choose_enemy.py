from flask_restx import Namespace, Resource
from flask import request, render_template, make_response, redirect, session
from project.constants import HEADERS
from project.logic.unit import EnemyUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_enemy_ns = Namespace("choose-enemy")


@choose_enemy_ns.route("/")
class ChooseHeroView(Resource):
    def get(self):
        unit_params = get_unit_params()
        unit_params["header"] = "врага"
        return make_response(
            render_template("hero_choosing.html", result=unit_params), 200, HEADERS
        )

    def post(self):
        enemy_data = request.form.to_dict()
        session["heroes"]["enemy"] = create_unit(enemy_data, EnemyUnit)
        return redirect("/fight/")