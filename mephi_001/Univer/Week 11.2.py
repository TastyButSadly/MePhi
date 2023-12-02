class Capacitor:
    def __init__(self, cap):
        self.cap = cap

    def __add__(self, other):  # последовательно
        return Capacitor(1 / (1 / self.cap + 1 / other.cap))

    def __mul__(self, other):  # параллельно
        return Capacitor(self.cap + other.cap)


    def __str__(self):
        if self.cap >= 1e-6:
            return f"Конденсатор ёмкостью {self.cap * 1e6:.2f} мкФ"
        elif self.cap >= 1e-9:
            return f"Конденсатор ёмкостью {self.cap * 1e9:.2f} нФ"
        elif self.cap >= 1e-12:
            return f"Конденсатор ёмкостью {self.cap * 1e12:.2f} пФ"
        else:
            return f"Конденсатор ёмкостью {self.cap:.2e} Ф"


C1 = Capacitor(1.0e-6)
C2 = Capacitor(2.0e-6)
C3 = C1 + C2
C4 = C1 * C2 * C1

print(C1, C2, C3, C4, sep="; ")
