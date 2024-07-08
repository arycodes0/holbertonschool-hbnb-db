"""
This module contains the routes for the places blueprint.

Imports:
- `jsonify`, `Blueprint`: Flask utilities for JSON responses and route organization.
- `create_place`, `delete_place`, `get_place_by_id`, `get_places`, `update_place`: Place-related controllers.
- `jwt_required`, `get_jwt_identity`: JWT utilities for authentication and retrieving user identity.
- `db`: Database access for place data.
- `wraps`: Helper for creating decorators.

Function: `check_place_permission(func)`:
- Purpose: Decorator to check if the current user has permission to access a specific place.
- Decorates a function to enforce authorization:
  - Ensures route is protected by JWT authentication.
  - Retrieves current user’s identity from the JWT.
  - Checks if the place exists and if the current user is the host.
  - Returns 404 if the place is not found.
  - Returns 401 if the user is unauthorized.

Blueprint: `places_bp`:
- Organizes routes under the `/places` prefix.

Routes:
- `GET /places`: Retrieves a list of places.
- `POST /places`: Creates a new place (requires JWT authentication).
- `GET /places/<place_id>`: Retrieves a specific place by `place_id`.
- `PUT /places/<place_id>`: Updates a specific place by `place_id` (requires JWT authentication and permission check).
- `DELETE /places/<place_id>`: Deletes a specific place by `place_id` (requires JWT authentication and permission check).

Example of a Protected Route:
- `GET /places/protected`: Returns the current user’s identity to demonstrate JWT usage.
"""


from flask import jsonify
from flask import Blueprint
from src.controllers.places import (
    create_place,
    delete_place,
    get_place_by_id,
    get_places,
    update_place,
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.persistence import db
from functools import wraps


def check_place_permission(func):
    @wraps(func)
    @jwt_required()
    def decorated_function(place_id, *args, **kwargs):
        current_user = get_jwt_identity()
        place = db.get('place', place_id)

        if not place:
            return jsonify({"msg": "Place not found"}), 404

        if current_user != place.host_id:
            return jsonify({"msg": "Unauthorized"}), 401

        return func(place_id, *args, **kwargs)

    return decorated_function

places_bp = Blueprint("places", __name__, url_prefix="/places")

places_bp.route("/", methods=["GET"])(get_places)
places_bp.route("/", methods=["POST"])(jwt_required()(create_place))

places_bp.route("/<place_id>", methods=["GET"])(get_place_by_id)
places_bp.route("/<place_id>", methods=["PUT"])(jwt_required()(check_place_permission(update_place)))
places_bp.route("/<place_id>", methods=["DELETE"])(jwt_required()(check_place_permission(delete_place)))

""" Below is an example of a protected route to demonstrate JWT usage. """
@places_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
