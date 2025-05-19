import pytest
from app import create_app, db


@pytest.fixture()   # Método que cria e devolve o app
def app():
    app = create_app(
        {
            "SECRET_KEY": "test",
            "SQLALCHEMY_DATABASE_URI": "sqlite://", # O banco de dados vai rodar em memória, ele não vai criar...
            "JWT_SECRET_KEY": "test",               #... um arquivo físico, ele vai armazenar tudo na memória.
        }
    )
    with app.app_context():
        db.create_all()
        yield app


@pytest.fixture()
def client(app):
    return app.test_client()
