from math import pi

k, N, t = map(float, input("исходные данные: ").split(","))

count_k = len(str(k).split(".")[1]) if "." in str(k) else 0  # число знаков после запятой
count_k = len(str(N).split(".")[1]) if "." in str(N) else 0
count_t = len(str(t).split(".")[1]) if "." in str(t) else 0

max_count = max(count_k, count_k, count_t)  # максимальное число знаков после запятой

print("данные маятника:", "\t", "{:.{}f}".format(k, max_count), "\t", "{:.{}f}".format(N, max_count),
      "\t", "{:.{}f}".format(t, max_count), "\t", "\n",
      "масса ", round(k * t ** 2 / (3 * pi ** 2), max_count), "\t", "обработано!")
# все числа выведены с равным числом знаков после запятой
