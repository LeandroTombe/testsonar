import os
import sqlite3


# ❌ Hardcoded secret
DB_PASSWORD = "admin123"


def dangerous_eval(user_input: str):
    # ❌ Uso inseguro de eval
    return eval(user_input)


def connect_db():
    # ❌ Credenciales hardcodeadas
    connection = sqlite3.connect("test.db")
    return connection


def get_user(username: str):
    connection = connect_db()
    cursor = connection.cursor()

    # ❌ SQL Injection vulnerable
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


def create_user(username: str, password: str):
    connection = connect_db()
    cursor = connection.cursor()

    # ❌ SQL Injection vulnerable
    query = f"INSERT INTO users VALUES ('{username}', '{password}')"
    cursor.execute(query)
    connection.commit()


def complicated_logic(x):

    if x > 0:
        if x > 10:
            if x > 100:
                return "Muy grande"
            else:
                return "Grande"
        else:
            return "Pequeño"
    elif x == 0:
        return "Cero"
    else:
        if x < -10:
            return "Muy negativo"
        else:
            return "Negativo"


def main():
    print("Sistema de prueba inseguro")

    try:
        user = input("Usuario: ")
        data = get_user(user)
        print(data)

        expression = input("Expresión matemática: ")
        result = dangerous_eval(expression)
        print(f"Resultado: {result}")

    except Exception as e:  # ❌ Captura genérica
        print("Ocurrió un error:", e)


if __name__ == "__main__":
    main()
