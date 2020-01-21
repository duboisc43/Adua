import matplotlib.pyplot as plt

from die import Die 

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualise the results.
x_values = [x for x in range(1, max_result+1)]
plt.bar(x_values, frequencies)

plt.title("Results of rolling two D6 1000 times")


# hist.y_title = "Result"
# hist.y_title = 'Frequency of Result'

# hist.add('D6 + D6', frequencies)

plt.show()