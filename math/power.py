import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure()

x = np.linspace(-1, 2, 100)
x1 = np.linspace(0, 2, 100)
y1 = [pow(3.1, val) for val in x]
y2 = [math.exp(val) for val in x]
y3 = [math.expm1(val) for val in x]
y4 = [math.sqrt(val) for val in x1]

plt.plot(x, y1, label = "pow(3.1, x)")
plt.plot(x, y2, label = "math.exp(x)")
plt.plot(x, y3, label = "math.expm1(x)")

plt.plot(x1, y4, label = "math.sqrt(x)")

plt.grid(True)
plt.legend()
plt.show()
