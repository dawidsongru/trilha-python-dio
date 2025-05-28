from http import HTTPStatus

from app import Role, User, db

def test_get_user_success(client):              # Testando um comportamento de sucesso
    # Given (O que eu forneço para meu teste)
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user = User(username="john-doe", password="test", role_id=role.id)
    db.session.add(user)
    db.session.commit()

    # When (O que eu executo)
    response = client.get(f"/users/{user.id}")

    # Then (O que eu verifico)
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"id": user.id, "username": user.username}  # Verifica o conteúdo de retorno. Retorna id e username.

def test_get_user_not_found(client):            # Testando um comportamento de falha
    # Given (O que eu forneço para meu teste)
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user_id = 1

    # When (O que eu executo)
    response = client.get(f"/users/{user_id}")

    # Then (O que eu verifico)
    assert response.status_code == HTTPStatus.NOT_FOUND
