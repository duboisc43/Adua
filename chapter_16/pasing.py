import csv
from datetime import datetime

from matplotlib import pyplot as plt 

# Get dates and high temperatures from file.
filename = 'santa_rosa.csv'
# 1, DateTime 	# 3, HiTemp		# 4, LowTemp
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[1], '%m/%d/%Y  %I:%M:%S %p')
		dates.append(current_date)

		high = float(row[3])
		highs.append(high)
# Plot data.
fig = plt.figure(dpi=150, figsize=(10,6))
plt.scatter(dates, highs, c='red')

# format plot
plt.title("Daily high temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()