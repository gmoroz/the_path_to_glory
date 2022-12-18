from flask_restx import Namespace, Resource
from flask import render_template, make_response, session, redirect
from project.constants import HEADERS
from project.container import user_service
from project.helpers import auth_required


fight_ns = Namespace("fight")


@fight_ns.route("/")
class FightView(Resource):
    @auth_required
    def get(self):
        if session.get("arena") is None:
            return redirect("/game")
        return make_response(
            render_template("fight.html", heroes=session["arena"]),
            200,
            HEADERS,
        )


@fight_ns.route("/hit/")
class Hit(Resource):
    @auth_required
    def get(self):
        if session.get("arena") is None:
            return redirect("/game")
        result = session["arena"].battle_result
        if session["arena"].game_is_running:
            result = session["arena"].player.hit(session["arena"].enemy)
            result += "\n" + session["arena"].next_turn()
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@fight_ns.route("/use-skill/")
class UseSkill(Resource):
    @auth_required
    def get(self):
        if session.get("arena") is None:
            return redirect("/game")
        result = session["arena"].battle_result
        if session["arena"].game_is_running:
            result = session["arena"].player.use_skill(session["arena"].enemy)
            result += "\n" + session["arena"].next_turn()
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@fight_ns.route("/pass-turn/")
class PassTurn(Resource):
    @auth_required
    def get(self):
        if session.get("arena") is None:
            return redirect("/game")
        result = session["arena"].battle_result
        if session["arena"].game_is_running:
            result = session["arena"].next_turn()
        return make_response(
            render_template("fight.html", heroes=session["arena"], result=result),
            200,
            HEADERS,
        )


@fight_ns.route("/end-fight/")
class EndFight(Resource):
    @auth_required
    def get(self):
        if session.get("arena") is None:
            return redirect("/game")
        user_service.update_statistics(session["arena"].battle_result)
        token = session["token"]
        session.clear()
        session["token"] = token
        return redirect("/game")
