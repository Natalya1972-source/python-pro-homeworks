from fastapi import FastAPI
from pydantic import BaseModel


# Створюємо FastAPI-застосунок
app = FastAPI(title="Коти-переселенці")


# Pydantic-модель кота
class Cat(BaseModel):
    name: str
    age: int
    breed: str
    weight: float
    favorite_food: str


# Імітація бази даних
cats = [
    {
        "id": 1,
        "name": "Моллі",
        "age": 7,
        "breed": "мейн-кун",
        "weight": 10.5,
        "favorite_food": "курочка"
    },
    {
        "id": 2,
        "name": "Паня",
        "age": 8,
        "breed": "домашня кішка",
        "weight": 4.5,
        "favorite_food": "риба"
    }
]


# Головний маршрут
@app.get("/")
async def home():
    return {
        "message": "API котів-переселенців працює"
    }


# Отримати список усіх котів
@app.get("/cats")
async def get_cats():
    return cats


# Отримати одного кота за ID
@app.get("/cats/{cat_id}")
async def get_cat(cat_id: int):
    for cat in cats:
        if cat["id"] == cat_id:
            return cat

    return {
        "error": "Кота не знайдено"
    }


# Додати нового кота
@app.post("/cats")
async def create_cat(cat: Cat):

    new_cat = {
        "id": len(cats) + 1,
        "name": cat.name,
        "age": cat.age,
        "breed": cat.breed,
        "weight": cat.weight,
        "favorite_food": cat.favorite_food
    }

    cats.append(new_cat)

    return new_cat