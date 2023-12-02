import pandas as pd


def warm_mass(r, t2):
    return 4200 * 75 * (t2 - 20) / r / 10 ** 6


r = [44, 15, 31, 41, 26]

data = {
    #'r': ['бензин', 'дерево', 'древесный уголь', 'нефть', 'спирт'],
    '': ['gasoline', 'wood', 'charcoal', 'petroleum', 'alcohol'],
    'Q': [i for i in r],
    'm1': [round(warm_mass(j, 30), 3) for j in r],  # Массы топлива для нагрева 75 л воды от 20°C до 30°C
    'm2': [round(warm_mass(j, 40), 3) for j in r],  # Массы топлива для нагрева 75 л воды от 20°C до 40°C
    'm3': [round(warm_mass(j, 50), 3) for j in r],  # Массы топлива для нагрева 75 л воды от 20°C до 50°C
    'm4': [round(warm_mass(j, 60), 3) for j in r]  # Массы топлива для нагрева 75 л воды от 20°C до 60°C
}

df = pd.DataFrame(data)

df.to_csv('waterboiler.csv', sep=';', index=False)
