import pygal

from die import Die 

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 1000 times"
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.y_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg') 