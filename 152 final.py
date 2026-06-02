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
root['bg'] = '#fafafa'
root.title('Интересные места')
root.geometry('350x400')
root.resizable(width=False, height=False)

frame_1 = Frame(root)
frame_1.place(relx=0.5, rely=0.12, relwidth=0.9, relheight=0.1, anchor=CENTER)
info = Label(frame_1, text='Интересные места', font=10)
info.pack()

frame_2 = Frame(root)
frame_2.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.25)
cityField = Entry(frame_2, bg='white', font=30)
cityField.pack()

btn = Button(frame_2, text='Узнать', command=get_city)
btn.pack()

frame_3 = Frame(root)
frame_3.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.4)
fact_label = Label(frame_3, text="Введите: msk, spb, kzn, nsk и т.д.", wraplength=300)
fact_label.pack()

root.mainloop
