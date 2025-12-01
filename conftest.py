# conftest.py
import pytest

from config.settings import BASE_URL
from utils.driver_factory import create_driver
from utils.logger import logger
from utils.screenshot import take_screenshot
from utils.api_client import ApiClient
from pages.login_page import LoginPage

try:
    # Comentario: pytest-html se usa solo si está instalado (se declara en requirements).
    import pytest_html  # type: ignore
except ImportError:  # pragma: no cover - defensa por si faltara el plugin
    pytest_html = None


@pytest.fixture(scope="session")
def base_url():
    """Devuelve la URL base del sitio. Útil si se necesita en varios tests."""
    return BASE_URL


@pytest.fixture()
def driver():
    """
    Fixture principal de WebDriver.
    Crea el navegador antes de cada test y lo cierra al finalizar.
    """
    logger.info("Starting WebDriver for test.")
    driver_instance = create_driver()
    yield driver_instance
    logger.info("Quitting WebDriver for test.")
    driver_instance.quit()


@pytest.fixture()
def login_page(driver):
    """
    Fixture que provee una instancia de LoginPage ya asociada al driver.
    Abre la página de login antes de cada test que lo use.
    """
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture(scope="session")
def api_client():
    """
    Fixture de sesión que provee un cliente de API.
    Esto evita recrear la instancia en cada test de API.
    """
    logger.info("Creating ApiClient for API tests.")
    return ApiClient()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que se ejecuta después de cada fase del test.
    Aquí detectamos fallos y, si el test usa el fixture 'driver',
    tomamos una captura de pantalla automática.
    """
    outcome = yield
    report = outcome.get_result()

    # Solo queremos actuar en la fase de ejecución principal del test
    if report.when != "call":
        return

    if report.failed:
        driver_instance = item.funcargs.get("driver", None)
        if driver_instance is not None:
            screenshot_path = take_screenshot(driver_instance, item.name)

            # Si pytest-html está disponible, agregamos la ruta de la captura como texto en el reporte.
            if pytest_html is not None:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.text(f"Screenshot: {screenshot_path}"))
                report.extra = extra
