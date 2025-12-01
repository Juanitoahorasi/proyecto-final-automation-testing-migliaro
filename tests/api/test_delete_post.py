# tests/api/test_delete_post.py
import pytest

from utils.logger import logger


@pytest.mark.api
def test_delete_post_returns_success_status(api_client):
    """
    Verifica que la petición DELETE /posts/1 devuelva un código de éxito (200 o 204).
    JSONPlaceholder no elimina realmente el recurso, pero responde adecuadamente.
    """
    logger.info("Running test_delete_post_returns_success_status.")

    response = api_client.delete("/posts/1")

    assert response.status_code in (200, 204), (
        f"Expected status code 200 or 204 for DELETE /posts/1, "
        f"but got {response.status_code}."
    )

    # Opcional: intentar parsear el body (suele ser vacío en JSONPlaceholder).
    try:
        _ = response.json()
    except ValueError:
        # Si no hay JSON, no es un fallo en sí.
        logger.info("DELETE /posts/1 returned no JSON body, which is acceptable.")
