from flask import Flask, redirect
from flask_restx import Api
from project.views.fight.choose_hero import choose_hero_ns
from project.views.fight.choose_enemy import choose_enemy_ns
from project.views.fight.fight import fight_ns
from project.config import Config
from project.setup_db import db


def create_app(config_object):
    app = Flask(
        __name__, template_folder="project/templates", static_folder="project/static"
    )
    app.config.from_object(config_object)

    @app.get("/")
    def index():
        return redirect("/auth/login")

    register_extensions(app)
    return app


def register_extensions(app):
    api = Api(app, title="Flask Api", doc="/docs")
    api.add_namespace(choose_hero_ns)
    api.add_namespace(choose_enemy_ns)
    api.add_namespace(fight_ns)


app = create_app(Config())


def init_db(app):
    db.init_app(app)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
