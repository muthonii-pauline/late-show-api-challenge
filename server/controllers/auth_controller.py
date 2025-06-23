from flask import Blueprint, request, jsonify
from server.app import db
from server.models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__, url_prefix="/")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.username)
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
