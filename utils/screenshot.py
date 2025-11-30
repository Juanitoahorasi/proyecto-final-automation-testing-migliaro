# utils/screenshot.py
from datetime import datetime
from pathlib import Path

from config.settings import SCREENSHOTS_DIR
from utils.logger import logger


def take_screenshot(driver, test_name: str) -> Path:
    """
    Toma una captura de pantalla del estado actual del navegador.

    :param driver: instancia actual de WebDriver.
    :param test_name: nombre del test para incluir en el archivo.
    :return: ruta completa al archivo de screenshot generado.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Comentario: se limpia el nombre del test para que sea un nombre de archivo válido.
    safe_test_name = test_name.replace("/", "_").replace("\\", "_").replace(" ", "_")

    file_name = f"{safe_test_name}_{timestamp}.png"
    file_path = SCREENSHOTS_DIR / file_name

    driver.save_screenshot(str(file_path))
    logger.error(f"Screenshot captured for failed test: {file_path}")

    return file_path
