import unittest

from mymodule import square, double, add

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4) #test if given 2, the output is 4
        self.assertEqual(square(3.0), 9.0) #test if given 3.0, the output is 9.0
        self.assertNotEqual(square(-3), -9) #test if given -3, the ouput is not -9

class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4) #test if given 2, the output is 4
        self.assertEqual(double(-3.1), -6.2) #test if given -3.1, the output is -6.2
        self.assertEqual(double(0), 0) #test if given 0, the output is 0

class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2, 4), 6) #test if given 2 and 4, the output is 6
        self.assertEqual(add(0, 0), 0) #test if given 0 and 0, the output is 0
        self.assertEqual(add(2.3, 3.6), 5.9) #test if given 2.3 and 3.6, the output is 5.9
        self.assertEqual(add('hello', 'world'), 'helloworld') #test if given 'hello' and 'world' the output is 'helloworld'
        self.assertEqual(add(2.3000, 4.300), 6.6) #test if given 2.3000 and 4.300, the output is 6.6
        self.assertNotEqual(add(-2, -2), 0) #test if given -2 and -2, the output is not 0

unittest.main()
