import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as file_object:
	reader = csv.reader(file_object)
	header_row = next(reader)
	
for index, column_header in enumerate(header_row):
	print(index, column_header)
	# print("\nKey: " + str(index))
	# print("Value: " + column_header)