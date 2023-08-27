from classes.get_api import HeadHunterAPI
from classes.BDManager import BDManager
from classes.BDCreate import BDCreate
from config import config

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh = HeadHunterAPI()

# Получает списка с апи-запросом вакансий выбранных работодателей
api = hh.get_api()

# Получает список вакансий от работодателей
vacancy = hh.get_vacancies()

# Получение вакансий в требуемом формате
formatted_vacancies = hh.get_formatted_vacancies()

# Создание экземпляра класса для проектирования базы данных
params = config()
bd = BDCreate('coursework5', params)

# Создание базы данных
bd.create_database()

# Заполнение таблиц в базе данных полученными вакансиями
bd.save_data_to_database(vacancy)

# Создание экземпляра класса для работы с базой данных
bd_manager = BDManager('coursework5', params)

# Вывод данных из таблицы со списком всех компаний и количество вакансий у каждой компании
bd_manager.get_companies_and_vacancies_count()

# Вывод всех вакансий
# bd_manager.get_all_vacancies()

# Вывод средней зарплаты по вакансиям
# bd_manager.get_avg_salary()

# Вывод всех вакансий, у которых зарплата выше средней по всем вакансиям
# bd_manager.get_vacancies_with_higher_salary()

# Вывод всех вакансий по ключевому слову
# keyword = input(">>>").lower()
# bd_manager.get_vacancies_with_keyword(keyword)