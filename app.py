from flask import Flask, render_template
from flask_restx import Api
from project.views.choose_hero import choose_hero_ns
from project.views.choose_enemy import choose_enemy_ns
from project.views.fight import fight_ns
from project.config import Config
from project.setup_db import db


def create_app(config_object):
    app = Flask(__name__, template_folder="project/templates")
    app.config.from_object(config_object)

    @app.get("/")
    def index():
        return render_template("index.html")

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
