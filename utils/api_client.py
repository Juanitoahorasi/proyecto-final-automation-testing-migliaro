# utils/api_client.py
import requests

from config.settings import API_BASE_URL
from utils.logger import logger


class ApiClient:
    """
    Cliente HTTP simple para interactuar con JSONPlaceholder (o cualquier API base similar).
    Usa la librería 'requests' y registra en el logger las operaciones básicas.
    """

    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url.rstrip("/")

    def _build_url(self, endpoint: str) -> str:
        """Construye la URL completa a partir del endpoint."""
        endpoint = endpoint.lstrip("/")
        return f"{self.base_url}/{endpoint}"

    def get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        """Realiza una petición GET."""
        url = self._build_url(endpoint)
        logger.info(f"API GET -> {url} | params={params}")
        response = requests.get(url, params=params)
        logger.info(f"API GET <- status_code={response.status_code}")
        return response

    def post(self, endpoint: str, json: dict | None = None) -> requests.Response:
        """Realiza una petición POST con body JSON."""
        url = self._build_url(endpoint)
        logger.info(f"API POST -> {url} | json={json}")
        response = requests.post(url, json=json)
        logger.info(f"API POST <- status_code={response.status_code}")
        return response

    def delete(self, endpoint: str) -> requests.Response:
        """Realiza una petición DELETE."""
        url = self._build_url(endpoint)
        logger.info(f"API DELETE -> {url}")
        response = requests.delete(url)
        logger.info(f"API DELETE <- status_code={response.status_code}")
        return response
