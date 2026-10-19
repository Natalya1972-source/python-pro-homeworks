from sqlalchemy import select

from db import Base, engine, SessionLocal
from models import Owner, Cat


# Створюємо таблиці в базі
Base.metadata.create_all(engine)


# ----------------------------------------
# CREATE
# ----------------------------------------

def create_data():
    with SessionLocal() as session:

        # Перевіряємо, чи вже є власник
        existing_owner = session.execute(
            select(Owner).where(Owner.email == "nataly@gmail.com")
        ).scalar_one_or_none()

        if existing_owner:
            print("Дані вже існують.")
            return

        owner = Owner(
            name="Наталя",
            email="nataly@gmail.com"
        )

        molly = Cat(
            name="Моллі",
            age=7,
            breed="мейн-кун",
            weight=10.5
        )

        panya = Cat(
            name="Паня",
            age=8,
            breed="домашня кішка",
            weight=4.5
        )

        # Додаємо котів власнику
        owner.cats.append(molly)
        owner.cats.append(panya)

        session.add(owner)
        session.commit()

        print("CREATE: власника і котів додано.")


# ----------------------------------------
# READ
# ----------------------------------------

def read_cats():
    with SessionLocal() as session:

        result = session.execute(
            select(Cat)
        )

        cats = result.scalars().all()

        print("\nREAD: список котів")

        for cat in cats:
            print(
                cat.id,
                cat.name,
                cat.age,
                cat.breed,
                cat.weight
            )


# ----------------------------------------
# UPDATE
# ----------------------------------------

def update_panya():
    with SessionLocal() as session:

        panya = session.execute(
            select(Cat).where(Cat.name == "Паня")
        ).scalar_one_or_none()

        if panya:
            panya.weight = 4.7
            session.commit()

            print(
                "\nUPDATE: вага Пані змінена на",
                panya.weight,
                "кг"
            )


# ----------------------------------------
# DELETE
# ----------------------------------------

def delete_test_cat():
    with SessionLocal() as session:

        owner = session.execute(
            select(Owner).where(Owner.email == "nataly@gmail.com")
        ).scalar_one()

        test_cat = Cat(
            name="Тестовий кіт",
            age=1,
            breed="невідома",
            weight=3.0,
            owner=owner
        )

        session.add(test_cat)
        session.commit()

        print("\nDELETE: тестового кота спочатку додано.")

        session.delete(test_cat)
        session.commit()

        print("DELETE: тестового кота видалено.")


# ----------------------------------------
# ONE-TO-MANY
# ----------------------------------------

def show_owner_with_cats():
    with SessionLocal() as session:

        owner = session.execute(
            select(Owner).where(Owner.email == "nataly@gmail.com")
        ).scalar_one()

        print("\nONE-TO-MANY:")
        print("Власник:", owner.name)

        for cat in owner.cats:
            print("-", cat.name)


# ----------------------------------------
# TRANSACTION + ROLLBACK
# ----------------------------------------

def rollback_example():
    with SessionLocal() as session:

        try:
            cat = Cat(
                name="Помилковий кіт",
                age=2,
                breed="невідома",
                weight=3.5,
                owner_id=999
            )

            session.add(cat)

            # Штучно створюємо помилку
            raise ValueError("Тестова помилка")

            session.commit()

        except Exception as error:
            session.rollback()

            print("\nROLLBACK:")
            print("Сталася помилка:", error)
            print("Зміни скасовано.")


# ----------------------------------------
# ЗАПУСК
# ----------------------------------------

create_data()
read_cats()
update_panya()
read_cats()
delete_test_cat()
show_owner_with_cats()
rollback_example()