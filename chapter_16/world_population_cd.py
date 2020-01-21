import json

import pygal
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes_cd import get_country_code

# Load the data into a list.
file_name = 'population_data.json'
with open(file_name) as f:
	pop_data = json.load(f)

# Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population

# Group the countries into 3 population levels. 
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:	
		cc_pops_2[cc] = pop 
	else:
		cc_pops_3[cc] = pop 
# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wmcd_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wmcd = pygal.maps.world.World(style=wmcd_style)
wmcd.title = 'World Population in 2010, by Country'
wmcd.add('0-10m', cc_pops_1)
wmcd.add('10m-1bn', cc_pops_2)
wmcd.add('>1bn', cc_pops_3)

wmcd.render_to_file('world_population.svg')
# import pygal
# #pygal.maps.world.World()
# wm = pygal.maps.world.World()
# wm.title = 'Populations of Countries in North America'
# wm.add('North America', {"ca": 34126000, 'us': 327200000, 'mx': 129200000})

# wm.render_to_file('na_populations.svg')