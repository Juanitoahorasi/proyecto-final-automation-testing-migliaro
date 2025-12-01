# pages/checkout_complete_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger import logger


class CheckoutCompletePage:
    """
    Página de confirmación de compra (checkout completo).
    """

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_order_complete(self) -> bool:
        """
        Verifica que el mensaje de confirmación de la compra esté presente.
        """
        headers = self.driver.find_elements(*self.COMPLETE_HEADER)
        if not headers:
            logger.info("Order complete header not found.")
            return False

        text = headers[0].text.strip().upper()
        logger.info(f"Order complete header text: {text}")
        return "THANK YOU FOR YOUR ORDER" in text
