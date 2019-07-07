import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure()

x = np.linspace(0.1, 10, 100)
y1 = [math.log2(val) for val in x]
y2 = [math.log10(val) for val in x]
y3 = [math.log(val) for val in x]
y4 = [math.log(val, 20) for val in x]
y5 = [math.log1p(val) for val in x]

plt.plot(x, y1, label = "math.log2(x)")
plt.plot(x, y2, label = "math.log10(x)")
plt.plot(x, y3, label = "math.log(x)")
plt.plot(x, y4, label = "math.log(x, 20)")
plt.plot(x, y5, label = "math.log1p(x)")

plt.grid(True)
plt.legend()
plt.show()
