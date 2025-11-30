# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import BASE_URL
from utils.logger import logger


class LoginPage:
    """
    Page Object para la página de login de Saucedemo.
    Representa los elementos y acciones principales del usuario.
    """

    # Localizadores de la página
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        """Abre la página de login usando la URL base."""
        logger.info("Opening login page.")
        self.driver.get(BASE_URL)

    def set_username(self, username: str):
        """Escribe el usuario en el campo correspondiente."""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password: str):
        """Escribe la contraseña en el campo correspondiente."""
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Hace clic en el botón de login."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        """
        Flujo completo de login: abre la página (si es necesario),
        completa las credenciales y hace clic en el botón.
        """
        logger.info(f"Attempting login with user '{username}'.")
        # Comentario: los tests pueden llamar open() antes si necesitan control granular.
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Devuelve el texto del mensaje de error si existe, vacío si no."""
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        if not elements:
            return ""
        return elements[0].text.strip()
