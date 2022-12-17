from flask_restx import Namespace, Resource
from flask import render_template, make_response, redirect, session
from project.constants import HEADERS, WIN
from project.helpers import auth_required
from project.logic.arena import Arena
from project.container import user_service

fight_ns = Namespace("fight")


@auth_required
@fight_ns.route("/")
class FightView(Resource):
    def get(self):
        session["arena"] = Arena()
        session["arena"].start_game(
            session["heroes"]["player"], session["heroes"]["enemy"]
        )
        return make_response(
            render_template("fight.html", heroes=session["heroes"]), 200, HEADERS
        )


@auth_required
@fight_ns.route("/hit/")
class Hit(Resource):
    def get(self):
        result = session["arena"].battle_result
        if session["arena"].game_is_running:
            result = session["arena"].player.hit(session["arena"].enemy)
            result += "\n" + session["arena"].next_turn()
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@auth_required
@fight_ns.route("/use-skill/")
class UseSkill(Resource):
    def get(self):
        result = session["arena"].battle_result
        if session["arena"].game_is_running:
            result = session["arena"].player.use_skill(session["arena"].enemy)
            result += "\n" + session["arena"].next_turn()
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result)
        )


@auth_required
@fight_ns.route("/pass-turn/")
class PassTurn(Resource):
    def get(self):
        result = session["arena"].battle_result
        if session["arena"].game_is_running:
            result = session["arena"].next_turn()
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result)
        )


@auth_required
@fight_ns.route("/end-fight/")
class EndFight(Resource):
    def get(self):
        if session["arena"] == WIN:
            session["user_d"].wins += 1
        else:
            session["user_d"].loses += 1
        user_service.update(session["user_d"])
        session.pop("arena")
        session.pop("heroes")
        return make_response(
            render_template("start_game.html", heroes=session["arena"])
        )
