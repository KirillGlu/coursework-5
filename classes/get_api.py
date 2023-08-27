import requests


class HeadHunterAPI:

    def __init__(self):
        self.data_lst = []
        self.vacancies_lst = []

    def get_api(self):
        """Получает списка с апи-запросом вакансий выбранных работодателей"""
        employers = ["Тинькофф", "Яндекс", "Сбер", "VK", "СКБ Контур", "ЛАНИТ", "Ozon", "Авито", "КРОК", "Nexign"]
        employers_dict = [78638, 1740, 3529, 15478, 41862, 733, 2180, 84585, 2987, 6004]
        for page in range(10):
            param = {
                'page': page,
                'per_page': 100,
                'only_with_vacancies': True
            }
            for i in range(len(employers_dict)):
                response = requests.get(f"https://api.hh.ru/employers/{employers_dict[i]}", params=param).json()
                self.data_lst.append(response['vacancies_url'])
        return self.data_lst

    def get_vacancies(self):
        """Получает список вакансий от работодателей"""
        for i in range(len(self.data_lst)):
            vacancies = requests.get(self.data_lst[i]).json()
            self.vacancies_lst.extend(vacancies['items'])
        return self.vacancies_lst

    def get_formatted_vacancies(self):
        """Форматирует список вакансий"""
        formatted_vacancies = []
        for i in range(len(self.vacancies_lst)):
            vacancy_data = self.vacancies_lst[i]
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

            format_data = {'name_employer': name_employer,
                           'name_vacancy': name_vacancy,
                           'city': city,
                           'salary': salary_to,
                           'currency': currency,
                           'url': url
                           }
            formatted_vacancies.append(format_data)
        return formatted_vacancies

