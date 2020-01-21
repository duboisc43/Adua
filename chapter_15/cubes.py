import numpy as np
import matplotlib.pyplot as plt 

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlGn, edgecolor='none', s=40)

#Set chart title and label axes

plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Value cubed", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis="both", which='major', labelsize=15)

plt.show()