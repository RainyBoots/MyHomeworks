from marvel import full_dict
from pprint import pprint
from typing import Dict, List, Set, Any, Tuple

# Пользовательский ввод
user_input: list = input('Введите цифры через пробел:').split(' ')

# Интуем каждое число в списке
user_list: List[int | None] = [int(n) if n.isdigit() else None for n in user_input]
# Словарь с фильмами которые мы запросили

filter_film: Dict[int, Dict[str, Any]] = {key: value for key, value in full_dict.items() if key in user_list}
# Множество с ключом director

director_set: Set[str] = {film['director'] for film in full_dict.values()}
# Применение 'str' к 'year'

dict_film_year: Dict[int, Dict[str, str]] = {key: {k: str(v) if k == 'year' else v for k, v in value.items()}
                                             for key, value in full_dict.items()}

# Все фильмы которые начинаются с 'Ч'
filtered_dict: Dict[int, Dict[str, Any]] = {k: v for k, v in full_dict.items() if
                                            v['title'] and v['title'].startswith('Ч')}

# Сортировка словаря по названию
sorted_title: List[Tuple[int, Dict[str, Any]]] = sorted(full_dict.items(), key=lambda x: str(x[1]['title']))

# Сортировка словаря по двум параметрам (year, title). Почему-то сортировка работает только если превращать все в
# строку. Наверное из-за TBA, но в предыдущем пункте тоже. Так что это не совсем понятно.
sorted_dict_2params: List[Tuple[int, Dict[str, Any]]] = sorted(full_dict.items(), key=lambda x: (str(x[1]['year']),
                                                                                                 str(x[1]['title'])))

# Отфильтрованный и отсортированный по названию словарь
filtered_and_sorted_dict: Dict[int, Dict[str, Any]] = {k: v for k, v in
                                                       sorted(full_dict.items(), key=lambda item: str(item[1]['title']))
                                                       if k in user_list}

pprint({"Список пользовательского ввода": user_list, "Фильтр для получения словаря": filter_film,
        "Множество с ключом 'director'": director_set,
        "Применение 'str' к 'year'": dict_film_year, "Фильмы на букву 'Ч'": filtered_dict,
        "Сортировка по названию": sorted_title, "Сортировка по году и названию": sorted_dict_2params,
        "Отфильтрованный и отсортированный словарь": filtered_and_sorted_dict}, sort_dicts=False)
# Проверка mypy пройдена
