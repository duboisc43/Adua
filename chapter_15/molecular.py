import matplotlib.pyplot as plt  

from random_walk import RandomWalk

#Keep making new walks, as long as the program is active.

#Make a random walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()

# # Set the size of the plotting window.
# plt.figure(figsize=(6, 4))

# point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=5)

#Emphasize the first and last points.
plt.plot(0, 0, c='green', linewidth=5)
plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', linewidth=5)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)


plt.show()

keep_running = raw_input("Make another walk? (y/n): ")
