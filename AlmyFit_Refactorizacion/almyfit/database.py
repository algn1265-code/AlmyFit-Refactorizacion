import sqlite3
from contextlib import contextmanager


class Database:
    """Responsable de las conexiones y la preparación del esquema."""

    def __init__(self, database_path="almyfit.db"):
        self.database_path = database_path

    def connect(self):
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    @contextmanager
    def session(self):
        """Abre una conexión y garantiza commit/rollback y cierre del archivo."""
        connection = self.connect()
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def initialize(self):
        schema = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            size TEXT NOT NULL,
            color TEXT NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >= 0),
            cost REAL NOT NULL CHECK(cost >= 0),
            price REAL NOT NULL CHECK(price >= 0)
        );
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            unit_price REAL NOT NULL CHECK(unit_price >= 0),
            unit_cost REAL NOT NULL CHECK(unit_cost >= 0),
            channel TEXT NOT NULL,
            sold_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY(product_id) REFERENCES products(id)
        );
        """
        with self.session() as connection:
            connection.executescript(schema)
            count = connection.execute("SELECT COUNT(*) FROM products").fetchone()[0]
            if count == 0:
                connection.executemany(
                    """INSERT INTO products
                    (name, category, size, color, stock, cost, price)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    [
                        ("Legging Sculpt", "Leggings", "M", "Negro", 12, 45000, 85000),
                        ("Top Active", "Top", "S", "Lila", 8, 28000, 55000),
                        ("Conjunto Aura", "Conjunto", "L", "Azul", 5, 70000, 125000),
                        ("Legging Flex", "Leggings", "S", "Negro", 3, 42000, 80000),
                    ],
                )
