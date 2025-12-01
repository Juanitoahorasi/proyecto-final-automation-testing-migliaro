# pages/inventory_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger import logger


class InventoryPage:
    """
    Page Object para la página de inventario de productos.
    Permite agregar/quitar productos del carrito y navegar al carrito.
    """

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_loaded(self) -> bool:
        """Verifica que la página de inventario esté cargada."""
        elements = self.driver.find_elements(*self.INVENTORY_CONTAINER)
        loaded = len(elements) > 0
        logger.info(f"Inventory page loaded: {loaded}")
        return loaded

    def _get_product_container_by_name(self, product_name: str):
        """
        Devuelve el contenedor de un producto dado su nombre.
        Se basa en el texto del elemento con clase 'inventory_item_name'.
        """
        products = self.driver.find_elements(*self.PRODUCT_NAME)
        for product in products:
            if product.text.strip() == product_name:
                # Comentario: subimos al contenedor padre del item.
                return product.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']")
        raise ValueError(f"Product with name '{product_name}' not found on inventory page.")

    def add_product_to_cart(self, product_name: str):
        """Hace clic en el botón 'Add to cart' del producto indicado."""
        logger.info(f"Adding product to cart: {product_name}")
        container = self._get_product_container_by_name(product_name)
        add_button = container.find_element(By.TAG_NAME, "button")
        add_button.click()

    def remove_product_from_cart(self, product_name: str):
        """
        Hace clic en el botón 'Remove' del producto indicado.
        Solo funciona si el producto ya está en el carrito.
        """
        logger.info(f"Removing product from cart: {product_name}")
        container = self._get_product_container_by_name(product_name)
        remove_button = container.find_element(By.TAG_NAME, "button")
        remove_button.click()

    def open_cart(self):
        """Abre la página del carrito haciendo clic en el ícono correspondiente."""
        logger.info("Opening cart page from inventory.")
        self.driver.find_element(*self.CART_ICON).click()

    def get_cart_badge_count(self) -> int:
        """Devuelve la cantidad de productos mostrada en el badge del carrito."""
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0
        text = badges[0].text.strip()
        return int(text) if text.isdigit() else 0
