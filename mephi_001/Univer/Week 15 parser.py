import json

# Конфигурационный файл для первого графика
config1 = {
    "file_path": "inertia_2.25_0.43.csv",
    "label": "Data 1",
    "color": "blue",
    "line_style": "-",
    "marker_style": "o",
    "marker_size": 10
}

# Конфигурационный файл для второго графика
config2 = {
    "file_path": "inertia_1.98_0.36.csv",
    "label": "Data 2",
    "color": "green",
    "line_style": "--",
    "marker_style": "s",
    "marker_size": 10
}

# Сохраняем конфигурацию в JSON-файлы
with open('config1.json', 'w') as config_file:
    json.dump(config1, config_file, indent=2)

with open('config2.json', 'w') as config_file:
    json.dump(config2, config_file, indent=2)
