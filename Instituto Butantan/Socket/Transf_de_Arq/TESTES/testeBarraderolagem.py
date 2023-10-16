import matplotlib.pyplot as plt
import numpy as np

plt.ion()
x = np.linspace(0, 4, 1000)
y = np.sin(2 * np.pi * (x - 0.01 * 0))
line, = plt.plot(x, y)

for i in range(1, 100):
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_ydata(y)
    plt.draw()
    plt.pause(0.001)