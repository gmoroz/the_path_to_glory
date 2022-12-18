import json
from flask_restx import Resource, Namespace
from flask import render_template, request, redirect, Response, session, make_response
from flask_bcrypt import check_password_hash
from project.container import user_service
from project.helpers import generate_tokens
from project.constants import HEADERS

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class RegisterView(Resource):
    def get(self):
        return make_response(render_template("sign_up.html"), 200, HEADERS)

    def post(self):
        if req_data := request.form.to_dict():
            user_service.create(req_data)
            return redirect("/auth/login/")


@auth_ns.route("/login/")
class LoginView(Resource):
    def get(self):
        return make_response(render_template("sign_in.html"), 200, HEADERS)

    def post(self):
        req_data = request.form.to_dict()
        user_d = user_service.get_user(req_data.get("username"))

        if user_d is not None:
            if not check_password_hash(user_d.password, req_data.get("password")):
                return Response(
                    response="Неправильный пароль. <a href='/auth/login/'>Попробовать еще раз</a>",
                    status=400,
                )
            tokens = generate_tokens(req_data)
            session["token"] = tokens.get("access_token")
            return redirect("/game")

        return Response(
            response="Неправильный логин. <a href='/auth/login/'>Попробовать еще раз</a>",
            status=400,
        )
