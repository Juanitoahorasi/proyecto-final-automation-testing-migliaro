# tests/ui/test_add_to_cart.py
import pytest

from config.settings import STANDARD_USER, STANDARD_PASSWORD
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger


PRODUCT_NAME = "Sauce Labs Backpack"


@pytest.mark.ui
def test_add_single_product_to_cart(driver, login_page):
    """
    Verifica que al agregar un producto desde el inventario:
    - El badge del carrito muestre la cantidad correcta.
    - El producto aparezca en la página del carrito.
    """
    logger.info("Running test_add_single_product_to_cart.")

    # Login
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    # Pasamos a la página de inventario
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "Inventory page should be loaded after login."

    # Agregamos un producto al carrito
    inventory_page.add_product_to_cart(PRODUCT_NAME)

    # Verificamos el número en el badge del carrito
    badge_count = inventory_page.get_cart_badge_count()
    assert badge_count == 1, f"Expected cart badge to show 1, but got {badge_count}."

    # Abrimos el carrito y verificamos que el producto esté presente
    inventory_page.open_cart()
    cart_page = CartPage(driver)

    products_in_cart = cart_page.get_products_in_cart()
    assert PRODUCT_NAME in products_in_cart, "Added product should be present in the cart."


@pytest.mark.ui
def test_remove_product_from_cart(driver, login_page):
    """
    Verifica que al eliminar un producto desde el carrito:
    - El producto deje de aparecer en la lista del carrito.
    - El badge del carrito se actualice correctamente (0 items).
    """
    logger.info("Running test_remove_product_from_cart.")

    # Login
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "Inventory page should be loaded after login."

    # Agregamos el producto y verificamos el badge
    inventory_page.add_product_to_cart(PRODUCT_NAME)
    assert inventory_page.get_cart_badge_count() == 1

    # Vamos al carrito
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    products_in_cart = cart_page.get_products_in_cart()
    assert PRODUCT_NAME in products_in_cart

    # Eliminamos el producto
    cart_page.remove_product(PRODUCT_NAME)

    # Comprobamos que ya no está en el carrito
    products_after_removal = cart_page.get_products_in_cart()
    assert PRODUCT_NAME not in products_after_removal, "Product should have been removed from cart."

    # Volvemos a inventario para verificar el badge (opcional pero ilustrativo)
    driver.back()  # vuelve a inventory
    updated_badge = inventory_page.get_cart_badge_count()
    assert updated_badge == 0, f"Expected cart badge 0 after removal, but got {updated_badge}."
