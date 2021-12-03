import concurrent.futures
from bs4 import BeautifulSoup
import requests
import time


URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'


""" Генерация и сохранение ссылок """

# def load_url(url):
#     r = requests.get(url)
#     print(r.url)
#     file_object = open('file.txt', 'a', encoding='utf-8')
#     file_object.write(r.url + "\n")
#     file_object.close()
#
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
#     for i in range(20):
#         try:
#             execute = executor.submit(load_url, URL)
#         except Exception as exc:
#             print('generated an exception: %s' % exc)

""" Получение всех ссылок со страниц """


# def get_links(new_url):
#     r = requests.get(new_url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     links = soup.find_all('a')
#
#     for link in links:
#         href = link.get('href')
#         if href and href.startswith('http') and 'wiki' not in href:
#             print(href)
#             res_file.write(href + "\n")
#
#
# res_file = open('page_links.txt', 'a', encoding='utf8')
# urls = open('file.txt', 'r', encoding='utf8').read().split('\n')
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
#     for url in urls:
#         execute = executor.submit(get_links, url)


""" Открытие каждой ссылки """


# def get_links(new_url):
#     try:
#         r = requests.get(
#             new_url,
#             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
#             timeout=5
#         )
#         code = r.status_code
#         print(code, url)
#     except Exception as e:
#         print(url, e)
#
from urllib.request import Request, urlopen
from urllib.parse import unquote

links = open('page_links.txt', encoding='utf8').read().split('\n')

for url in links:
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)
# urls = open('page_links.txt', encoding='utf8').read().split('\n')
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
#     for url in urls:
#         execute = executor.submit(get_links, url)


""" Вывод: время работы значительно сокращается при использовании ThreadPoolExecutor, нежели
 при обычном синхронном отборе данных. Так, при проверке ссылок при синхронной обработке понадобилось 337 секунд, 
 а с помощью ThreadPoolExecutor 29. Изменяя количество воркеров в большую сторону, скорость работы увеличивается, 
 но засчет оперативной памяти, процессора и прочего"""