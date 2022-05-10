import requests
import xml.etree.ElementTree as ET
import datetime


def currency_rates(char_code: str):
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    xml = ET.fromstring(r.text)

    for valute in xml.findall('Valute'):
        if valute.find('CharCode').text == char_code.upper():
            date_str = xml.attrib.get("Date")
            date_dt = datetime.datetime.strptime(date_str, '%d.%m.%Y')
            return float(valute.find('Value').text.replace(',','.')), date_dt.strftime("%Y-%m-%d")
    return None
