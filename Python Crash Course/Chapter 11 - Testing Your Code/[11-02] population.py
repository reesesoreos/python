import unittest
from inputs.city_functions_mod import city_country

class TestCase(unittest.TestCase):
    def test_city_country(self):
        location = city_country('paris', 'france')
        self.assertEqual(location, 'Paris, France')
    
    def test_city_country_population(self):
        info = city_country('santiago', 'chile', 5000000)
        self.assertEqual(info, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
