import requests
from bs4 import BeautifulSoup
import sys


# URL для парсинга данных о городах Украины и валютах стран
city_url = 'https://index.minfin.com.ua/reference/people/town/'
currency_url = 'https://fxtop.com/ru/countries-currencies.php'

# Выполняем запросы к ресурсам
response_city = requests.get(city_url)
response_currency = requests.get(currency_url)


def city_parser(city_name):
    """
    Функция для парсинга информации о населении городов Украины.

    :param city_name: Название города, для которого нужно получить информацию о населении.
    :type city_name: str

    :return: Информация о городе, населении и стране (Украина).
    :rtype: str or None
    """
    if response_city.status_code == 200:
        soup = BeautifulSoup(response_city.text, 'html.parser')

        table = soup.find('table')

        city_population_dict = {}

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 2:
                city = columns[0].text.strip()
                population = columns[1].text.strip()
                city_population_dict[city.lower()] = population

        parsed_data = city_population_dict.get(city_name.lower())

        if parsed_data:
            return f"Город - {city_name.capitalize()}\nСтрана - Украина \nНаселение - {parsed_data} чел "
        else:
            return None


def currency(country_name):
    """
    Функция для парсинга информации о валютах стран.

    :param country_name: Название страны, для которой нужно получить информацию о валюте.
    :type country_name: str

    :return: Информация о стране и ее валюте.
    :rtype: str or None
    """
    if response_currency.status_code == 200:
        soup = BeautifulSoup(response_currency.text, 'html.parser')

        table = soup.find('table')

        country_currency_dict = {}

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 4:
                country = columns[0].text.strip()
                currency = columns[2].text.strip()
                country_currency_dict[country.lower()] = currency

        parsed_currency = country_currency_dict.get(country_name.lower())

        if parsed_currency:
            return f"Страна - {country_name.capitalize()} \nВалюта - {parsed_currency}"
        else:
            return None


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 1:
        input_value = args[0]
        city_info = city_parser(input_value)
        if city_info:
            print(city_info)
        else:
            country_info = currency(input_value)
            if country_info:
                print(country_info)
            else:
                print(f"Данные для {input_value} не найдены.")
    else:
        print("Использование: python main.py <город или страна>")