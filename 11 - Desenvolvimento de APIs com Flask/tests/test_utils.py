from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest
from utils import eleva_quadrado, requires_role    # Importar os métodos


@pytest.mark.parametrize("test_input,expected", [(2, 4), (10, 100), (3, 9)])
def test_eleva_quadrado_sucesso(test_input, expected):
    resultado = eleva_quadrado(test_input)      # Executar o método
    assert resultado == expected                # Esperar o retorno

@pytest.mark.parametrize(
    "test_input,exc_class,msg",
    [
        ('a', TypeError, "unsupported operand type(s) for ** or pow(): 'str' and 'int'"),
        (None, TypeError, "unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'")
    ]
)
def test_eleva_quadrado_falha(test_input, exc_class, msg):
    with pytest.raises(exc_class) as exc:
        eleva_quadrado(test_input)
        # breakpoint()
    assert str(exc.value) == msg

# Criando o método de teste
def test_requires_role_success():   # cenário de sucesso
    mock_user = Mock()
    mock_user.role.name = "admin"

    mock_get_jwt_identity = patch("utils.get_jwt_identity")                     # não precisa fazer nenhum retorno
    mock_db_get_or_404 = patch("utils.db.get_or_404", return_value=mock_user)   # precisa retornar um usuário
    mock_get_jwt_identity.start()   # iniciar um recurso
    mock_db_get_or_404.start()      # iniciar um recurso

    decorated_function = requires_role("admin")(lambda: "sucesso")

    result = decorated_function()

    assert result == "sucesso"

    mock_get_jwt_identity.stop()    # parar um recurso
    mock_db_get_or_404.stop()       # parar um recurso


def test_requires_role_fail():   # cenário de falha
    mock_user = Mock()
    mock_user.role.name = "normal"

    mock_get_jwt_identity = patch("utils.get_jwt_identity")                     # não precisa fazer nenhum retorno
    mock_db_get_or_404 = patch("utils.db.get_or_404", return_value=mock_user)   # precisa retornar um usuário
    mock_get_jwt_identity.start()   # iniciar um recurso
    mock_db_get_or_404.start()      # iniciar um recurso

    decorated_function = requires_role("admin")(lambda: "sucesso")

    result = decorated_function()

    assert result == ({"message": "User haven't access."}, HTTPStatus.FORBIDDEN) # Tupla retorna dicionário e status

    mock_get_jwt_identity.stop()    # parar um recurso
    mock_db_get_or_404.stop()       # parar um recurso
