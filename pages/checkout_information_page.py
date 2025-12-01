# pages/checkout_information_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger import logger


class CheckoutInformationPage:
    """
    Página de Checkout: información del comprador (Step One).
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        """Completa los campos requeridos con los datos indicados."""
        logger.info("Filling checkout information.")
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

        self.driver.find_element(*self.POSTAL_CODE_INPUT).clear()
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continue_to_overview(self):
        """Avanza a la página de resumen del checkout."""
        logger.info("Continuing to checkout overview.")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
