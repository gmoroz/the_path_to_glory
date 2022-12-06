from flask_restx import Namespace, Resource
from flask import request
from project.container import arena

fight_ns = Namespace("fight")


@fight_ns.route("/")
class FightView(Resource):
    def get(self):
        
