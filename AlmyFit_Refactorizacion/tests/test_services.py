import tempfile
import unittest
from pathlib import Path

from almyfit.database import Database
from almyfit.repository import AlmyFitRepository
from almyfit.services import AlmyFitService, ValidationError, InventoryError


class AlmyFitServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Database(str(Path(self.temp_dir.name) / "test.db"))
        self.database.initialize()
        self.repository = AlmyFitRepository(self.database)
        self.service = AlmyFitService(self.repository)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_inventory_has_demo_products(self):
        self.assertGreaterEqual(len(self.service.list_inventory()), 4)

    def test_valid_sale_reduces_stock(self):
        product = self.service.list_inventory()[0]
        before = product["stock"]
        sale = self.service.register_sale(product["id"], 1, "Instagram")
        self.assertEqual(self.repository.get_product(product["id"])["stock"], before - 1)
        self.assertGreaterEqual(sale["total"], 0)

    def test_zero_quantity_is_rejected(self):
        product = self.service.list_inventory()[0]
        with self.assertRaises(ValidationError):
            self.service.register_sale(product["id"], 0, "Instagram")

    def test_unknown_channel_is_rejected(self):
        product = self.service.list_inventory()[0]
        with self.assertRaises(ValidationError):
            self.service.register_sale(product["id"], 1, "CanalInventado")

    def test_insufficient_stock_is_rejected(self):
        product = self.service.list_inventory()[0]
        with self.assertRaises(InventoryError):
            self.service.register_sale(product["id"], product["stock"] + 1, "WhatsApp")

    def test_invalid_month_is_rejected(self):
        with self.assertRaises(ValidationError):
            self.service.monthly_summary("octubre-2026")


if __name__ == "__main__":
    unittest.main()
