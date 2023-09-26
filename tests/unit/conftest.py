import pytest


@pytest.fixture(scope="module")
def app():
    from app.main import app

    app.config.update({"TESTING": True})

    return app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()
