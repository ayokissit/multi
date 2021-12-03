from hashlib import md5
from random import choice
import concurrent.futures


""" Скорость генерации 1 монеты на одном ядре составила 17 секунд, при использовании ProcessPoolExecutor 
первая монета был найдена за 2.2 секунды (при повторном запуске за 5.3 сек).  """

while True:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()
    if h.endswith("00000"):
        print(s, h)


# def find_token():
#     while True:
#         s = "".join([choice("0123456789") for _ in range(50)])
#         h = md5(s.encode('utf8')).hexdigest()
#         if h.endswith("00000"):
#             print(s, h)
#
#
# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
#         e = executor.submit(find_token)