from flask_restx import Namespace, Resource
from flask import render_template, make_response, redirect
from project.constants import HEADERS
from project.container import arena, heroes
from project.functions import check_heroes

fight_ns = Namespace("fight")


@fight_ns.route("/")
class FightView(Resource):
    def get(self):
        if not check_heroes():
            return redirect("/", 302)
        arena.start_game(heroes["player"], heroes["enemy"])
        return make_response(render_template("fight.html", heroes=heroes), 200, HEADERS)


@fight_ns.route("/hit/")
class Hit(Resource):
    def get(self):
        if not check_heroes():
            return redirect("/", 302)
        result = arena.battle_result
        if arena.game_is_running:
            result = arena.player.hit(arena.enemy)
            result += "\n" + arena.next_turn()
        return make_response(
            render_template("fight.html", heroes=heroes, result=result), 200, HEADERS
        )


@fight_ns.route("/use-skill/")
class UseSkill(Resource):
    def get(self):
        if not check_heroes():
            return redirect("/", 302)
        result = arena.battle_result
        if arena.game_is_running:
            result = arena.player.use_skill(arena.enemy)
            result += "\n" + arena.next_turn()
        return make_response(
            render_template("fight.html", heroes=heroes, result=result)
        )


@fight_ns.route("/pass-turn/")
class PassTurn(Resource):
    def get(self):
        if not check_heroes():
            return redirect("/", 302)
        result = arena.battle_result
        if arena.game_is_running:
            result = arena.next_turn()
        return make_response(
            render_template("fight.html", heroes=heroes, result=result)
        )


@fight_ns.route("/end-fight/")
class EndFight(Resource):
    def get(self):
        return make_response(render_template("index.html", heroes=heroes))
