from typing import Any


class AlmyFitRepository:
    """Centraliza consultas SQL y persistencia; no contiene reglas de negocio."""

    def __init__(self, database):
        self.database = database

    def list_inventory(self) -> list[dict[str, Any]]:
        with self.database.session() as connection:
            rows = connection.execute(
                """SELECT id, name, category, size, color, stock, cost, price
                   FROM products ORDER BY name"""
            ).fetchall()
        return [dict(row) for row in rows]

    def get_product(self, product_id: int):
        with self.database.session() as connection:
            row = connection.execute(
                """SELECT id, name, category, size, color, stock, cost, price
                   FROM products WHERE id = ?""",
                (product_id,),
            ).fetchone()
        return dict(row) if row else None

    def create_sale(self, product, quantity, channel):
        with self.database.session() as connection:
            connection.execute("BEGIN")
            cursor = connection.execute(
                """INSERT INTO sales
                   (product_id, product_name, quantity, unit_price, unit_cost, channel)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (product["id"], product["name"], quantity, product["price"], product["cost"], channel),
            )
            updated = connection.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?",
                (quantity, product["id"], quantity),
            )
            if updated.rowcount != 1:
                raise ValueError("El inventario cambió o no hay unidades suficientes.")
            sale_id = cursor.lastrowid
        return {"id": sale_id, "total": product["price"] * quantity,
                "profit": (product["price"] - product["cost"]) * quantity}

    def monthly_summary(self, year_month):
        with self.database.session() as connection:
            row = connection.execute(
                """SELECT COUNT(*) AS sales_count,
                          COALESCE(SUM(quantity * unit_price), 0) AS revenue,
                          COALESCE(SUM(quantity * (unit_price - unit_cost)), 0) AS profit
                   FROM sales WHERE substr(sold_at, 1, 7) = ?""",
                (year_month,),
            ).fetchone()
        return dict(row)

    def profit_ranking(self):
        with self.database.session() as connection:
            rows = connection.execute(
                """SELECT product_name,
                          SUM(quantity * (unit_price - unit_cost)) AS profit
                   FROM sales GROUP BY product_name ORDER BY profit DESC"""
            ).fetchall()
        return [dict(row) for row in rows]
