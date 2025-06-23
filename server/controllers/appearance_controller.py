from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from ..models.appearance import Appearance
from ..models.guest import Guest
from ..models.episode import Episode
from ..app import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')

    if not (1 <= rating <= 5):
        return {"error": "Rating must be 1-5"}, 400

    guest = Guest.query.get(data.get("guest_id"))
    episode = Episode.query.get(data.get("episode_id"))

    if not guest or not episode:
        return {"error": "Guest or Episode not found"}, 404

    a = Appearance(rating=rating, guest_id=guest.id, episode_id=episode.id)
    db.session.add(a)
    db.session.commit()
    return {"message": "Appearance created", "id": a.id}, 201
