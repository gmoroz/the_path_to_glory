from flask_restx import Namespace, Resource
from flask import request, render_template, redirect, make_response, session
from project.constants import HEADERS
from project.logic.unit import PlayerUnit
from project.logic.data_for_front import create_unit, get_unit_params

choose_hero_ns = Namespace("choose-hero")


@choose_hero_ns.route("/")
class ChooseHeroView(Resource):
    def get(self):
        unit_params = get_unit_params()
        unit_params["header"] = "героя"
        return make_response(
            render_template("hero_choosing.html", result=unit_params), 200, HEADERS
        )

    def post(self):
        session["player"]  = request.form.to_dict()
        return redirect("/choose-enemy/")
