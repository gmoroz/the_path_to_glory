import json
from flask_restx import Resource, Namespace
from flask import render_template, request, redirect, Response, session
from project.container import user_service, user_schema
from project.helpers import check_password, generate_tokens

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class RegisterView(Resource):
    def get(self):
        return render_template("sign_up.html")

    def post(self):
        if req_data := request.form.to_dict():
            user_service.create(req_data)
            return redirect("/auth/login")


@auth_ns.route("/login")
class LoginView(Resource):
    def get(self):
        return render_template("sign_in.html")

    def post(self):
        req_data = request.form.to_dict()
        user_d = user_service.get_user(req_data.get("username"))

        if user_d is not None:
            if not check_password(req_data.get("password"), user_d.password):
                return Response(
                    response="Неправильный пароль. <a href='/auth/login/'>Попробовать еще раз</a>",
                    status=400,
                )
            user_string = user_schema.dumps(user_d)
            user_dict = json.loads(user_string)

            tokens = generate_tokens(user_dict)
            session["token"] = tokens.get("access_token")
        return Response(
            response="Неправильный логин. <a href='/auth/login/'>Попробовать еще раз</a>",
            status=400,
        )
