# utils/logger.py
import logging
from pathlib import Path
from config.settings import ROOT_DIR

# Archivo de log dentro del proyecto
LOG_FILE = Path(ROOT_DIR) / "test_execution.log"

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,  # Nivel de log por defecto
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()  # También imprime en consola
    ],
)

# Logger global a reutilizar en todo el proyecto
logger = logging.getLogger("automation_tests")

# Nota: se usa un único logger sencillo según tu preferencia.
