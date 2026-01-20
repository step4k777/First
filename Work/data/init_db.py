from db import get_connection

def init():
    conn = get_connection()
    cursor = conn.cursor()

    # Таблица товаров
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        category TEXT NOT NULL
    )
    """)

    # Чистим старые данные (чтобы не дублировались при повторном запуске)
    cursor.execute("DELETE FROM products")

    # Товары
    products = [
        ("Elden Ring", 2990, "rpg"),
        ("Witcher 3", 1490, "rpg"),
        ("Skyrim", 990, "rpg"),

        ("CS2 Prime", 1290, "shooter"),
        ("Call of Duty", 3990, "shooter"),

        ("Civilization VI", 1990, "strategy"),
        ("Total War: Rome II", 2490, "strategy")
    ]

    cursor.executemany(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        products
    )

    conn.commit()
    conn.close()
    print("✅ База данных создана и заполнена")

if __name__ == "__main__":
    init()