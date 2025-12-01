# tests/api/test_get_posts.py
import pytest

from utils.logger import logger


@pytest.mark.api
def test_get_posts_returns_list(api_client):
    """
    Verifica que la petición GET /posts devuelva:
    - Código de estado 200.
    - Una lista JSON no vacía.
    - Cada elemento con las claves esperadas.
    """
    logger.info("Running test_get_posts_returns_list.")
    response = api_client.get("/posts")

    assert response.status_code == 200, "Expected status code 200 for GET /posts."

    data = response.json()
    assert isinstance(data, list), "Response body should be a list."
    assert len(data) > 0, "Posts list should not be empty."

    required_keys = {"userId", "id", "title", "body"}
    first_post = data[0]
    assert required_keys.issubset(first_post.keys()), (
        f"First post should contain keys {required_keys}, but got {first_post.keys()}."
    )
