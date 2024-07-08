"""
Documentation for Flask Application Setup with SQLAlchemy:

Imports:
- `Flask`: The Flask class to create a Flask application instance.
- `SQLAlchemy`: SQLAlchemy class to handle database operations.

Application Setup:
1. `app = Flask(__name__)`:
   - Creates an instance of the Flask class.
   - `__name__` is used to determine the root path of the application.

2. `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'`:
   - Configures the Flask application to use SQLite as the database.
   - `SQLALCHEMY_DATABASE_URI`: Sets the URI for the SQLite database named `development.db`.

3. `db = SQLAlchemy(app)`:
   - Creates an instance of SQLAlchemy and associates it with the Flask application.
   - Enables the use of SQLAlchemy ORM for database operations within the Flask app.
"""


from .amenity import Amenity
from .base import Base
from .city import City
from .country import Country
from .place import Place
from .review import Review
from .user import User

__all__ = ['Amenity', 'Base', 'City', 'Country', 'Place', 'Review', 'User']
