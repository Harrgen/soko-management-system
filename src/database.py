"""
Database configuration and connection setup.
Creates SQLAlchemy engine and session factory.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Check connection before using
    echo=settings.DEBUG   # Show SQL queries in debug mode
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
    
    Yields:
        Session: Database session
        
    Example:
        >>> db = next(get_db())
        >>> db.query(User).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all database tables. For development only."""
    Base.metadata.create_all(bind=engine)