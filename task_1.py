import requests


def best_hero(heroes: list):
    heroes_dict = {} #Определяем пустой словарь, где ключи - это имена героев, а значения - их интелект
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url) #Используя библиотеку requests, делаем get запрос по url. Полученный ответ сохраняем в переменную
    if response.status_code != 200: #Проверяем имеем ли статус 200
        return "Запрс некорректный", response.status_code #Возвращаем сообщению пользователю, что запрос некорректный или ошибка на сервере, завершая работу функции
    hero_dict = response.json() #Получаем данные из ответа и сохраняем в переменную. Здесь у нас список из геров, который хранится в отдельном словаре
    for elem in hero_dict: #Проходим в цикле по героям
        hero = elem["name"] #Получаем имя героя из словаря и сохраняем в переменную
        if hero in heroes: #Проверяем есть ли герой в искомом списке супергероев
            heroes_dict[hero] = int(elem["powerstats"]["intelligence"]) #Сохраняем героя в наш ранее созданный словарь
    ihero = max(heroes_dict, key=lambda x: heroes_dict[x]) #Получаем героя с максимальным интелектом
    result = (f"\nСамый умный супергерой: {ihero}) # - его интелект: {heroes_dict[ihero]}")
    return result

list_hero_name = ["Hulk", "Captain America", "Thanos"]
print(best_hero(list_hero_name))