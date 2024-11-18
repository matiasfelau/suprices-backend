import unittest

from source.main.service.price_calculator_service import calculate_price


class CalculatePriceTest(unittest.TestCase):


    def test_calculate_price(self):
        output = calculate_price(5.55)
        target = 11.09
        self.assertEqual(output, target)

if __name__ == "__main__":
    unittest.main()
