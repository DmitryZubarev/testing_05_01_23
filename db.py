import psycopg2
from config import *


def get_row_number():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user_name,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT max(id)
                FROM public.user"""
            )

            count = cursor.fetchone()[0]

            return int(count)

    except Exception as _ex:
        print(_ex)

    finally:
        connection.close()


def add_user(login: str, email: str, phone: str):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user_name,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        ident = get_row_number() + 1

        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO public.user (id, login, email, phone)
                VALUES ('{ident}', '{login}', '{email}', '{phone}')
                """
            )

    except Exception as _ex:
        print(_ex)

    finally:
        connection.close()


def get_user(user_id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user_name,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT id, login, email, phone
                FROM public.user
                WHERE id = {user_id}"""
            )

            result = cursor.fetchone()
            user = {
                'id': int(result[0]),
                'login': result[1],
                'email': result[2],
                'phone': result[3]
            }

            return user

    except Exception as _ex:
        print(_ex)

    finally:
        connection.close()


def get_user_by_data(login: str, email: str, phone: str):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user_name,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT id
                FROM public.user
                WHERE (login = '{login}' AND email = '{email}' AND phone = '{phone}')"""
            )

            result = cursor.fetchone()[0]

            return int(result)

    except Exception as _ex:
        print(_ex)

    finally:
        connection.close()


print(get_row_number())
