from almyfit.database import Database
from almyfit.repository import AlmyFitRepository
from almyfit.services import AlmyFitService, ValidationError, InventoryError


def print_menu():
    print("\n=== ALMY FIT | Ventas e inventario ===")
    print("1. Ver inventario")
    print("2. Registrar venta")
    print("3. Resumen mensual")
    print("4. Ranking de ganancia")
    print("5. Salir")


def run_app():
    database = Database()
    database.initialize()
    service = AlmyFitService(AlmyFitRepository(database))

    while True:
        print_menu()
        option = input("Selecciona una opción: ").strip()
        try:
            if option == "1":
                for p in service.list_inventory():
                    print(f"#{p['id']} {p['name']} | {p['category']} | talla {p['size']} | "
                          f"stock {p['stock']} | precio ${p['price']:.2f}")
            elif option == "2":
                product_id = int(input("ID del producto: ").strip())
                quantity = int(input("Cantidad: ").strip())
                channel = input("Canal (Instagram/WhatsApp/TikTok): ").strip()
                sale = service.register_sale(product_id, quantity, channel)
                print(f"Venta #{sale['id']} registrada. Total ${sale['total']:.2f}; "
                      f"ganancia ${sale['profit']:.2f}")
            elif option == "3":
                result = service.monthly_summary(input("Mes (AAAA-MM): ").strip())
                print(f"Ventas: {result['sales_count']} | ingresos ${result['revenue']:.2f} | "
                      f"ganancia ${result['profit']:.2f}")
            elif option == "4":
                for item in service.profit_ranking():
                    print(f"{item['product_name']}: ${item['profit']:.2f}")
            elif option == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")
        except (ValueError, ValidationError, InventoryError) as error:
            print(f"No se pudo completar la operación: {error}")
        except Exception:
            print("Ocurrió un error inesperado. Revisa los registros o contacta soporte.")


if __name__ == "__main__":
    run_app()
