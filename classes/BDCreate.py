import psycopg2


class BDCreate:

    def __init__(self, database_name: str, params: dict):
        self.database_name = database_name
        self.params = params

    def create_database(self):
        """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        try:
            cur.execute(f'DROP DATABASE {self.database_name}')
        except:
            pass
        finally:
            cur.execute(f'CREATE DATABASE {self.database_name}')

        conn.close()

        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        # with conn.cursor() as cur:
        #     cur.execute("""
        #         CREATE TABLE employers (
        #             employer_id SERIAL PRIMARY KEY,
        #             employer VARCHAR
        #         )
        #     """)

        with conn.cursor() as cur:
            cur.execute("""
                    CREATE TABLE vacancies (
                        vacancies_id SERIAL PRIMARY KEY,
                        employer VARCHAR,
                        vacancy VARCHAR NOT NULL,
                        vacancy_url TEXT,
                        city VARCHAR,
                        salary INTEGER,
                        currency VARCHAR
                    )
                """)

        conn.commit()
        conn.close()

    # params = config()
    # bd = BDManager('coursework5', params)
    # bd.create_database()

    def save_data_to_database(self, data: list[dict]):
        """Сохранение данных о каналах и видео в базу данных."""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            for i in range(len(data)):
                vacancy_data = data[i]
                if vacancy_data['salary'] is None:
                    continue
                if vacancy_data['salary']['to'] is None:
                    continue
                else:
                    name_employer = vacancy_data['employer']['name']
                    name_vacancy = vacancy_data['name']
                    city = vacancy_data['area']['name']
                    url = vacancy_data['alternate_url']
                    salary_to = vacancy_data['salary']['to']
                    currency = vacancy_data['salary']['currency']
                # cur.execute(
                #     """
                #     INSERT INTO employers (employer)
                #     VALUES (%s)
                #     """,
                #     name_employer
                # )
                # employer_id = cur.fetchone()[0]
                cur.execute(
                    """
                    INSERT INTO vacancies (vacancy, employer, vacancy_url, city, salary, currency)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (name_vacancy, name_employer, url, city, salary_to, currency)
                )

        conn.commit()
        conn.close()