import requests
import tkinter as tk
from urllib.request import urlopen
from PIL import ImageTk

API_KEY = '...'

# Задание №1
print(requests.get('https://google.com', timeout=5))

# Задание №2
city_name = input('Введите название города: ')
response = requests.get('https://api.openweathermap.org/data/2.5/weather',
                        params={'q': city_name, 'appid': API_KEY}, timeout=5).json()

print(f'Температура: {round(response["main"]["temp"] - 273.15, 2)} °C')
print(f'Влажность: {response["main"]["humidity"]}%')
print(f'Давление: {response["main"]["pressure"]} мм.рт.ст.', end='\n\n')

# Задание №3 (вариант 6: steamcommunity.com -> api.steampowered.com)
app_id = input('Введите ID игры (ex. 440): ')
count_news = int(input('Введите количество новостей: '))
# Поиск новостей по ID игры (appid) с заданным количеством (count) с длиной текста (maxlength) в 50 символов
response = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/', timeout=5,
                        params={'appid': app_id, 'count': count_news, 'maxlength': 120, 'format': 'json'}).json()

for news in response['appnews']['newsitems']:
    print(f'\n{news["title"]} | {news["url"]}')
    print(f'{news["feedlabel"]} {news["author"]} | Дата: {news["date"]}')
    print(f'{news["contents"]}')
    print('----------------------------------------')


# Допзадание
def refresh_picture():
    with urlopen(requests.get('https://randomfox.ca/floof/', timeout=5).json()['image']) as resp:
        img = ImageTk.PhotoImage(data=resp.read())
    lbl_picture.configure(image=img)
    lbl_picture.image = img


wndw = tk.Tk()
wndw.title('Генератор котят')
wndw.geometry('700x600')

frame = tk.Frame(wndw)
frame.place(relx=0.5, rely=0.5, anchor='c')  # type: ignore

with urlopen(requests.get('https://aws.random.cat/meow', timeout=5).json()['file']) as resp:
    img = ImageTk.PhotoImage(data=resp.read())
    lbl_picture = tk.Label(frame, image=img)
lbl_picture.grid(column=0, row=0, padx=10, pady=10)
lbl_picture.config(width=700, height=500)

btn_generate = tk.Button(frame, text='Сгенерировать', font=('VK Sans Display', 12), command=refresh_picture)
btn_generate.grid(column=0, row=1, padx=20, pady=20)

wndw.mainloop()
