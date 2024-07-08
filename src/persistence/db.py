"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)

Imports:
- `Base`: Base class for all models.
- `Repository`: Abstract base class for repositories.
- `db`: SQLAlchemy instance for database operations.
- `NoResultFound`: Exception raised when a query does not return any results.
- `User`: User model class.

Class: `DBRepository`
- Implements the `Repository` interface for database operations.

Methods:
1. `reload()`:
   - Purpose: Typically not needed for database repositories.
   - No implementation provided.

2. `get_all(model_name: str) -> list`:
   - Purpose: Retrieves all objects of a given model.
   - Parameters: `model_name` - The name of the model.
   - Returns: A list of all objects of the specified model.

3. `get(model_name: str, obj_id: str) -> Base | None`:
   - Purpose: Retrieves an object by its ID.
   - Parameters: 
     - `model_name` - The name of the model.
     - `obj_id` - The ID of the object.
   - Returns: The object if found, otherwise `None`.

4. `save(obj: Base) -> None`:
   - Purpose: Saves an object to the database.
   - Parameters: `obj` - The object to be saved.
   - Commits the transaction.

5. `update(obj: Base) -> None`:
   - Purpose: Updates an existing object in the database.
   - Parameters: `obj` - The object to be updated.
   - Commits the transaction.

6. `delete(obj: Base) -> bool`:
   - Purpose: Deletes an object from the database.
   - Parameters: `obj` - The object to be deleted.
   - Commits the transaction.
   - Returns: `True` after successful deletion.

7. `get_by_email(email: str) -> Base | None`:
   - Purpose: Retrieves a user object by email.
   - Parameters: `email` - The email of the user.
   - Returns: The user object if found, otherwise `None`.
   - Catches `NoResultFound` exception and returns `None` if no user is found.
"""

from src.models.base import Base
from src.persistence.repository import Repository
from src import db
from sqlalchemy.orm.exc import NoResultFound
from src.models import User

class DBRepository(Repository):
    """Database repository implementation"""

    def reload(self) -> None:
        """Reload data to the repository"""
        # This method is not typically needed for database repositories
        pass

    def get_all(self, model_name: str) -> list:
        """Get all objects of a model"""
        model_class = Base._decl_class_registry.get(model_name.capitalize())
        if model_class:
            return model_class.query.all()
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Get an object by id"""
        model_class = Base._decl_class_registry.get(model_name.capitalize())
        if model_class:
            return model_class.query.get(obj_id)
        return None

    def save(self, obj: Base) -> None:
        """Save an object"""
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Base) -> None:
        """Update an object"""
        db.session.commit()

    def delete(self, obj: Base) -> bool:
        """Delete an object"""
        db.session.delete(obj)
        db.session.commit()
        return True
    
    def get_by_email(self, email: str) -> Base | None:
        """Get a user object by email"""
        try:
            return User.query.filter_by(email=email).one()
        except NoResultFound:
            return None
