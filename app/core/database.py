from urllib.parse import quote_plus
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

# Create connection URL from settings
connection_url = f'mysql://{settings.db_user}:{quote_plus(settings.db_password.get_secret_value())}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
engine = create_engine(connection_url)


def get_session():
    """Returns a new session.

    Returns:
        Session: A SQLModel session connected to the configured database.
    """
    return Session(engine)


def init_db():
    """Initializes the database by creating all tables defined in the models.

    This function should be called at the start of the application.
    """
    SQLModel.metadata.create_all(engine)
