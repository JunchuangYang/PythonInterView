__author__ = 'lenovo'
import unittest
from Python_Offer import xxxx

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertFalse(xxxx.solution(s = "mississippi",p = "mis*is*p*."))
        self.assertFalse(xxxx.solution(s = "aa",p = "a"))
        self.assertTrue(xxxx.solution(s = "aa",p = "a*"))
        self.assertTrue(xxxx.solution(s = "aab",p = "c*a*b"))
        self.assertTrue(xxxx.solution(s = "ab",p = ".*"))
        self.assertTrue(xxxx.solution(s = "a",p = "ab*"))
        self.assertFalse(xxxx.solution(s = "ab",p = ".*c"))
        self.assertTrue(xxxx.solution(s = "bbbba",p=".*a*a"))
        self.assertTrue(xxxx.solution(s = "aaaaaaaaaaaaab",p="a*a*a*a*a*a*a*a*a*a*c"))



if __name__ == "__main__":
    t = UnitTest()
    t.test()