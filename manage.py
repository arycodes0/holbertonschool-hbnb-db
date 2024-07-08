"""
Entry point for the application. 

Documentation for Flask CLI Script:

Imports:
- `os`: Provides a way to interact with the operating system.
- `FlaskGroup` from `flask.cli`: Creates a Flask CLI for managing the application.
- `create_app` from `src`: Function to create the Flask application instance.
- `db, app` from `SQL.init_db`: Database and application instances.
- `database_exists`, `create_database` from `sqlalchemy_utils`: Functions to check for and create databases.

Setup:
1. `cli = FlaskGroup(create_app=create_app)`:
   - Creates a CLI group for managing the Flask application.

Function: `initialize_database()`:
- Checks the environment and initializes the database accordingly:
  - For development: Creates the database if it does not exist.
  - For production: Ensures the production database exists and runs initialization SQL script.

Main Execution:
1. `if __name__ == "__main__":`
   - Executes `initialize_database()` to set up the database.
   - Calls `cli()` to handle CLI commands.
"""


import os
from flask.cli import FlaskGroup
from src import create_app
from SQL.init_db import db, app
from sqlalchemy_utils import database_exists, create_database

cli = FlaskGroup(create_app=create_app)

def initialize_database():
    env = os.getenv('ENV', 'development')
    if env == 'development' and not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
        print("Development database created.")
    elif env == 'production':
        # Ensure production database exists and is initialized using db.sql
        os.system(f"psql -U user -d hbnb_prod -f SQL/db.sql")
        print("Production database initialized.")

if __name__ == "__main__":
    initialize_database()
    cli()
