import math


class Cylinder:
    def __init__(self, radius, height, mass=None, density=None):
        self.radius = radius
        self.height = height
        self.mass = mass
        self.density = density

    def volume(self):
        return round(math.pi * self.radius ** 2 * self.height, 2)

    def density_calc(self):
        return round(self.mass / self.volume(), 5)

    def moment_of_inertia(self, a=0):
        if self.mass is not None:
            return round(0.5 * self.mass * self.radius ** 2 + self.mass * a ** 2, 2)
        elif self.density is not None:
            return round(0.25 * self.density * math.pi * self.radius ** 4 * self.height +
                         math.pi * self.density * self.height * self.radius ** 2 * a ** 2, 2)

    def __str__(self):
        if self.mass is not None:
            return f"Цилиндр радиуса {self.radius} м, высоты {self.height} м, массой {self.mass} кг, плотностью {self.density_calc()} кг/м**3"
        elif self.density is not None:
            return f"Цилиндр радиуса {self.radius} м, высоты {self.height} м, плотностью {self.density} кг/м3"


cylinder = Cylinder(5.0, 10.0, 1)
print(cylinder)
print('Объем:', cylinder.volume())
print('Момент инерции:', cylinder.moment_of_inertia(2))
# print(cylinder.density_calc())
