"""
Database configuration and connection setup.
Creates SQLAlchemy engine and session factory.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CORRECT IMPORT - from config in same directory
from src.config import settings
print("Using DATABASE_URL:", settings.DATABASE_URL)

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=settings.DEBUG
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create base class for models
Base = declarative_base()


def get_db():
    """
    Get database session for dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all database tables. For development only."""
    Base.metadata.create_all(bind=engine)