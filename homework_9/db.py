from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# Створюємо SQLite-базу
engine = create_engine(
    "sqlite:///cats_orm.db",
    echo=False
)


# Базовий клас для ORM-моделей
class Base(DeclarativeBase):
    pass


# Фабрика сесій
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)