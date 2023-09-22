import requests
from bs4 import BeautifulSoup

url = 'https://index.minfin.com.ua/reference/people/town/'
response = requests.get(url)


def city_parser():
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table')

        city_population_dict = {}

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 2:
                city = columns[0].text.strip()
                population = columns[1].text.strip()
                city_population_dict[city.lower()] = population

        city = input("Введите город: ").lower()
        parsed_data = city_population_dict.get(city)

        return f"Город - '{city.capitalize()}', население - '{parsed_data} чел'"


if __name__ == "__main__":
    print(city_parser())
