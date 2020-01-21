import unittest 

from country_codes_cd import get_country_code

class CountryCodesTestCase(unittest.TestCase):
	"""CountryCodesTestCase"""
	def test_get_country_code__init__(self):
		country_code = get_country_code('Andorra')
		self.assertEqual(country_code, 'ad')

		country_code = get_country_code('United Arab Emirates')
		self.assertEqual(country_code, 'ae')

		country_code = get_country_code('Afghanistan')
		self.assertEqual(country_code, 'af')
		
unittest.main()