import psycopg2
from config import *


"""The method returns the maximum ID from the database.
   The method is needed due to the fact
   that auto-increment is not configured in the database"""
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


"""The method receives 3 fields as input: login, email and phone number,
   after which it adds a new record with these parameters to the database"""
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


"""The method receives user ID and returns all data of the row with 
   appropriate ID"""
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


"""The method receives user's login, email and phone number,
   finds the first row in database with these parameters
   and return ID from a found row"""
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
