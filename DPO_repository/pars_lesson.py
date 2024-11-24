# Задача 1

# import requests as req
#
# try:
#     resp = req.get('https://api.github.com')
#     if resp.status_code == 200:
#         print('There is such a site on the internet')
#     else:
#         print('An error has occurred')
# except Exception as e:
#     print("There is no site in internet", e)

# Задача 2

# import requests as req
#
# try:
#     resp = req.get('https://requestb.in')
#     print('No problem with SSL', resp)
# except req.exceptions.SSLError:
#     print('Some problems with SSL')

# Задача 3

# import requests as req
#
# session = req.Session()
# response = session.get('https://www.python.org/')
# print(response.status_code)
# print(session.headers)
# print(response.url)
# print(response.encoding)
# print(response.reason)
# print(session.cookies.get_dict())
# print(response.elapsed)
# print(response.request)
# print(response.content)

# Задача 4

# import requests as req
#
# resp = req.get('https://en.wikipedia.org/robots.txt')
# with open("robots.txt", 'wb') as f:
#
#     f.write(resp.content)

# Задача 5

# import requests
# from bs4 import BeautifulSoup
#
# resp = requests.get('http://www.example.com/')
# soup = BeautifulSoup(resp.text, 'html.parser')
# titles = soup.find_all('h1')
# for title in titles:
#     print(title.text)

# Задача 6

# import requests as req
# from bs4 import BeautifulSoup
#
# url = 'https://en.wikipedia.org/wiki/Main_Page'
# resp = req.get(url)
# soap = BeautifulSoup(resp.text, 'html.parser')
# header_list = ['h1', 'h2', 'h3', 'h4', 'h5']
# headers = soap.findAll(header_list)
# for header in headers:
#     print(header.text)

# Задача 7

# import requests as req
# from bs4 import BeautifulSoup
#
# url = 'https://en.wikipedia.org/wiki/Python'
# resp = req.get(url)
# soap = BeautifulSoup(resp.text, 'html.parser')
#
# links = soap.findAll('a', href=True)
#
# links_list = []
#
# for link in links:
#     href = link['href']
#     if href.startswith('/'):
#         href = 'https://en.wikipedia.org' + href
#     links_list.append(href)
#
# for link in links_list:
#     print(link)

# Задача 8 первый вариант

# import pandas as pd
#
# table = pd.read_csv('4.5_month.csv')
# print(len(table) + 1)

# Задача 8 второй вариант

# with open('4.5_month.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
#     data = [line.strip().split(',') for line in lines]
#     counter = 0
#     for line in lines:
#         counter += 1
#         # print(line)
#     print(counter)

# Задача 9

# import requests
# from bs4 import BeautifulSoup
# import random
#
#
# def scrape_imdb_top_movies():
#     url = 'https://www.imdb.com/chart/top'
#
#     response = requests.get(url)
#
#     if response.status_code != 200:
#         print(f"Ошибка при запросе: {response.status_code}")
#         return
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     movie_rows = soup.find_all('td', class_='titleColumn')
#
#     movies = []
#
#     for row in movie_rows:
#         title_year = row.a.get_text() + ' (' + row.span.get_text().strip('()') + ')'
#
#         movie_link = 'https://www.imdb.com' + row.a['href']
#
#         movie_response = requests.get(movie_link)
#         movie_soup = BeautifulSoup(movie_response.text, 'html.parser')
#
#         description = movie_soup.find('span', class_='sc-16ede01-2 gXUyNh').get_text()
#
#         movies.append((title_year, description))
#
#     return movies
#
#
# def print_random_movies(movies, count=10):
#     random_movies = random.sample(movies, count)
#
#     for movie in random_movies:
#         title_year, description = movie
#         print('-' * 40)
#         print(title_year)
#         print(description)
#         print('-' * 40)
#
#
# if __name__ == "__main__":
#     movies = scrape_imdb_top_movies()
#     print_random_movies(movies)
#
# # Сколько бы не пытался ошибка 403 и все!!!!!!!!!!!!!!!!!!!!!!!!!!