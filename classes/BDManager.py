import psycopg2


class BDManager:

    def __init__(self, database_name: str, params: dict):
        self.database_name = database_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT DISTINCT employer, COUNT(vacancy)
                FROM vacancies
                GROUP BY employer
                """
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_all_vacancies(self):
        """Получает список всех вакансий"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT employer, vacancy, salary, vacancy_url
                FROM vacancies
                """
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT AVG(salary)
                FROM vacancies
                """
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT vacancy
                FROM vacancies
                WHERE salary > (SELECT AVG(salary) FROM vacancies)
                """
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слово"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT vacancy
                FROM vacancies
                WHERE vacancy LIKE ('%{keyword}%')
                """
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()
