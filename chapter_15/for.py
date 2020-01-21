all_outcomes = []
x_values = []
for x in range(1,7):
	all_outcomes.append(x*1)
	all_outcomes.append(x*2)
	all_outcomes.append(x*3)
	all_outcomes.append(x*4)
	all_outcomes.append(x*5)
	all_outcomes.append(x*6)

for x in range(1,7):
	for y in range(1,7):
		all_outcomes.append(x*y)
print(all_outcomes)

for x in all_outcomes:
	if x not in x_values:
		x_values.append(x)

print(len(x_values))