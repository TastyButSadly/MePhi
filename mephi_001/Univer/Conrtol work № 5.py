import matplotlib.pyplot as plt
import numpy as np


def random_walk(x, y, t):
    a = np.random.uniform(1.5, 5.001)
    b = np.random.uniform(1.5, 5.001)
    dl = 0.03

    trace = [[], []]

    # if it's necessary to jump within a square, leave it as is
    # else if it's necessary to jump within a circle, comment lines 22 and 23 and recommend others
    
    for _ in range(t + 1):
        # jump_direction = np.random.uniform(0, 2 * np.pi)
        dl_max = dl
        # dl_max = abs(dl / np.cos(jump_direction))
        # dl_i = np.random.uniform(0, dl_max)
        # dl_q = dl
        # dx = dl_i * np.cos(jump_direction)
        # dy = dl_i * np.sin(jump_direction)
        dx = np.random.uniform(-dl_max, dl_max)
        dy = np.random.uniform(-dl_max, dl_max)

        print(round(x, 6), round(y, 6))

        if 0 < x + dx < a:
            x += dx
        elif x + dx > a:
            x += dx - a
        elif x + dx < a:
            x += dx + a

        if 0 < y + dy < b:
            y += dy
        elif y + dy > b:
            y += dy - b
        elif y + dy < b:
            y += dy + b

        trace[0].append(x)
        trace[1].append(y)

    return trace


trace = random_walk(0.5, 0.5, 20)

plt.plot(trace[0], trace[1], marker='o', linestyle='-')
plt.show()
