# pages/checkout_overview_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger import logger


class CheckoutOverviewPage:
    """
    Página de resumen del checkout (Step Two).
    """

    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_finish(self):
        """Finaliza la compra haciendo clic en 'Finish'."""
        logger.info("Clicking finish button on checkout overview.")
        self.driver.find_element(*self.FINISH_BUTTON).click()
