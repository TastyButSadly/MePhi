import pandas as pd
import numpy as np

# pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# valuess = pd.Series([1, 2, 3, 4], index=['one', 'two', 'tree', 'four'])
# print(valuess)
# print(*valuess.index)
# print(valuess.iloc[0])
# valuess[['one', 'two']] = 0
# print(valuess)
index = ["Меркурий", "Венера", "Земля", "Марс",
         "Юпитер", "Сатурн", "Уран", "Нептун", "Плутон"]
mass_kg = [3.302E23, 4.869E24, 5.974E24, 6.419E23,
           1.899E27, 5.685E26, 8.685E25, 1.024E26, 1.3E22]
equatorial_radius_km = [2440., 6052., 6378., 3397., 71490., 60270., 25560., 24760., 1151.]

df1 = pd.DataFrame({'mass':mass_kg, 'radius': equatorial_radius_km}, index = index )
df2 = pd.DataFrame(np.array([mass_kg, equatorial_radius_km]).T, columns=['mass', 'radius'], index=index)
print(df1)
print(df2)