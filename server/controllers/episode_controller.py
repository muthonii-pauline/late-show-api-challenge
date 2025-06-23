from flask import Blueprint, jsonify, request
from server.app import db
from server.models.episode import Episode
from flask_jwt_extended import jwt_required

episode_bp = Blueprint("episode", __name__, url_prefix="/episodes")

@episode_bp.route("", methods=["GET"])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": ep.id, "date": ep.date, "number": ep.number} for ep in episodes]), 200

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    return jsonify({
        "id": ep.id,
        "date": ep.date,
        "number": ep.number,
        "appearances": [{"guest": a.guest.name, "rating": a.rating} for a in ep.appearances]
    }), 200

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200
