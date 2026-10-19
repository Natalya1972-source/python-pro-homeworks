import sqlite3


# Підключаємося до бази даних
connection = sqlite3.connect("cats.db")
cursor = connection.cursor()

# Вмикаємо підтримку зовнішніх ключів
cursor.execute("PRAGMA foreign_keys = ON")


# ==================================================
# 1. DDL - СТВОРЕННЯ СТРУКТУРИ БАЗИ ДАНИХ
# ==================================================

# Видаляємо старі таблиці, щоб програму можна було запускати повторно
cursor.execute("DROP TABLE IF EXISTS feeding")
cursor.execute("DROP TABLE IF EXISTS cats")
cursor.execute("DROP TABLE IF EXISTS owners")


# Таблиця власників
cursor.execute("""
CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")


# Таблиця котів
cursor.execute("""
CREATE TABLE cats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    breed TEXT,
    weight REAL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
)
""")


# Таблиця харчових уподобань
cursor.execute("""
CREATE TABLE feeding (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cat_id INTEGER NOT NULL,
    favorite_food TEXT,
    FOREIGN KEY (cat_id) REFERENCES cats(id)
)
""")


# ==================================================
# 2. ІНДЕКС
# ==================================================

cursor.execute("""
CREATE INDEX idx_owners_email
ON owners(email)
""")


# ==================================================
# 3. DML - ДОДАВАННЯ ДАНИХ
# ==================================================

cursor.execute("""
INSERT INTO owners (name, email)
VALUES (?, ?)
""", ("Наталя", "nataly@gmail.com"))

owner_id = cursor.lastrowid


cursor.execute("""
INSERT INTO cats (name, age, breed, weight, owner_id)
VALUES (?, ?, ?, ?, ?)
""", ("Моллі", 7, "мейн-кун", 10.5, owner_id))

molly_id = cursor.lastrowid


cursor.execute("""
INSERT INTO cats (name, age, breed, weight, owner_id)
VALUES (?, ?, ?, ?, ?)
""", ("Паня", 8, "домашня кішка", 4.5, owner_id))

panya_id = cursor.lastrowid


cursor.execute("""
INSERT INTO feeding (cat_id, favorite_food)
VALUES (?, ?)
""", (molly_id, "курочка"))


cursor.execute("""
INSERT INTO feeding (cat_id, favorite_food)
VALUES (?, ?)
""", (panya_id, "риба"))


connection.commit()


# ==================================================
# 4. SELECT - ОТРИМАННЯ ДАНИХ
# ==================================================

print("Усі коти:")

cursor.execute("""
SELECT name, age, breed, weight
FROM cats
""")

for cat in cursor.fetchall():
    print(cat)


# ==================================================
# 5. ФІЛЬТРАЦІЯ
# ==================================================

print("\nКоти віком від 8 років:")

cursor.execute("""
SELECT name, age
FROM cats
WHERE age >= 8
""")

for cat in cursor.fetchall():
    print(cat)


# ==================================================
# 6. JOIN - ВЛАСНИК І ЙОГО КОТИ
# ==================================================

print("\nВласник та його коти:")

cursor.execute("""
SELECT owners.name, cats.name
FROM owners
JOIN cats ON owners.id = cats.owner_id
""")

for row in cursor.fetchall():
    print(row)


# ==================================================
# 7. JOIN - КІТ ТА УЛЮБЛЕНА ЇЖА
# ==================================================

print("\nУлюблена їжа котів:")

cursor.execute("""
SELECT cats.name, feeding.favorite_food
FROM cats
JOIN feeding ON cats.id = feeding.cat_id
""")

for row in cursor.fetchall():
    print(row)


# ==================================================
# 8. GROUP BY + COUNT
# ==================================================

print("\nКількість котів у власника:")

cursor.execute("""
SELECT owners.name, COUNT(cats.id)
FROM owners
JOIN cats ON owners.id = cats.owner_id
GROUP BY owners.id
""")

for row in cursor.fetchall():
    print(row)


# Закриваємо з'єднання
connection.close()