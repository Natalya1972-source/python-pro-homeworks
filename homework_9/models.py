from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Owner(Base):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    # Один власник може мати багато котів
    cats: Mapped[list["Cat"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan"
    )


class Cat(Base):
    __tablename__ = "cats"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    breed: Mapped[str]
    weight: Mapped[float]

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("owners.id")
    )

    # Кожен кіт має одного власника
    owner: Mapped["Owner"] = relationship(
        back_populates="cats"
    )