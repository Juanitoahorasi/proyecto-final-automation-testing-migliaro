# tests/UI/test_login.py
import pytest

from config.settings import STANDARD_USER, STANDARD_PASSWORD
from utils.logger import logger


@pytest.mark.ui
def test_login_success(driver, login_page):
    """
    Verifica que un usuario válido pueda iniciar sesión correctamente.

    Flujo:
    - Abrir la página de login (lo hace el fixture login_page).
    - Ingresar credenciales válidas.
    - Verificar que la URL cambie a la página de inventario.
    """
    logger.info("Running test_login_success.")
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    # Comprobamos que estamos en la página de inventario
    current_url = driver.current_url
    assert "inventory" in current_url, (
        f"Expected to be on inventory page, but current URL is: {current_url}"
    )


@pytest.mark.ui
def test_login_invalid_credentials(driver, login_page):
    """
    Verifica que el sistema muestre un mensaje de error
    cuando se ingresan credenciales inválidas (escenario negativo).
    """
    logger.info("Running test_login_invalid_credentials.")
    invalid_password = STANDARD_PASSWORD + "x"
    login_page.login(STANDARD_USER, invalid_password)

    error_message = login_page.get_error_message()

    # Comprobamos que exista mensaje de error
    assert error_message != "", "Expected an error message for invalid credentials."

    # Comprobación suave de contenido esperado (puede ajustarse según el texto real)
    assert "Epic sadface" in error_message or "Username and password" in error_message
