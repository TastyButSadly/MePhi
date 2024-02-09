import os
import json

def char_occurr(file_path):
    char_occ = load_char_occurr()

    abs_file_path = os.path.abspath(file_path)  # асболютный путь к файлу

    with open(abs_file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        for char in data:
            char_occ[char] = char_occ.get(char, 0) + 1

    char_occ = dict(sorted(char_occ.items()))  # для красоты отсортируем по ключу
    json.dump(char_occurr, json_file, ensure_ascii=False)


def load_char_occurr():  # открытие json
    with open('char_occurr.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def save_occurr(char_occurr):  # сохранение json



file_name = 'Ницше.txt'
char_occurr(file_name)
