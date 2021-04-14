import unittest
from string_to_list import list_from_text


class TestStringToList(unittest.TestCase):
    def test_simple_range(self):
        self.assertEqual(list_from_text("1-5"),list(range(1,6)))
    def test_range_and_page(self):
        self.assertEqual(list_from_text("1-5,5"),list(range(1,6)))
    def test_multiple_range_and_page(self):
        a = list(range(1,6))
        a.append(10)
        b = list(range(20,101))
        full_condition = a+b
        self.assertEqual(list_from_text("1-5,10,20-100"),\
            full_condition)
        self.assertEqual(list_from_text("0,1,2,0-3,5-3"),\
            list(range(0,6)))

    def test_reverse_range(self):
        self.assertEqual(list_from_text("5-1"),\
            list(range(1,6)))
        self.assertEqual(list_from_text("50-23"),\
            list(range(23,51)))
    
    def test_negative(self):
        self.assertEqual(list_from_text("-1"),[])
        self.assertEqual(list_from_text("-1--20"),[])
        self.assertEqual(list_from_text("-1--20,-1,1-5"),list(range(1,6)))



if __name__ == '__main__':
    unittest.main()