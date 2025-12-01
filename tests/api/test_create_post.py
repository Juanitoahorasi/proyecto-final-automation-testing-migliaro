# tests/api/test_create_post.py
import pytest

from utils.logger import logger


@pytest.mark.api
def test_create_post_returns_created_resource(api_client):
    """
    Verifica que la petición POST /posts:
    - Devuelva un código de estado 201.
    - Devuelva un objeto JSON con los datos enviados.
    - Incluya un 'id' generado.
    Nota: JSONPlaceholder no crea realmente el recurso,
    pero simula correctamente la respuesta.
    """
    logger.info("Running test_create_post_returns_created_resource.")

    payload = {
        "title": "Automation test post",
        "body": "This is a test post created by automated tests.",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201, "Expected status code 201 for POST /posts."

    data = response.json()
    for key, value in payload.items():
        assert data.get(key) == value, f"Expected '{key}'='{value}' in response."

    assert "id" in data, "Response should contain an 'id' field for the created post."
