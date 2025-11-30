# utils/driver_factory.py
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from config.settings import BROWSER, IMPLICIT_WAIT
from utils.logger import logger


def create_driver():
    """
    Crea y devuelve una instancia de WebDriver según el navegador configurado.
    Actualmente solo soporta Edge para simplificar el proyecto.
    """
    if BROWSER.lower() != "edge":
        # Comentario en español: por simplicidad, solo soportamos Edge en este proyecto.
        raise ValueError("Only Microsoft Edge browser is supported in this project.")

    edge_options = EdgeOptions()
    # Comentario: se pueden agregar opciones extra si las necesitás (por ej. modo headless).

    # Comentario: asumimos que msedgedriver está en el PATH del sistema.
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=edge_options)

    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)

    logger.info("Edge WebDriver created and configured.")
    return driver
