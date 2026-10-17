import unittest
from inputs.city_functions import city_country

class TestCase(unittest.TestCase):
    def test_city_country(self):
        location = city_country('paris', 'france')
        self.assertEqual(location, 'Paris, France')

if __name__ == '__main__':
    unittest.main()
