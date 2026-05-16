import sqlite3
import re


def busca_usuario_por_email(email_digitado):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_digitado):
        raise ValueError("Formato de email inválido")

    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    query = "SELECT nome, email FROM usuarios WHERE email = ?"
    print(f"Executando query: {query}")

    cursor.execute(query, (email_digitado,))

    return cursor.fetchone()