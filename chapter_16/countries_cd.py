import json

from pygal.maps.world import COUNTRIES

missing = [, , 'Korea, Rep.', 'Qatar', 'Yemen, Rep.']

for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])

if country_name == 'Yemen, Rep.':
	return 'ye'
elif country_name == 'Korea, Rep.':
	return 'kr'
elif country_name == 'Korea Dem. Rep.':
	return 'kp'
elif country_name == 'Egypt, Arab Rep.'
	return 'eg'
	