from flask_restx import Namespace, Resource
from flask import render_template, make_response, session, redirect
from project.constants import HEADERS
from project.helpers import auth_required
from project.create_units import get_arena


fight_ns = Namespace("fight")


@fight_ns.route("/")
class FightView(Resource):
    @auth_required
    def get(self):
        arena = get_arena(session["arena"])
        return make_response(
            render_template("fight.html", heroes=arena),
            200,
            HEADERS,
        )


@fight_ns.route("/hit/")
class Hit(Resource):
    @auth_required
    def get(self):
        arena = get_arena(session["arena"])
        result = arena.battle_result
        if arena.game_is_running:
            result = arena.player.hit(arena.enemy)
            result += "\n" + arena.next_turn()
        session["arena"] = arena
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@fight_ns.route("/use-skill/")
class UseSkill(Resource):
    @auth_required
    def get(self):
        arena = get_arena(session["arena"])
        result = arena.battle_result
        if arena.game_is_running:
            result = arena.player.use_skill(arena.enemy)
            result += "\n" + arena.next_turn()
        session["arena"] = arena
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@fight_ns.route("/pass-turn/")
class PassTurn(Resource):
    @auth_required
    def get(self):
        arena = get_arena(session["arena"])
        result = arena.battle_result
        if arena.game_is_running:
            result = arena.next_turn()
        session["arena"] = arena
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@fight_ns.route("/end-fight/")
class EndFight(Resource):
    @auth_required
    def get(self):
        session.pop("arena", None)
        return redirect("/game")
