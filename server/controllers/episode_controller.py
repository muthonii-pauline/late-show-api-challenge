from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..app import db
from ..models.episode import Episode

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return {"error": "Episode not found"}, 404

    return {
        "id": ep.id,
        "date": ep.date,
        "number": ep.number,
        "appearances": [
            {"id": a.id, "guest": a.guest.name, "rating": a.rating}
            for a in ep.appearances
        ]
    }

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return {"error": "Not found"}, 404
    db.session.delete(ep)
    db.session.commit()
    return {"message": "Episode deleted"}, 200
