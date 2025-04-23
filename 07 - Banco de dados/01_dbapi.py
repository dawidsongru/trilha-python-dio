import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome VARCHAR(100), "
        "email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);",
        data
    )
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        "UPDATE clientes SET nome=?, email=? WHERE id=?;",
        data
    )
    conexao.commit()


# atualizar_registro(conexao, cursor, "joao1", "joao1@gmail.com", 1)
# atualizar_registro(conexao, cursor, "paulo1", "paulo1@gmail.com", 2)


def excluir_registro(conexao, cursor, id):
    # Quando for colocar uma tupla com um único valor, inserir uma vírgula
    data = (id,)
    cursor.execute(
        # Digitar comandos SQL em letras maiúsculas
        "DELETE FROM clientes WHERE id=?;",
        data
    )
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)",
        dados
    )
    conexao.commit()


# dados = [
#     ("ana", "ana@gmail.com"),
#     ("carlos", "carlos@gmail.com"),
#     ("fernando", "fernando@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)

# cursor.execute("SELECT * FROM minha_tabela WHERE id = l")
# result = cursor.fetchone()
# print(result)

# cursor.execute("SELECT * FROM minha_tabela")
# results = cursor.fetchall()
# for row in results:
#     print(row)


# # Recuperar cliente
# def recuperar_cliente(cursor, id):
#     cursor.execute("SELECT id, email FROM clientes WHERE id=?", (id,))
#     return cursor.fetchone()


# Recuperar cliente
def recuperar_cliente(cursor, id):
    # cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    cursor.execute("SELECT nome, id, email FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    # Ordem Crescente
    # return cursor.execute("SELECT * FROM clientes ORDER BY nome;")
    # Ordem Decrescente
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# Retornar os dados de todos os id's (clientes)
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])


print(f"Seja bem vindo ao sistema {cliente["nome"]}")
print(f"Seja bem vindo ao sistema {cliente[1]}")
