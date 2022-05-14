import requests
import xml.etree.ElementTree as ET
from decimal import Decimal
from decimal import getcontext

getcontext().prec = 7


def currency_rates_decimal(char_code: str) -> Decimal:
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    xml = ET.fromstring(r.text)
    for valute in xml.findall('Valute'):
        if valute.find('CharCode').text == char_code.upper():
            return Decimal(valute.find('Value').text.replace(',','.'))
    return None


print("Введите наименование валюты:")
print(currency_rates_decimal(input()))
