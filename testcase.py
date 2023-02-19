from jiajianfa import *
import unittest
class Jia(unittest.TestCase):
    def test_yichang(self):
        r=add(3,5)
        print(r)
if __name__ == '__main__':
    suit=unittest.TestLoader().discover(".","test*.py")
    runner=unittest.TextTestRunner()
    runner.run(suit)