
from tkinter import *
import requests

def get_city():
    city = cityField.get()
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json&addressdetails=1&limit=2'
    headers = {'User-Agent': 'MyApp/1.0'}
    
    result = requests.get(url, headers=headers)
    data = result.json()

    if len(data) >= 2:
        place1 = data[0]
        place2 = data[1]
        text = f"{place1.get('display_name', 'Нет названия')}\nТип: {place1.get('type', 'не указан')}\n\n{place2.get('display_name', 'Нет названия')}\nТип: {place2.get('type', 'не указан')}"
    else:
        text = "Не найдено. Введите: msk, spb, kzn, nsk"

    fact_label['text'] = text


root = Tk()
root['bg'] = '