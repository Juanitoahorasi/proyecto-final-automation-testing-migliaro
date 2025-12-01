# tests/ui/test_checkout.py
import pytest

from config.settings import STANDARD_USER, STANDARD_PASSWORD
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import logger


PRODUCTS_TO_BUY = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]


@pytest.mark.ui
def test_successful_checkout_flow(driver, login_page):
    """
    Verifica un flujo completo de compra:
    - Login con usuario válido.
    - Agregar varios productos al carrito.
    - Iniciar checkout desde el carrito.
    - Completar datos del comprador.
    - Finalizar la compra y verificar mensaje de confirmación.
    """
    logger.info("Running test_successful_checkout_flow.")

    # Login
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "Inventory page should be loaded after login."

    # Agregamos varios productos al carrito
    for product_name in PRODUCTS_TO_BUY:
        inventory_page.add_product_to_cart(product_name)

    # Verificamos que el badge coincide con la cantidad de productos seleccionados
    badge_count = inventory_page.get_cart_badge_count()
    assert badge_count == len(PRODUCTS_TO_BUY), (
        f"Expected cart badge {len(PRODUCTS_TO_BUY)}, but got {badge_count}."
    )

    # Vamos al carrito
    inventory_page.open_cart()
    cart_page = CartPage(driver)
    products_in_cart = cart_page.get_products_in_cart()
    for product_name in PRODUCTS_TO_BUY:
        assert product_name in products_in_cart, "All selected products should be in cart."

    # Iniciamos checkout
    cart_page.click_checkout()

    # Completamos información del comprador
    info_page = CheckoutInformationPage(driver)
    info_page.fill_information("Juan", "Tester", "12345")
    info_page.continue_to_overview()

    # Resumen y finalización de la compra
    overview_page = CheckoutOverviewPage(driver)
    overview_page.click_finish()

    # Página de confirmación
    complete_page = CheckoutCompletePage(driver)
    assert complete_page.is_order_complete(), "Order should be completed successfully."
