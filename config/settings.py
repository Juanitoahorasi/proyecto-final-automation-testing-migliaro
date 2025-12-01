# config/settings.py
from pathlib import Path

# URL base del sitio a automatizar (UI)
BASE_URL = "https://www.saucedemo.com/"

# URL base de la API pública (JSONPlaceholder)
API_BASE_URL = "https://jsonplaceholder.typicode.com"

# Navegador a utilizar (por ahora solo Edge, pero se deja preparado por si se amplía)
BROWSER = "edge"

# Credenciales de prueba (hardcodeadas por simplicidad)
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"

# Timeout genérico para esperas implícitas
IMPLICIT_WAIT = 10  # segundos

# Directorios para artefactos (se crean si no existen)
ROOT_DIR = Path(__file__).resolve().parents[1]
SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
REPORTS_DIR = ROOT_DIR / "reports"

SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
