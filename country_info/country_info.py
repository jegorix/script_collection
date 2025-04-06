'''
📍 Получаем данные о стране с помощью Python — быстро, просто и в стиле Data Science.
Хочешь узнать площадь, столицу или список регионов любой страны прямо из кода?
Библиотека countryinfo делает это за пару строчек!

🖱 Работает для большинства стран мира;
🖱 Возвращает столицы, регионы, валюту, соседей и даже границы;
🖱 Отлично подходит для геоанализов, ботов, дашбордов и просто фана.

pip install countryinfo
'''

from countryinfo import CountryInfo
from typing import List, Union


def get_country_info(country_name: str) -> None:
    country = CountryInfo(country_name)

    area: Union[int, None] = country.area()
    population: Union[int, None] = country.population()
    provinces: Union[List[str], None] = country.provinces()
    capital: Union[str, None] = country.capital()

    print(f"📍 Страна: {country_name}")
    print(f"📐 Площадь: {area:,} км²")
    print(f"👥 Население: {population:,} человек")
    print(f"🏙 Столица: {capital}")
    print(f"📌 Регионы: {', '.join(provinces[:5])} ... (и другие)")


if __name__ == "__main__":
    get_country_info("USA")