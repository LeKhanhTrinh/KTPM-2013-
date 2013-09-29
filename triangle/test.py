'''
Created on Sep 29, 2013

@author: KHANHTRINH
'''
'''
Created on Sep 29, 2013

@author: KHANHTRINH
'''
import unittest
import math
from triangle import detect_triangle

class test(unittest.TestCase):
    def testInputInvalid(self): # Test invalid
        print "Test case 1: a = %r, b = %r, c = %r" % ("-1",2,0)
        self.assertEqual(detect_triangle('a', 2.0, 0), "Gia tri dau vao khong phu hop\n")
        print "Test case 2: a = %r, b = %r, c = %r" % (2,"-1",0)
        self.assertEqual(detect_triangle(2, "-1", 0), "Gia tri dau vao khong phu hop\n")
        print "Test case 3: a = %r, b = %r, c = %r" % (2,0,"-1")
        self.assertEqual(detect_triangle(2,0, "-1"), "Gia tri dau vao khong phu hop\n")
        print "Test case 4: a = %r, b = %r, c = %r" % (1,2,"2^32")
        self.assertEqual(detect_triangle(1, 2.0, 2**32), "Gia tri dau vao khong phu hop\n")
        print "Test case 6: a = %r, b = %r, c = %r" % ("2^32-1","2**32","0")
        self.assertEqual(detect_triangle(2**32-1, 2**32, 0), "Gia tri dau vao khong phu hop\n")
        print "Test case 7: a = %r, b = %r, c = %r" % ("1e-10","2**32","2**32-2")
        self.assertEqual(detect_triangle(1e-10 , 2**32, 2**32-2), "Gia tri dau vao khong phu hop\n")
    def testInputValid(self):   # Test invalid.
        print "Test case 5: a = %r, b = %r, c = %r" % (0,2,"2^32-1")
        self.assertEqual(detect_triangle(0, 2.0, 2**32-1), "Khong phai tam giac\n")
        print "Test case 8: a = %r, b = %r, c = %r" % (1,4,5)
        self.assertEqual(detect_triangle(1.0, 4.0, 5.0), "Khong phai tam giac\n")
        print "Test case 9: a = %r, b = %r, c = %r" % (1,4,"2**32-1")
        self.assertEqual(detect_triangle(1.0, 4.0, 2**32-1), "Khong phai tam giac\n")
        print "Test case 10: a = %r, b = %r, c = %r" % (1,2**32-1,1)
        self.assertEqual(detect_triangle(1.0, 2**32-1, 1), "Khong phai tam giac\n")
        print "Test case 11: a = %r, b = %r, c = %r" % ("1e-10",4,1)
        self.assertEqual(detect_triangle(1e-10, 4.0, 1), "Khong phai tam giac\n")
        print "Test case 12: a = %r, b = %r, c = %r" % ("2**32-1","1e-10","1e-10")
        self.assertEqual(detect_triangle(2**32-1, 1e-10, 1e-10), "Khong phai tam giac\n")
    def testTGVuong(self):  # Tam giac vuong
        print "Test case 13: a = %r, b = %r, c = %r" % (3,4,5)
        self.assertEqual(detect_triangle(3.0, 4.0, 5.0), "Tam giac vuong\n")
        print "Test case 14: a = %r, b = %r, c = %r" % (5*1e-10, 4*1e-10,3*1e-10)
        self.assertEqual(detect_triangle(5*1e-10, 3*1e-10,4*1e-10), "Tam giac vuong\n")
        print "Test case 15: a = %r, b = %r, c = %r" % (4*2**31, 5*2**31,3*2**31)
        self.assertEqual(detect_triangle(4*2**29, 5*2**29,3*2**29), "Tam giac vuong\n")
        print "Test case 33: a = %r, b = %r, c = %r" % (8.0,math.sqrt(48),4.0)
        self.assertEqual(detect_triangle(8.0,math.sqrt(48),4.0), "Tam giac vuong\n")
    def testTGcan(self):    # Tam giac can
        print "Test case 16: a = %r, b = %r, c = %r" % (2,2,1)
        self.assertEqual(detect_triangle(2.0, 2.0, 1.0), "Tam giac can\n")
        print "Test case 17: a = %r, b = %r, c = %r" % ("4e-5", "7e-5", "4e-5")
        self.assertEqual(detect_triangle(4e-5, 7e-5, 4e-5), "Tam giac can\n")
        print "Test case 18: a = %r, b = %r, c = %r" % ("5e-5", "5e-5", "8e-5")
        self.assertEqual(detect_triangle(5e-5, 5e-5, 8e-5), "Tam giac can\n")
        print "Test case 19: a = %r, b = %r, c = %r" % ("5e-5", "3e-5", "3e-5")
        self.assertEqual(detect_triangle(5e-5, 3e-5, 3e-5), "Tam giac can\n")
        print "Test case 20: a = %r, b = %r, c = %r" % ("2**32-1",4,"2**32-1")
        self.assertEqual(detect_triangle(2**32-1, 4, 2**32-1), "Tam giac can\n")
        print "Test case 21: a = %r, b = %r, c = %r" % ("2**32-1","2**32-1",4)
        self.assertEqual(detect_triangle(2**32-1, 2**32-1, 4), "Tam giac can\n")
    # Gioi han 2**26 khi co mot bien < 1
        print "Test case 22: a = %r, b = %r, c = %r" % ("2**32-1","2**32-1","1e-6")
        self.assertEqual(detect_triangle(2**32-1, 2**32-1, 1e-9), "Tam giac can\n")
    def testTGdeu(self):    # Tam giac deu
        print "Test case 23: a = %r, b = %r, c = %r" % (2,2,2)
        self.assertEqual(detect_triangle(2.0, 2.0, 2.0), "Tam giac deu\n")
        print "Test case 24: a = %r, b = %r, c = %r" % ("2**32-1","2**32-1","2**32-1")
        self.assertEqual(detect_triangle(2**32-1, 2**32-1, 2**32-1), "Tam giac deu\n")
        print "Test case 25: a = %r, b = %r, c = %r" % ("1e-10","1e-10","1e-10")
        self.assertEqual(detect_triangle(1e-10, 1e-10, 1e-10), "Tam giac deu\n")
    def testTGvuongcan(self):   # Tam giac vuong can
        print "Test case 26: a = %r, b = %r, c = %r" % (1,1,math.sqrt(2))
        self.assertEqual(detect_triangle(1.0, 1.0, math.sqrt(2.0)), "Tam giac vuong can\n")
        print "Test case 27: a = %r, b = %r, c = %r" % (2,2*math.sqrt(2),2)
        self.assertEqual(detect_triangle(2, 2*math.sqrt(2), 2), "Tam giac vuong can\n")
        print "Test case 28: a = %r, b = %r, c = %r" % (2*math.sqrt(2),2,2)
        self.assertEqual(detect_triangle(2*math.sqrt(2.0), 2.0, 2), "Tam giac vuong can\n")
    def testTGthuong(self):     # Tam giac thuong
        print "Test case 29: a = %r, b = %r, c = %r" % (3, 5, 7)
        self.assertEqual(detect_triangle(3, 5.0, 7.0), "Tam giac binh thuong\n")
        print "Test case 30: a = %r, b = %r, c = %r" % (2, "2^32-1", "2^32-2")
        self.assertEqual(detect_triangle(2, 2**31-5, 2**31-4), "Tam giac binh thuong\n")
    # Gioi han 10**-5 cho e = 10**-10
        print "Test case 31: a = %r, b = %r, c = %r" % (2e-10, 3-5e-10, 3-4e-10)
        self.assertEqual(detect_triangle(2e-10, 3-5e-10, 3-4e-10), "Tam giac binh thuong\n")
        print "Test case 32: a = %r, b = %r, c = %r" % (2e-7, 3e-7, 4e-7)
        self.assertEqual(detect_triangle(2e-7, 3e-7, 4e-7), "Tam giac binh thuong\n")
def main():
    unittest.main()

if __name__ == "__main__":
    main()