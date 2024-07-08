""" This module contains the routes for the countries endpoint.

Summary of Routes and Comments:

Active Routes:
1. `get_countries`: Handles `GET` requests to `/countries` to retrieve a list of all countries.
2. `get_country_by_code`: Handles `GET` requests to `/countries/<code>` to retrieve a specific country by its code.
3. `get_country_cities`: Handles `GET` requests to `/countries/<code>/cities` to retrieve a list of cities in a specific country by its code.

Commented-Out Routes:
1. `create_country`: Commented out to prevent handling `POST` requests to `/countries` for creating a new country.
2. `update_country`: Commented out to prevent handling `PUT` requests to `/countries/<country_id>` for updating an existing country.
3. `delete_country`: Commented out to prevent handling `DELETE` requests to `/countries/<country_id>` for deleting an existing country.

Reasons for Commenting Out:
- The functions may be under development or not yet implemented.
- Temporarily disabling routes to control feature availability.
- Maintaining code cleanliness and preventing errors.
"""

from flask import Blueprint
from src.controllers.countries import (
    # create_country,
    get_countries,
    get_country_by_code,
    get_country_cities,
)

countries_bp = Blueprint("countries", __name__, url_prefix="/countries")

countries_bp.route("/", methods=["GET"])(get_countries)
countries_bp.route("/<code>", methods=["GET"])(get_country_by_code)
countries_bp.route("/<code>/cities", methods=["GET"])(get_country_cities)
# countries_bp.route("/", methods=["POST"])(create_country)

# countries_bp.route("/<country_id>", methods=["PUT"])(update_country)
# countries_bp.route("/<country_id>", methods=["DELETE"])(delete_country)