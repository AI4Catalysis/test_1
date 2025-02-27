import unittest
from xplus31.src.merge.deeper.file31 import plus31
from xplus31.src.merge.deeper.__dumb import const
from xplus31.output import print_clr

class TestMyPackage(unittest.TestCase):
    def test_some_function(self):
        self.assertEqual(   plus31(0),  31  )
        self.assertEqual(   const,      2   )
        self.assertEqual(   print_clr(1,'+',2,bgclr=4),  None  )

if __name__ == '__main__':
    unittest.main()