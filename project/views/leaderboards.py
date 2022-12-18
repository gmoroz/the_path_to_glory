from flask_restx import Resource, Namespace
from flask import render_template, make_response
from project.container import user_service
from project.constants import HEADERS

leaderboards_ns = Namespace("leaderboards")


@leaderboards_ns.route("")
class LeaderboardsView(Resource):
    def get(self):
        users = sorted(user_service.get_all(), key=lambda user: -user.wins_count)
        return make_response(
            render_template("leaderboards.html", users=users), 200, HEADERS
        )
