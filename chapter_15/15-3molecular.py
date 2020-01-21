import matplotlib.pyplot as plt

from random_walk_refactored import RandomWalk

# Keep making new walks, as long as the program is active.

# Make a random walk, and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(dpi=128, figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)
    
# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=75, zorder=2)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=75, zorder=2)
    
# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
    
plt.show()


