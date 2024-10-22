import requests
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bs4 import BeautifulSoup
from datetime import datetime

def parse():
    url = 'https://ru.investing.com/currencies/usd-rub-historical-data'

    list_of_price = []
    list_of_date = []

    headers = {
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_='freeze-column-w-1 w-full overflow-x-auto text-xs leading-4')

        if table:
            rows = table.find_all('tr')

            for row in rows[1:]:
                cells = row.find_all('td')

                date = cells[0].text.strip()
                price = float(cells[1].text.strip().replace(',', '.'))
                open_price = cells[2].text.strip()
                high_price = cells[3].text.strip()
                low_price = cells[4].text.strip()
                change_percentage = cells[5].text.strip()
                if date[3:5] == '10':
                    list_of_date.append(datetime.strptime(date, '%d.%m.%Y'))
                    list_of_price.append(price)
                    print(
                        f"Дата: {date}, Цена: {price}, Открытие: {open_price}, Высокая: {high_price}, Низкая: {low_price}")
        else:
            print("Таблица с данными не найдена.")
    else:
        print(f"Ошибка при запросе страницы: {response.status_code}")
    return list_of_date, list_of_price


def plot(list_x, list_y):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(list_x, list_y, marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('USD')
    ax.set_title('Cost of USD in October')
    ax.grid(True)

    return fig


list_x, list_y = parse()
root = tk.Tk()
root.title("Graph in Tkinter")

fig = plot(list_x, list_y)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()

