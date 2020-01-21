import csv

import pygal
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes_cd import get_country_code as gcc 


filename = "top_income.csv"
with open(filename) as f:
	reader = csv.reader(f)
	for row in range(0,4):
		next(reader)
	header_row = next(reader)
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
	
	top_2010_incomes = []
	country_names = []
	for row in reader:
		country_names.append(row[0])
		top_2010_incomes.append(row[54])	

income_dict = dict(zip(country_names, top_2010_incomes))	
# Build a dictionary with country codes, income share held by highest 10% in the year 2010
cc_income_dict_data, cc_income_dict_nodata = {}, {}
for country_name, income in income_dict.items():
	if country_name:
		cc = gcc(country_name)
		if income:
			if cc:
				cc_income_dict_data[cc] = income	
		else:
			cc_income_dict_nodata[cc] = 'no data available'
	else:
		continue


wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)	
wm = pygal.maps.world.World(style=wm_style)

wm.title = "Income share held by highest '10%' in the year 2010"

wm.add('Countries with data available', cc_income_dict_data)


wm.render_to_file('income_map.svg')