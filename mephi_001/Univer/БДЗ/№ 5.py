class Atoms_n_Molecules:
    def __init__(self, name, mass, pos):
        self.name = name
        self.mass = mass
        self.pos = pos

    def __str__(self):
        return f"{self.name}({self.mass}, {self.pos})"

    def __add__(self, other):
        if isinstance(other, Atoms_n_Molecules):
            total_mass = self.mass + other.mass
            x = (self.mass * self.pos[0] + other.mass * other.pos[0]) / total_mass
            y = (self.mass * self.pos[1] + other.mass * other.pos[1]) / total_mass
            new_pos = (x, y)

            new_name = f"{self.name}{other.name}"

            return Atoms_n_Molecules(new_name, total_mass, new_pos)

# Пример использования
atom1 = Atoms_n_Molecules("H", 1.008, (0, 0))
atom2 = Atoms_n_Molecules("O", 16.00, (1, 0))

molecule = atom1 + atom2
print(molecule)