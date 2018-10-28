import unittest
import math
import lighting.ESPLedStripWarmWhite
from tests.mocks.mock_router import MockRouter

class TestESPLedStripWarmWhite(unittest.TestCase):
    def test_conversion(self):
        router = MockRouter(None)
        light = lighting.ESPLedStripWarmWhite(router)
        userVal = 10
        lightVal = light.convertBrightness(userVal)
        self.assertEqual(self.mock_conversion_level(userVal), lightVal)

    def test_conversion_inverse(self):
        router = MockRouter(None)
        light = lighting.ESPLedStripWarmWhite(router)
        userVal = 818
        lightVal = light.convertBrightnessInverse(userVal)
        self.assertEqual(self.mock_conversion_inverse_level(userVal), lightVal)
        
    def mock_conversion_level(self, p):
        maxp = 31
        maxv = math.log(1023)

        scale = maxv / maxp
        level = math.exp(scale * p)

        return math.floor(level)

    def mock_conversion_inverse_level(self, p):
        maxp = 31
        maxv = math.log(1023)

        scale = maxp / maxv
        level = scale * math.log(p)

        return int(level + .5)

if __name__ == '__main__':
    unittest.main()
