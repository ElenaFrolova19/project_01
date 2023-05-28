# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# Решение

from random import sample
three_songs = sample (my_favorite_songs, 3)
print(f'Три случайные песни {three_songs}')
total_time = three_songs[0][1] + three_songs[1][1] + three_songs[2][1]
print(f'Три песни звучат {"%.2f" % total_time} минут')

import datetime
sec = total_time // 1 *60 + total_time % 1*100
time_format = str(datetime.timedelta(seconds=sec))
print(f'Три песни звучат {time_format} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение
data = list(my_favorite_songs_dict.items())
three_songs_dict = sample(data, 3)
print(f'Три случайные песни {three_songs_dict}')
total_time_dict = three_songs_dict[0][1] + three_songs_dict[1][1] + three_songs_dict[2][1]
print(f'Три песни звучат {"%.2f" % total_time_dict} минут')

sec_dict = total_time_dict // 1 *60 + total_time_dict % 1*100
time_format_dict = str(datetime.timedelta(seconds = sec_dict))
print(f'Три песни звучат {time_format_dict} минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

