import unittest #测试的库
from city_functions import City

class TestCity(unittest.TestCase):
    '''测试代码,必须是test开头'''
    def test_city(self):
        city = City('Shanghai','China',1000)
        self.assertEqual(city,'Shanghai,China-population 1000')

unittest.main()
