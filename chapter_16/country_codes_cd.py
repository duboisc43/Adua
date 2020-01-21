from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	"""Return the Pygal 2 digit country code for the given country"""
	for code, name in COUNTRIES.items():
		if country_name == 'Yemen, Rep.':
			return 'ye'
		elif country_name == 'Korea, Rep.':
			return 'kr'
		elif country_name == 'Korea Dem. Rep.':
			return 'kp'
		elif country_name == 'Egypt, Arab Rep.':
			return 'eg'
		elif country_name == name:
			return code
	# If country wasn't found, return None.
	return None

