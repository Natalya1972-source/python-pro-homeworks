# ЗАВДАННЯ 1. СТВОРЕННЯ КЛАСІВ
# Опис товару
class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    # Метод змінює ціну
    def change_price(self, new_price):
        self.price = new_price

    # Вигляд об'єкта при print()
    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} грн"

# Товар на складі
class StockItem:
    """
    Кількість товару зберігається окремо від Product,
    оскільки кількість є характеристикою складу.
    """

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    # Метод змінює складський залишок
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity


# Клієнт
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    # Метод додає нове замовлення клієнту
    def add_order(self, order):
        self.orders.append(order)


# Одна позиція в замовленні
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    # Метод рахує вартість цієї позиції
    def total_price(self):
        return self.product.price * self.quantity


# Замовлення
class Order:
    def __init__(self):
        self.items = []
        self.total_amount = 0

    # Додає товар до замовлення
    def add_product(self, product, quantity=1):
        item = OrderItem(product, quantity)
        self.items.append(item)
        self.total_amount = self.calculate_total()

    # Обчислює загальну суму замовлення
    def calculate_total(self):
        return sum(item.total_price() for item in self.items)


# ЗАВДАННЯ 2. ВЗАЄМОДІЯ МІЖ КЛАСАМИ
# Зчитування початкових даних з файлу
def load_store_data(filename):
    products = {}
    stock = {}
    customers = {}

    section = None

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line == "[PRODUCTS]":
                section = "products"
                continue

            if line == "[CUSTOMERS]":
                section = "customers"
                continue

            if section == "products":
                name, category, price, quantity = line.split(";")

                product = Product(
                    name,
                    category,
                    float(price)
                )

                products[name] = product
                stock[name] = StockItem(
                    product,
                    int(quantity)
                )

            elif section == "customers":
                name, email = line.split(";")

                customers[email] = Customer(
                    name,
                    email
                )

    return products, stock, customers

# Завантажуємо початковий стан магазину
products, stock, customers = load_store_data("store_data.txt")

# Виводимо товари
print("Товари в магазині:")
for item in stock.values():
    print(
        item.product.name,
        "-",
        item.product.price,
        "грн, кількість:",
        item.quantity
    )

# Виводимо клієнтів
print("\nКлієнти:")
for customer in customers.values():
    print(customer.name, "-", customer.email)

# Створення замовлення
print("\nСтворення замовлення:")

customer = customers["nataly@gmail.com"]

order = Order()

# Наталя замовляє 2 ведмедики та 1 LEGO
order.add_product(products["Ведмедик"], 2)
order.add_product(products["LEGO City"], 1)

# Додаємо замовлення клієнту
customer.add_order(order)

# Зменшуємо залишок на складі
stock["Ведмедик"].change_quantity(
    stock["Ведмедик"].quantity - 2
)

stock["LEGO City"].change_quantity(
    stock["LEGO City"].quantity - 1
)

# Виводимо замовлення
print("Клієнт:", customer.name)

print("Товари в замовленні:")
for item in order.items:
    print(
        item.product.name,
        "-",
        item.quantity,
        "шт.",
        "-",
        item.total_price(),
        "грн"
    )

print("Загальна сума:", order.total_amount, "грн")

# Виводимо залишок після замовлення
print("\nЗалишок на складі:")
for item in stock.values():
    print(
        item.product.name,
        "-",
        item.quantity,
        "шт."
    )