from flask_restx import Namespace, Resource
from flask import request, render_template, make_response, redirect, session
from project.constants import HEADERS
from project.helpers import auth_required
from project.logic.arena import Arena
from project.logic.unit import EnemyUnit, PlayerUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_enemy_ns = Namespace("choose-enemy")


@choose_enemy_ns.route("/")
class ChooseEnemyView(Resource):
    @auth_required
    def get(self):
        unit_params = get_unit_params(is_enemy=True)
        unit_params["header"] = "врага"
        return make_response(
            render_template("hero_choosing.html", result=unit_params), 200, HEADERS
        )

    @auth_required
    def post(self):
        enemy_data = request.form.to_dict()
        session["arena"] = Arena(
            create_unit(session["player"], PlayerUnit),
            create_unit(enemy_data, EnemyUnit),
        )
        session.pop("player", None)
        session["arena"].start_game()
        return redirect("/fight/")
