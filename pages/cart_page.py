# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger import logger


class CartPage:
    """
    Page Object para la página del carrito.
    Permite consultar productos y avanzar al checkout.
    """

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_products_in_cart(self) -> list[str]:
        """Devuelve una lista con los nombres de los productos en el carrito."""
        items = self.driver.find_elements(*self.CART_ITEM)
        product_names = []
        for item in items:
            name_element = item.find_element(*self.CART_ITEM_NAME)
            product_names.append(name_element.text.strip())
        logger.info(f"Products currently in cart: {product_names}")
        return product_names

    def remove_product(self, product_name: str):
        """
        Elimina un producto del carrito haciendo clic en su botón 'Remove'.
        """
        logger.info(f"Removing product from cart page: {product_name}")
        items = self.driver.find_elements(*self.CART_ITEM)
        for item in items:
            name_element = item.find_element(*self.CART_ITEM_NAME)
            if name_element.text.strip() == product_name:
                remove_button = item.find_element(By.TAG_NAME, "button")
                remove_button.click()
                return
        raise ValueError(f"Product '{product_name}' not found in cart to remove.")

    def click_checkout(self):
        """Hace clic en el botón 'Checkout' para iniciar el flujo de compra."""
        logger.info("Clicking checkout button on cart page.")
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
