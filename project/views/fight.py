from flask_restx import Namespace, Resource
from flask import render_template, make_response
from project.constats import HEADERS
from project.container import arena, heroes

fight_ns = Namespace("fight")


@fight_ns.route("/")
class FightView(Resource):
    def get(self):
        arena.start_game(heroes["player"], heroes["enemy"])
        return make_response(render_template("fight.html", heroes=heroes), 200, HEADERS)


@fight_ns.route("/hit/")
class Hit(Resource):
    def get(self):
        result = ""
        if arena.game_is_running:
            result = arena.player.hit(arena.enemy)
        return make_response(
            render_template("fight.html", heroes=heroes, result=result), 200, HEADERS
        )
