import unittest
import io
import si

class Test01_add_valid_data(unittest.TestCase):

    def test_list_int(self):
        x = si.SimpleInteger()
        r=x.add(1,2)
        self.assertEqual(3,r)

class Test02_add_invalid_data(unittest.TestCase):

    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.add(1.5,2)
        self.assertEqual(None, r)

class Test03_subtract_valid_data(unittest.TestCase):

    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.subtract(3,7)
        self.assertEqual(-4,r)

class Test04_subtract_invalid_data(unittest.TestCase):

    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.subtract(3.5,7)
        self.assertEqual(None,r)

class Test05_multiply_valid_data(unittest.TestCase):

    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.multiply(5,3)
        self.assertEqual(15,r)

class Test06_multiply_invalid_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.multiply(5.5,3)
        self.assertEqual(None,r)

class Test07_isequal_valid_true_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.isequal(7,7)
        self.assertEqual(True,r)

class Test08_isequal_valid_false_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.isequal(7,8)
        self.assertEqual(False,r)

class Test09_isequal_invalid_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.isequal(7.5,7)
        self.assertEqual(None,r)

class Test10_isgreaterthan_valid_true_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.isgreaterthan(19,6)
        self.assertEqual(True,r)

class Test11_isgreaterthan_valid_false_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.isgreaterthan(10,10)
        self.assertEqual(False, r)

class Test12_isgreaterthan_invalid_data(unittest.TestCase):
    def test_list_int(self):
        x=si.SimpleInteger()
        r=x.isgreaterthan(10.5,6)
        self.assertEqual(None,r)

if __name__ == '__main__':
  with open('test.txt', "w") as f:
      runner = unittest.TextTestRunner(f)
      unittest.main(testRunner=runner)
