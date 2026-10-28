import re
from almyfit.repository import AlmyFitRepository


class ValidationError(ValueError):
    """Entrada del usuario inválida."""


class InventoryError(ValueError):
    """Operación no posible por falta de inventario."""


class AlmyFitService:
    """Aplica reglas de negocio y valida antes de guardar."""

    ALLOWED_CHANNELS = {"instagram", "whatsapp", "tiktok"}

    def __init__(self, repository: AlmyFitRepository):
        self.repository = repository

    def list_inventory(self):
        return self.repository.list_inventory()

    def register_sale(self, product_id, quantity, channel):
        if not isinstance(product_id, int) or product_id <= 0:
            raise ValidationError("El ID del producto debe ser un entero positivo.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValidationError("La cantidad debe ser un entero positivo.")
        normalized_channel = channel.strip().lower()
        if normalized_channel not in self.ALLOWED_CHANNELS:
            raise ValidationError("Canal inválido. Usa Instagram, WhatsApp o TikTok.")
        product = self.repository.get_product(product_id)
        if product is None:
            raise ValidationError("No existe un producto con ese ID.")
        if quantity > product["stock"]:
            raise InventoryError(f"Stock insuficiente. Disponible: {product['stock']}.")
        try:
            return self.repository.create_sale(product, quantity, normalized_channel.title())
        except (ValueError, ArithmeticError) as error:
            raise InventoryError("No fue posible registrar la venta; verifica el inventario.") from error

    def monthly_summary(self, year_month):
        if not isinstance(year_month, str) or not re.fullmatch(
            r"\d{4}-(0[1-9]|1[0-2])", year_month
        ):
            raise ValidationError("El mes debe tener formato AAAA-MM, por ejemplo 2026-10.")
        return self.repository.monthly_summary(year_month)

    def profit_ranking(self):
        return self.repository.profit_ranking()
