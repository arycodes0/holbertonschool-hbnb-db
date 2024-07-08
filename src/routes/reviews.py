"""
This module contains the routes for the reviews blueprint.

Blueprint: `reviews_bp`
- Organizes routes under the reviews module.

Routes:
- `POST /places/<place_id>/reviews`:
  - Creates a new review for a place (requires JWT authentication).
  - Handler: `create_review`

- `GET /places/<place_id>/reviews`:
  - Retrieves all reviews for a specific place.
  - Handler: `get_reviews_from_place`

- `GET /users/<user_id>/reviews`:
  - Retrieves all reviews from a specific user.
  - Handler: `get_reviews_from_user`

- `GET /reviews`:
  - Retrieves all reviews.
  - Handler: `get_reviews`

- `GET /reviews/<review_id>`:
  - Retrieves a specific review by its ID.
  - Handler: `get_review_by_id`

- `PUT /reviews/<review_id>`:
  - Updates a specific review by its ID.
  - Handler: `update_review`

- `DELETE /reviews/<review_id>`:
  - Deletes a specific review by its ID.
  - Handler: `delete_review`
"""


from flask import Blueprint
from src.controllers.reviews import (
    create_review,
    delete_review,
    get_reviews_from_place,
    get_reviews_from_user,
    get_review_by_id,
    get_reviews,
    update_review,
)

reviews_bp = Blueprint("reviews", __name__)

reviews_bp.route("/places/<place_id>/reviews", methods=["POST"])(create_review)
reviews_bp.route("/places/<place_id>/reviews")(get_reviews_from_place)
reviews_bp.route("/users/<user_id>/reviews")(get_reviews_from_user)

reviews_bp.route("/reviews", methods=["GET"])(get_reviews)

reviews_bp.route("/reviews/<review_id>", methods=["GET"])(get_review_by_id)
reviews_bp.route("/reviews/<review_id>", methods=["PUT"])(update_review)
reviews_bp.route("/reviews/<review_id>", methods=["DELETE"])(delete_review)
