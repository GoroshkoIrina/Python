import requests
import xml.etree.ElementTree as ET


def currency_rates(char_code: str) -> float:
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    xml = ET.fromstring(r.text)

    for valute in xml.findall('Valute'):
        if valute.find('CharCode').text == char_code.upper():
            return float(valute.find('Value').text.replace(',','.'))
    return None


print("Введите наименование валюты:")
print(currency_rates(input()))
