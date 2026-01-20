from data.db import get_connection

def get_products_by_category(category: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, price FROM products WHERE category = ?",
        (category,)
    )

    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name" : row[1],
            "price": row[2]
        })

    return products