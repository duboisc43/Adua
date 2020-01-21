import pygal

from die import Die 

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die_1.roll() * die_2.roll()
	results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling, and multiplying, two D6 1000 times"
# all_outcomes = []
# x_values = []
# for x in range(1,7):
# 	all_outcomes.append(x*1)
# 	all_outcomes.append(x*2)
# 	all_outcomes.append(x*3)
# 	all_outcomes.append(x*4)
# 	all_outcomes.append(x*5)
# 	all_outcomes.append(x*6)

# for x in all_outcomes:
# 	if x not in x_values:
# 		x_values.append(x)

hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.y_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual.svg') 